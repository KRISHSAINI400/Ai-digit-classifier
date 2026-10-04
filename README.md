# Handwritten Digit Classification using Deep Learning

A deep learning project built using Python and TensorFlow that automatically classifies handwritten digits (0-9) from the MNIST dataset.

## Problem
Recognizing human handwriting is tough for computers because everyone writes differently. This project uses a Deep Neural Network (DNN) to identify digits with high accuracy.

## Dataset
MNIST Dataset: It contains 70,000 grayscale images (28x28 pixels) of handwritten digits from 0 to 9.

## Method
1. Loaded the MNIST dataset directly using TensorFlow Keras.
2. Normalized the pixel values (divided by 255) to scale them between 0 and 1.
3. Created a Sequential Neural Network with a Flatten layer, a Hidden Dense layer (128 units, ReLU activation), and an Output Dense layer (10 units, Softmax activation).
4. Compiled using the Adam optimizer and Sparse Categorical Crossentropy loss.
5. Trained the model for 3 epochs and evaluated it on unseen test data.

## Tools Used
Python, TensorFlow, Keras, Google Colab

## Output & Screenshots
Here is the model training and the final evaluation accuracy:

### Model Training
![Training Process](screenshot1.png)

### Final Test Accuracy
![Model Accuracy](screenshot2.png)

### Live Sample Prediction
![AI Prediction](screenshot3.png)

## How to Run
1. Open the code from `main.py` in Google Colab.
2. Run all the blocks to see live model training and predictions.

## Author
Krish Saini
