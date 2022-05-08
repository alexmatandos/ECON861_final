import pandas
import pickle

with open("result.pickle", "rb") as f:
	result = pickle.load(f)

with open("result_2.pickle", "rb") as f:
	result_2 = pickle.load(f)

with open("result_3.pickle", "rb") as f:
	result_3 = pickle.load(f)

with open("result_4.pickle", "rb") as f:
	result_4 = pickle.load(f)

with open("result_5.pickle", "rb") as f:
	result_5 = pickle.load(f)

print(result[1])
print(result_2[1])
print(result_3[1])
print(result_4[1])
print(result_5[0])