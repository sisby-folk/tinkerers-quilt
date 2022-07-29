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


dir_pack = '../out/tinkerers_repair'
dir_recipes = dir_pack + "/data/tinkerer/recipes/"
assert_not_dir(dir_pack)
shutil.copytree('override', dir_pack)
assert_dir(dir_recipes)

armor_durability = [[165, 240, 225, 195],  # Iron
                    [77, 112, 105, 91],  # Golden
                    [363, 528, 495, 429],  # Diamond
                    [407, 592, 555, 481]]  # Netherite
tiers = [("iron", 250), ("golden", 32), ("diamond", 1561), ("netherite", 2031)]
repair = ["iron_ingot", "gold_ingot", "diamond", "netherite_ingot"]
types = ["helmet", "chestplate", "leggings", "boots", "pickaxe", "sword", "shovel", "axe", "hoe"]
type_costs = [5, 8, 7, 4, 3, 2, 1, 3, 2]

for template_name in ["dework", "repair", "upgrade"]:
    with open("./template/smithing.json", "r") as template_file:
        template = json.load(template_file)

        for type_idx, current_type in enumerate(types):
            for tier_idx, current_tier in enumerate(tiers):
                current_dict = deepcopy(template)
                match template_name:
                    case "dework":
                        current_dict["base"]["item"] = "minecraft:" + current_tier[0] + "_" + current_type
                        current_dict["ingredient"]["item"] = "minecraft:netherite_scrap"
                        current_dict["result"]["item"] = "minecraft:" + current_tier[0] + "_" + current_type
                        current_dict["result"]["data"]["RepairCost"] = "$((base.RepairCost + 1)/2)-1"
                        current_dict["result"]["data"]["Damage"] = "$base.Damage"
                    case "repair":
                        durability = current_tier[1] if type_idx > 3 else armor_durability[tier_idx][type_idx]
                        current_dict["base"]["item"] = "minecraft:" + current_tier[0] + "_" + current_type
                        current_dict["ingredient"]["item"] = "minecraft:" + repair[tier_idx]
                        current_dict["result"]["item"] = "minecraft:" + current_tier[0] + "_" + current_type
                        current_dict["result"]["data"]["Damage"] = "$base.Damage - " + str(math.floor(durability / 4.0))
                        current_dict["result"]["data"]["RepairCost"] = "$base.RepairCost"
                    case "upgrade":
                        if current_tier == tiers[0] or type_idx <= 3:  # No iron or armor
                            continue
                        current_dict["base"]["item"] = "minecraft:" + tiers[tier_idx - 2 if current_tier[0] == "diamond" else 1][0] + "_" + current_type
                        current_dict["ingredient"]["item"] = "minecraft:" + repair[tier_idx]
                        current_dict["result"]["item"] = "minecraft:" + current_tier[0] + "_" + current_type
                        current_dict["result"]["data"]["Damage"] = str(math.floor(current_tier[1] * ((type_costs[type_idx] - 1) / 4.0)))
                        current_dict["result"]["data"]["RepairCost"] = "$base.RepairCost"
                with open(dir_recipes + template_name + "_" + current_tier[0] + "_" + current_type + ".json",
                          "w") as out_file:
                    json.dump(current_dict, out_file, indent=4, sort_keys=True)
