import pickle
import os

path = os.getcwd()


fname = f'{path}\\feat_scaler.pickle'

with open(file=fname, mode='rb') as f:
    fip_scaler = pickle.load(f)

# print(dir(fip_scaler))
print(fip_scaler.mean_)
print(fip_scaler.var_)
print()