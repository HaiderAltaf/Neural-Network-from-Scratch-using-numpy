# -*- coding: utf-8 -*-
"""Question_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iiY15hAKjrZNTfpjtp7A0SOT-PSFOQse

# Question 1
Download the fashion-MNIST dataset and plot 1 sample image for each class. Show each sample class in wandb
"""
import numpy as np
import pandas as pd
from keras.datasets import fashion_mnist
import matplotlib.pyplot as plt
import math

## installing the wandb 
!pip install wandb
import wandb

## split the dataset into train and test
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
X_train = x_train.reshape(x_train.shape[0], x_train.shape[1]*x_train.shape[2] )/255
X_test = x_test.reshape(x_test.shape[0], x_test.shape[1]*x_test.shape[2])/255

## split the train dataset for the validation of the model(10%)

validation_size = int(len(X_train)*0.1)
# randomly shuffle the indices of the data
shuffled_indices = np.random.permutation(len(X_train))
# split the shuffled data into training and validation sets
train_indices, validation_indices = shuffled_indices[:-validation_size], shuffled_indices[-validation_size:]
X_train, X_validation = X_train[train_indices], X_train[validation_indices]
y_train, y_validation = y_train[train_indices], y_train[validation_indices]

## initialized the wandb project
wandb.init(entity= "am22s020", project="cs6910_trial")

"""# Function to plot images of each class present in the fashion mnist dataset"""

def plot_class_sample():

  """
  This function is used to print images of all classes present in our dataset,
  and export to wandb to add in report.
  
  """
  class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal',
                'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
            
  no_of_classes = len(class_names)

  list_of_images  = []   # to give to the wandb

  for i in range(no_of_classes):
    
      # Find the index of the first image of each class
      idx = np.where(y_train == i)[0][0]
      
      # Plot the image
      image = X_train[idx].reshape(28,28)
      list_of_images.append((image, class_names[i]))

  # Plot the images in a grid
  fig, axes = plt.subplots(1, no_of_classes, figsize=(12,5))
  for i in range(no_of_classes):
      image, label = list_of_images[i]
      axes[i].imshow(image, cmap='gray')
      axes[i].set_title(label)
      axes[i].axis('off')

  wandb.log({"Question 1": [wandb.Image(img, caption=caption) for img, caption in list_of_images]})

"""Run the function to see result"""

plot_class_sample()