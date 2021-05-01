from model_file import NN
from collections import OrderedDict
import torch

def decode_nn():
    real_model = OrderedDict()
    for key, value in NN:
        real_model[key] = torch.FloatTensor(value)
    return real_model


if __name__=="__main__":
    print(decode_nn())
