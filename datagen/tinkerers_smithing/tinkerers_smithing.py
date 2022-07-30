import json
import math
import os
import shutil
from copy import deepcopy


def assert_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def assert_not_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)


dir_pack = '../out/tinkerers_smithing'
dir_recipes = dir_pack + '/data/tinkerer/recipes/'
assert_not_dir(dir_pack)
shutil.copytree('override', dir_pack)
assert_dir(dir_recipes)

armor_durability = [[165, 240, 225, 195],  # Iron
                    [77, 112, 105, 91],  # Golden
                    [363, 528, 495, 429],  # Diamond
                    [407, 592, 555, 481]]  # Netherite
tool_durability = [250, 32, 1561, 2031]
tiers = ['iron', 'golden', 'diamond', 'netherite']
repair = ['iron_ingot', 'gold_ingot', 'diamond', 'netherite_ingot']
types = ['chestplate', 'leggings', 'helmet', 'boots', 'pickaxe', 'sword', 'shovel', 'axe', 'hoe']
type_costs = [8, 7, 5, 4, 3, 2, 1, 3, 2]

with open('./template/smithing.json', 'r') as template_file:
    template = json.load(template_file)

for type_idx, current_type in enumerate(types):
    for tier_idx, current_tier in enumerate(tiers):
        for recipe_type in ['dework', 'dework_final', 'repair', 'repair_final', 'upgrade']:
            current_dict = deepcopy(template)
            current_dict['result']['item'] = 'minecraft:' + current_tier + '_' + current_type

            if recipe_type.startswith('dework'):
                final = recipe_type.endswith('_final')
                current_dict['base']['item'] = 'minecraft:' + current_tier + '_' + current_type
                current_dict['base']['data']['require']["RepairCost"] = 1 if final else '$2..'
                current_dict['ingredient']['item'] = 'minecraft:netherite_scrap'
                current_dict['result']['data']['RepairCost'] = "$0" if final else '$((base.RepairCost + 1)/2)-1'

            if recipe_type.startswith('repair'):
                final = recipe_type.endswith('_final')
                durability = tool_durability[tier_idx] if type_idx > 3 else armor_durability[tier_idx][type_idx]
                durability_restored = math.ceil(durability / 4.0)
                current_dict['base']['item'] = 'minecraft:' + current_tier + '_' + current_type
                current_dict['base']['data']['require']["Damage"] = '$..' + str(durability_restored - 1) if final else '$' + str(durability_restored) + '..'
                current_dict['ingredient']['item'] = 'minecraft:' + repair[tier_idx]
                current_dict['result']['data']['Damage'] = "$0" if final else '$base.Damage - ' + str(durability_restored)

            if recipe_type.startswith('upgrade'):
                if current_tier in ['iron', 'netherite', 'gold'] or type_costs[type_idx] > 5:
                    continue
                current_dict['base']['item'] = 'minecraft:' + tiers[tier_idx - (2 if current_tier == 'diamond' else 1)] + '_' + current_type
                current_dict['ingredient']['item'] = 'minecraft:' + repair[tier_idx]
                current_dict['result']['data']['Damage'] = "$" + str(math.floor(tool_durability[tier_idx] * ((type_costs[type_idx] - 1) / 4.0)))

            with open(dir_recipes + recipe_type + '_' + current_tier + '_' + current_type + '.json', 'w') as out_file:
                json.dump(current_dict, out_file, indent=4, sort_keys=True)


tool_durability = [59, 131, 250]
tiers = ['wooden', 'stone', 'gold', 'iron']
repair = ['planks', 'stone_tool_materials', 'gold_ingot', 'iron_ingot']
repair_type = ['tag', 'tag', 'item', 'item']

with open('./template/shapeless.json', 'r') as template_file:
    template = json.load(template_file)

    for type_idx, current_type in enumerate(types):
        for tier_idx, current_tier in enumerate(tiers):
            for recipe_type in ['repair_single', 'repair_single_final', 'repair_double', 'repair_double_final', 'repair_triple', 'repair_triple_final', 'upgrade']:
                if type_idx < 4:
                    continue

                current_dict = deepcopy(template)
                current_dict['result']['item'] = 'minecraft:' + current_tier + '_' + current_type

                if recipe_type.startswith('repair'):
                    if current_tier in ['iron', 'gold']:
                        continue

                    final = recipe_type.endswith('_final')
                    amount = 3 if 'triple' in recipe_type else (2 if 'double' in recipe_type else 1)

                    if amount > type_costs[type_idx]:
                        continue

                    durability = tool_durability[tier_idx]
                    current_dict['ingredients'][0]['item'] = 'minecraft:' + current_tier + '_' + current_type

                    for _ in range(amount):
                        current_dict['ingredients'] += [{repair_type[tier_idx]: 'minecraft:' + repair[tier_idx]}]

                    durability_restored = math.ceil((durability * amount) / float(type_costs[type_idx]))
                    current_dict['ingredients'][0]['data']['require']["Damage"] = '$..' + str(durability_restored - 1) if final else '$' + str(durability_restored) + '..'
                    current_dict['result']['data']['Damage'] = "$0" if final else '$i0.Damage - ' + str(durability_restored)

                if recipe_type.startswith('upgrade'):
                    if current_tier in ['wooden']:
                        continue
                    current_dict['ingredients'][0]['item'] = 'minecraft:' + tiers[tier_idx - (2 if current_tier in ['iron', 'gold'] else 1)] + '_' + current_type
                    amount = type_costs[type_idx]
                    for _ in range(amount):
                        current_dict['ingredients'] += [{repair_type[tier_idx]: 'minecraft:' + repair[tier_idx]}]

                    current_dict['result']['data']['Damage'] = "$i0.Damage"

                with open(dir_recipes + recipe_type + '_' + current_tier + '_' + current_type + '.json', 'w') as out_file:
                    json.dump(current_dict, out_file, indent=4, sort_keys=True)
