import copy
import json
import math
import os
from copy import deepcopy
#
# origin_template = {
#     "origin": {
#         "codename": "demishort",
#         "name": "Demi-Short",
#         "description": "Demi-Short",
#         "icon": "Demi-Short",
#         "order": 0,
#         "impact": 0,
#     },
#     "power": {
#         "codename": "demishort",
#         "name": "Demi-Short",
#         "description": "Demi-Short",
#         "scale": 0,
#     }
# }
# def get_dicts():
#     current_origins = []
#     for filename in os.listdir("./origins/"):
#         with open("./origins/"+filename, "r") as origin_file:
#             origin_json = json.load(origin_file)
#         with open("./powers/" + filename, "r") as power_file:
#             power_json = json.load(power_file)
#         new_origin = copy.deepcopy(origin_template)
#         new_origin["origin"]["codename"] = filename.split('.')[0]
#         new_origin["power"]["codename"] = filename.split('.')[0]
#         new_origin["origin"]["description"] = origin_json["description"]
#         new_origin["origin"]["icon"] = origin_json["icon"]
#         new_origin["power"]["name"] = power_json["name"]
#         new_origin["power"]["description"] = power_json["description"]
#         new_origin["power"]["scale"] = power_json["scale"]
#         current_origins = current_origins + [new_origin]
#     print(current_origins)

origins = [
    {'origin':  {'codename': 'demishort',       'name': 'Demi-Short',       'description': 'Half-Short',                                                'icon': 'minecraft:honey_bottle'},
     'power':   {'codename': 'demishort',       'name': 'Demi-Short',       'desc-adjective': 'a bit short',                    'desc-height': 1.6, 'desc-sneak-height': 1.4,   'desc-width': 0.5,  'scale-height': 0.9, 'scale-width': 0.9}},
    {'origin':  {'codename': 'demitall',        'name': 'Demi-Tall',        'description': 'Half-Tall',                                                 'icon': 'minecraft:cookie'},
     'power':   {'codename': 'demitall',        'name': 'Demi-Tall',        'desc-adjective': 'slightly taller than average',   'desc-height': 1.9, 'desc-sneak-height': 1.6,   'desc-width': 0.6,  'scale-height': 1.05, 'scale-width': 1.05}},
    {'origin':  {'codename': 'hemidemishort',   'name': 'HemiDemi-Short',   'description': '1/4 Short',                                                 'icon': 'minecraft:potion'},
     'power':   {'codename': 'hemidemishort',   'name': 'HemiDemi-Short',   'desc-adjective': 'ever-so-slightly short',         'desc-height': 1.7, 'desc-sneak-height': 1.5,   'desc-width': 0.6,  'scale-height': 0.95, 'scale-width': 0.95}},
    {'origin':  {'codename': 'impish',          'name': 'Impish',           'description': '1.5x Short\nMinor gameplay impact.',                        'icon': 'minecraft:water_bucket'},
     'power':   {'codename': 'impish',          'name': 'Impish',           'desc-adjective': 'impishly short',                 'desc-height': 1.3, 'desc-sneak-height': 1,      'desc-width': 0.4,  'scale-height': 0.66, 'scale-width': 0.66}},
    {'origin':  {'codename': 'oversize1',       'name': 'Oversize',         'description': "'Neat.'\nMedium gameplay impact.",                          'icon': 'minecraft:pumpkin_pie'},
     'power':   {'codename': 'oversize1',       'name': 'Oversize',         'desc-adjective': 'oversized',                      'desc-height': 3,   'desc-sneak-height': 2.5,   'desc-width': 1,    'scale-height': 1.62, 'scale-width': 1.62}},
    {'origin':  {'codename': 'oversize2',       'name': 'Oversize II',      'description': "'Sheesh.'\nMajor gameplay impact.",                         'icon': 'minecraft:cake'},
     'power':   {'codename': 'oversize2',       'name': 'Oversize II',      'desc-adjective': 'very oversized',                 'desc-height': 3.5, 'desc-sneak-height': 3,     'desc-width': 1.2,    'scale-height': 1.92, 'scale-width': 1.92}},
    {'origin':  {'codename': 'oversize3',       'name': 'Oversize III',     'description': "'Yikes.'\nMajor gameplay impact.",                          'icon': 'minecraft:hay_block'},
     'power':   {'codename': 'oversize3',       'name': 'Oversize III',     'desc-adjective': 'extremely oversized',            'desc-height': 4,   'desc-sneak-height': 3.5,   'desc-width': 1.3,    'scale-height': 2.2, 'scale-width': 2.2}},
    {'origin':  {'codename': 'semishort',       'name': 'Semi-Short',       'description': '3/4 Short',                                                 'icon': 'minecraft:splash_potion'},
     'power':   {'codename': 'semishort',       'name': 'Semi-Short',       'desc-adjective': 'quite short',                    'desc-height': 1.6, 'desc-sneak-height': 1.3,   'desc-width': 0.5,  'scale-height': 0.85, 'scale-width': 0.85}},
    {'origin':  {'codename': 'short',           'name': 'Short',            'description': '\'It\'s a bit drafty actually.\'',                          'icon': 'minecraft:experience_bottle'},
     'power':   {'codename': 'short',           'name': 'Short',            'desc-adjective': 'very short',                     'desc-height': 1.5, 'desc-sneak-height': 1.2,   'desc-width': 0.6,  'scale-height': 0.8, 'scale-width': 0.8}},
    {'origin':  {'codename': 'sized',           'name': 'Sized',            'description': '\'This is fine too.\'',                                     'icon': 'minecraft:milk_bucket'},
     'power':   {'codename': 'sized',           'name': 'Sized',            'desc-adjective': 'average sized',                  'desc-height': 1.8, 'desc-sneak-height': 1.5,   'desc-width': 0.6,  'scale-height': 1, 'scale-width': 1}},
    {'origin':  {'codename': 'tall',            'name': 'Tall',             'description': '\'How\'s the weather down there?\'',                        'icon': 'minecraft:apple'},
     'power':   {'codename': 'tall',            'name': 'Tall',             'desc-adjective': 'taller than average',            'desc-height': 2,   'desc-sneak-height': 1.7,   'desc-width': 0.7,  'scale-height': 1.1, 'scale-width': 1.1}},
    {'origin':  {'codename': 'taller',          'name': 'Taller',           'description': "'How's the weather down *there*?'\nMinor gameplay impact.", 'icon': 'minecraft:bread'},
     'power':   {'codename': 'taller',          'name': 'Taller',           'desc-adjective': 'tall',                           'desc-height': 2.2, 'desc-sneak-height': 1.8,   'desc-width': 0.7,  'scale-height': 1.2, 'scale-width': 1.2}},
    {'origin':  {'codename': 'tallest',         'name': 'Tallest',          'description': "'Watch your head.'\nMinor gameplay impact.",                'icon': 'minecraft:mushroom_stew'},
     'power':   {'codename': 'tallest',         'name': 'Tallest',          'desc-adjective': 'extremely tall',                 'desc-height': 2.4, 'desc-sneak-height': 2,     'desc-width': 0.8,  'scale-height': 1.33, 'scale-width': 1.33}},
    {'origin':  {'codename': 'orcish',         'name': 'Orcish',          'description': "'Intimidated?'\nMinor gameplay impact.",                'icon': 'minecraft:mushroom_stew'},
     'power':   {'codename': 'orcish',         'name': 'Orcish',          'desc-adjective': 'larger and broader',                 'desc-height': 2.4, 'desc-sneak-height': 2,     'desc-width': 1,  'scale-height': 1.33, 'scale-width': 1.56}}]

with open("./template_" + "origin" + ".json", "r") as origin_template_file:
    with open("./template_" + "power" + ".json", "r") as power_template_file:
        origin_template = json.load(origin_template_file)
        power_template = json.load(power_template_file)

        for origin_dict in origins:
            current_origin_file = copy.deepcopy(origin_template)
            current_power_file = copy.deepcopy(power_template)

            current_origin_file["powers"] = ["tinkerer:" + origin_dict["power"]["codename"]]
            current_origin_file["icon"] = origin_dict["origin"]["icon"]
            current_origin_file["name"] = origin_dict["origin"]["name"]
            current_origin_file["description"] = origin_dict["origin"]["description"]

            current_power_file["name"] = origin_dict["power"]["name"]
            current_power_file["description"] = "You\'re " + origin_dict["power"]["desc-adjective"] + " (" + str(math.floor(origin_dict["power"]["scale-height"] * 100)) + "%)!" +\
                                                "\nHeight: " + str(origin_dict["power"]["desc-height"]) + (" Block" if origin_dict["power"]["desc-height"] == 1 else " Blocks") +\
                                                "\nSneak Height: " + str(origin_dict["power"]["desc-sneak-height"]) + (" Block" if origin_dict["power"]["desc-sneak-height"] == 1 else " Blocks") +\
                                                "\nWidth: " + str(origin_dict["power"]["desc-width"]) + (" Block Exactly" if origin_dict["power"]["desc-width"] == 1 else " Blocks")
            current_power_file["entity_action_chosen"]["actions"][0]["command"] = str(current_power_file["entity_action_chosen"]["actions"][0]["command"]).replace("{{ scale_height }}", str(origin_dict["power"]["scale-height"]))
            current_power_file["entity_action_chosen"]["actions"][1]["command"] = str(current_power_file["entity_action_chosen"]["actions"][1]["command"]).replace("{{ scale_width }}", str(origin_dict["power"]["scale-width"]))

            with open("./origins/" + origin_dict["origin"]["codename"] + ".json", "w") as out_file:
                json.dump(current_origin_file, out_file, indent=4, sort_keys=True)
            with open("./powers/" + origin_dict["power"]["codename"] + ".json", "w") as out_file:
                json.dump(current_power_file, out_file, indent=4, sort_keys=True)
