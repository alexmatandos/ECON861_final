import kfold_template
import pandas
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
import pickle

dataset = pandas.read_csv("dataset_clean.csv")
print(dataset)

## removing observations between rows 10000 and 12000:
dataset = dataset[(dataset['Unnamed: 0'] < 9999) | (dataset['Unnamed: 0'] > 11999)]
print(dataset)

target = dataset['price_range_categorical'].values
data = dataset.drop(columns = ['Unnamed: 0' ,'image_filename', 'price_range_categorical']).values
print(target)
print(data)

machine = RandomForestClassifier(criterion = "gini", max_depth = 10, n_estimators = 300 ,bootstrap = True, max_features = "auto")
result = kfold_template.run_kfold(data, target, 4, machine, 1, 1, 1)

print(result[1])
for x in result[2]:
	print(x)
print(result[3])

machine_2 = linear_model.LogisticRegression(max_iter = 1000)
result_2 = kfold_template.run_kfold(data, target, 4, machine_2, 1, 1, 1)

print(result_2[1])
for x in result_2[2]:
	print(x)
print(result_2[3])

with open("result_3.pickle", "wb") as f:
	pickle.dump(result, f)

with open("result_4.pickle", "wb") as f:
	pickle.dump(result_2, f)