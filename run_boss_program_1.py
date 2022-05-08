import pandas
import pickle

with open("result.pickle", "rb") as f:
	result = pickle.load(f)

with open("result_2.pickle", "rb") as f:
	result_2 = pickle.load(f)

print(result)
print(result_2)