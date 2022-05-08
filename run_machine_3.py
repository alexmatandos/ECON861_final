import kfold_template
import pandas
from sklearn import linear_model
import pickle

dataset = pandas.read_csv("detail_price_dataset.csv")

## applying the same fix as before for 'bathrooms':
bathroom_integer = dataset['bathroom'].astype(str).str.split('.'). str[0].astype(float)
bathroom_decimal = dataset['bathroom'].astype(str).str.split('.'). str[1].astype(float)
dataset['bathroom_fixed'] = bathroom_integer + bathroom_decimal*.5
dataset = dataset.drop(columns = ['bathroom'])

## cleaning for everything else:
dataset = dataset.drop(columns = ['state'])
dataset = pandas.get_dummies(dataset, columns = ['city' ,'maintain', 'sidewalk_access', 'kitchen_quality', 'home_functionality'])

target = dataset['price'].values
data = dataset.drop(columns = ['price', 'image_filename', 'price_range']).values

## running a linear regression, similar to hedonic pricing:
machine = linear_model.LinearRegression()
result = kfold_template.run_kfold(data, target, 4, machine, 0, 0, 0)

print(result[0])

with open("result_5.pickle", "wb") as f:
	pickle.dump(result, f)