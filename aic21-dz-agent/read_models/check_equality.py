import torch
from import_file import NN


file_name = "1_eval"
to_save = []
real_nn = torch.load(file_name)

tests = []

keys1 = [key for key in real_nn]
keys2 = [key for key in NN]

print("> Keys are equal? ", keys1==keys2)
tests.append(keys1==keys2)

for key in keys1:
	eq = torch.all(real_nn[key].eq(NN[key]))
	tests.append(eq)
	print(f"> Item {key} are equal? ", eq)

print("="*50)
print("> All tests done. Final result: ", all(tests))