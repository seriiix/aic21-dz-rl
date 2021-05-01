from collections import OrderedDict
import json
import torch


file_name = "1_eval"
to_save = []
to_read = torch.load(file_name)
imports = ""
for key, tensor in to_read.items():
    listed = tensor.tolist()
    print(tensor.size)
    if key == "fc1.weight":
        for i in range(len(tensor)):
            key = key.replace('.', '_')
            name = f"V_{key}_{i}"
            listed = tensor[i].tolist()
            imports += f"from {name} import {name.upper()}\n"
            with open(f"{name}.py", "a") as outfile:
                outfile.write(name.upper())
                outfile.write(" = ")
                json.dump(listed, outfile)

    else:
        key = key.replace('.', '_')
        name = f"V_{key}" 
        imports += f"from {name} import {name.upper()}\n"
        with open(f"{name}.py", "a") as outfile:
            outfile.write(name.upper())
            outfile.write(" = ")
            json.dump(listed, outfile)
    # to_save.append((key, listed))

# ONLY WHEN WE CHANGE THE DIMENSIONS WE UNCOMMENT THIS 
# with open(f"import_file.py", "w") as outfile:
            # outfile.write(imports)

