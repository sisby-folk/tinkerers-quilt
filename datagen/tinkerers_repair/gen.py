import json
import math
from copy import deepcopy

armor_durability = [[165, 240, 225, 195],  # Iron
                    [77, 112, 105, 91],  # Golden
                    [363, 528, 495, 429],  # Diamond
                    [407, 592, 555, 481]]  # Netherite
tiers = [("iron", 250), ("golden", 32), ("diamond", 1561), ("netherite", 2031)]
repair = ["iron_ingot", "gold_ingot", "diamond", "netherite_ingot"]
types = ["helmet", "chestplate", "leggings", "boots", "pickaxe", "sword", "shovel", "axe", "hoe"]

for template_name in ["dework", "repair"]:
    with open("./template_" + template_name + ".json", "r") as template_file:
        template = json.load(template_file)

        for type_idx, current_type in enumerate(types):
            for tier_idx, current_tier in enumerate(tiers):
                item_string = "minecraft:" + current_tier[0] + "_" + current_type
                repair_item_string = "minecraft:" + repair[tier_idx]
                durability = current_tier[1] if type_idx > 3 else armor_durability[tier_idx][type_idx]
                current_dict = deepcopy(template)
                current_dict["base"]["item"] = item_string
                current_dict["result"]["item"] = item_string
                if template_name == "repair":
                    current_dict["ingredient"]["item"] = repair_item_string
                    current_dict["result"]["data"]["Damage"] = "$base.Damage - " + str(math.ceil(durability / 4))
                with open("./recipes/" + template_name + "_" + current_tier[0] + "_" + current_type + ".json",
                          "w") as out_file:
                    json.dump(current_dict, out_file, indent=4, sort_keys=True)
