import pandas
import os
import glob
import imageio
import math
import numpy

## fixing the bathroom variable:
dataset = pandas.read_csv("dataset.csv")

bathroom_integer = dataset['bathroom'].astype(str).str.split('.'). str[0].astype(float)
bathroom_decimal = dataset['bathroom'].astype(str).str.split('.'). str[1].astype(float)

dataset['bathroom_fixed'] = bathroom_integer + bathroom_decimal*.5
dataset = dataset.drop(columns = ['bathroom'])

## removing state, since all observations are located in California, and removing home functionality:
#print(set(dataset['state']))
dataset = dataset.drop(columns = ['state'])
dataset = dataset.drop(columns = ['sidewalk_access'])
dataset = dataset.drop(columns = ['kitchen_quality'])
dataset = dataset.drop(columns = ['home_functionality'])

## checking for weird values in the covariates:
#print(set(dataset['price_range']))
#print(set(dataset['maintain']))
#print(set(dataset['sidewalk_access']))
#print(set(dataset['kitchen_quality']))
#print(set(dataset['home_functionality']))

## getting dummies for 'city', 'price_range', 'maintain', 'sidewalk_access', 'kitchen_quality', 'home_functionality':

dataset = pandas.get_dummies(dataset, columns = ['city', 'maintain'])

## getting categorical variables for the variable that shall be forecasted, 'price_range':

codes, uniques = pandas.factorize(dataset['price_range'])
dataset['price_range_categorical'] = codes
dataset = dataset.drop(columns = ['price_range'])

## getting the rgb data from the image files:

def get_rgb(file_path):
	imimage = imageio.imread(file_path, pilmode = "RGB")
	imimage = imimage/255
	#imimage = imimage.sum(axis = 0).sum(axis = 0)/(imimage.shape[0]*imimage.shape[1])
	imimage_top = imimage[0:math.ceil(imimage.shape[0]/2), :]
	imimage_bottom = imimage[math.ceil(imimage.shape[0]/2):imimage.shape[0], :]
	imimage_top = imimage_top.sum(axis = 0).sum(axis = 0)/(imimage_top.shape[0]*imimage_top.shape[1])
	imimage_bottom = imimage_bottom.sum(axis = 0).sum(axis = 0)/(imimage_bottom.shape[0]*imimage_bottom.shape[1])
	imimage = numpy.concatenate((imimage_top, imimage_bottom))
	return imimage

def read_picture_folder(folder_name):
	results = pandas.DataFrame()
	for file_path in glob.glob(folder_name + "/*"):
		print(file_path)
		image_features = pandas.DataFrame(get_rgb(file_path))
		image_features = pandas.DataFrame.transpose(image_features)
		image_features['image_filename'] = file_path.replace(folder_name + "\\", "")
		results = pandas.concat([results, image_features])
	results = results.rename(columns = {0: "Red", 1: "Green", 2: "Blue"})
	return results

image_dataset = read_picture_folder("image_files")

print(image_dataset)
dataset = pandas.merge(dataset, image_dataset, on = 'image_filename')
dataset.columns = dataset.columns.str.replace("\n", "")

dataset.to_csv("dataset_clean.csv")
