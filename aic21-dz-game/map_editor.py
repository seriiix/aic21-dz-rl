import json

with open("map.json", 'rb') as f:
    map = josn.loads(f)


# CODE HERE

map[2][3]["cell_type"] = map[2][3]["cell_type"] # 0 or 2
map[2][3]["rec1"] = 0 # Grass
map[2][3]["rec2"] = 0 # Bread

# # # # #

with open("map.json", 'w') as f:
    json.dump(map, f)