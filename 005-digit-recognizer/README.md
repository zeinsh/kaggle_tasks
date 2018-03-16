# Digit Recognizer

dataset : MNIST data
task type: multi class classification
[task link](https://www.kaggle.com/c/digit-recognizer/)

[model 1.0](https://github.com/zeinsh/kaggle_tasks/blob/master/005-digit-recognizer/model1.0.ipynb)
Keras - Convolutionl neural network - LeNet5
Test accuracy achieved on kaggle : 0.98657

-----------------

[model 1.1](https://github.com/zeinsh/kaggle_tasks/blob/master/005-digit-recognizer/model1.1.ipynb)
Keras - Convolutionl neural network - LeNet5 
Add BatchNormalization layer to the previous model
Test accuracy achieved on kaggle : 0.9909

---------------

[model 2.0](https://github.com/zeinsh/kaggle_tasks/blob/master/005-digit-recognizer/model2.ipynb)

tensorflow

## MLP model2 

### Structure

- Input layer 784 elements
- Hidden layer 1, 25 neurons, relu activation
- Hidden layer 2, 12 neurons, relu activation
- Output layer 10 neurons, sigmoid activation



- Number of iterations 100
- Batch gradient descent, batch size 64
- Loss function: softmax_cross_entropy_with_logits
- Xavier initialization
- Adam optimization algoithm for backpropogation
    - learning rate 0.001



* generalization score (on kaggle) 0.94957 
* training accuracy: 0.97548
* validation accuracy: 0.9469
* training time: 1min 46s

----------------------

[model 2.1](https://github.com/zeinsh/kaggle_tasks/blob/master/005-digit-recognizer/model2.1.ipynb)

tensorflow

## MLP model2.1 

### Structure

- Input layer 784 elements
- Hidden layer 1, 200 neurons, relu activation, droupout prob=0.8
- Hidden layer 2, 200 neurons, relu activation, droupout prob=0.8
- Output layer 10 neurons, sigmoid activation



- Number of iterations 100
- Batch gradient descent, batch size 64
- Loss function: softmax_cross_entropy_with_logits
- Xavier initialization
- Adam optimization algoithm for backpropogation
    - learning rate 0.001



* generalization score (on kaggle) 0.973 
* training accuracy: 0.99148
* validation accuracy: 0.96786
* training time: 3min 7s

----------------------
