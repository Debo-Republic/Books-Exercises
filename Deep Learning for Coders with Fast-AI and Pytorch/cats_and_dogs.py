# Program to differentiate using dogs and cats.

# Import all functions of methods contained in the vision module of FastAI.
from fastai.vision.all import *
# Download and decompose the training data of cats in the computer 
# URL.Pets is to show that fastAI already has access to pre-existing number of datasets
# Untar_data returns the paths where the images has been decompressed
path = untar_data(URL.PETS/'images')

