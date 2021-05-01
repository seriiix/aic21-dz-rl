from collections import OrderedDict
import json
import torch


file_name = "1_eval"
to_save = []
to_read = torch.load(file_name)
print(to_read["FC1.WEIGHT".lower()])