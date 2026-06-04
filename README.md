# ml-engineering-workbench

Playground to try ML model development, train it, evaluate it, host it in production, and expose it as an API that can be called from the Java backend.


# Building a model involves the following steps:
## Data - needed to train the model
## Model - A simple model to begin with that forms the base of further training (could start with a linear model, which has straightforward predictability on a plane, vs. non-linear models, which are complex and do not fit on a plane). Ultimately the model will result in either linear or non-linear behavior (non-linear problems are often solved by neural networks) based on the training data and accuracy requirements.
## Objective Function - The formulae used to evaluate if the model output is accurate enough. There are two kinds:
### Loss/Cost function - Lower the value, better the accuracy. Minimizes the error of prediction. Mostly used in supervised learning.
### Gain/Reward function - Opposite of the loss function; higher the value, the better the accuracy. Used in reinforcement learning.
The machine learning process mostly involves optimizing these functions to improve training efficiency and prediction accuracy.
## Optimization Algorithm - This involves techniques to generate different inputs that can be supplied to the model to test and match against the objective function. It is essentially the process of finding gradient descent to generate the input values used to train the model. The rate of learning ('n', also called 'eta') is chosen optimally so that learning time and input quality are balanced efficiently. General considerations for choosing 'eta': the learning rate needs to be high enough to reach the minimum in a reasonable amount of time, or low enough so that we don't oscillate around the minimum.

# Different learning techniques:
## Supervised - The inputs are labelled and the model is tested to match the label for each input.
## Unsupervised - The inputs are not labelled, and the model is trained to come up with a classification based on similarity in the data. This addresses the problem with supervised learning when the dataset is huge and takes a very long time for humans to label. In this learning, the training process involves providing instructions to divide the data into groups (e.g., divide animal photos into two groups—the algorithm will decide the grouping to the best of its abilities—or determine if the weather is sunny or not and respond with True or False). This classification process is also called clustering.

## Reinforcement - Here the algorithm is trained by rewarding it when it meets the expectation, providing it with more motivation to improve its efficiency further.

# Supervised Learning:
Supervised learning involves two types:
## Classification - Produces output like Car or Bike. Uses Cross Entropy.
## Regression - Produces output in the form of a number like 1.24, 4.23, etc. Uses L2-Norm - Euclidean distance of the outputs and the targets. Ei(yi-ti)pow2. Distance away from target - T

# Modelling
This step involves coming up with a base model. In simple terms this is y = f(x). Given a list of input data, the linear model will look like a simple algebra function - f(x) = wx + b. Here x is the input, w is the coefficient, and b is the intercept.
However in ML jargon, w is called the weight and b is the bias. These are called parameters in machine learning.
There are different types to represent a model. e.g., f(x) = xw + b or xpow(T).w + b or wpow(T).x + b
The goal of the machine learning algorithm is to come up with values for w and b to keep f(x) = y as close as possible to the expected result.


# Algebra Tutorials
Algebra forms the basic knowledge needed to train the models. Having a basic understanding not only helps but also makes it all the more sense as we are learning AI/ML. In fact, I would suggest to begin with learning Algebra concepts first.
## Concepts
### Matrices - two-dimensional array. An mxn matrix has m rows and n columns
### A matrix with size 1x1 is a scalar
### A matrix with size 1xn or mx1 is a vector—a horizontal or vertical vector, respectively.
### A vector can be plotted on a 2D plane; two vectors intersect on a plane.
### Matrices of size 1x1, 1xn, mx1, or mxn are all called tensors. A more complex tensor has a third dimension represented as kxmxn, where k denotes matrices in k layers, one behind the other.
### Transpose - inverting the elements in a vector


## Operations
### Addition - requires matrices of the same dimensions to add. e.g., u + v
### Subtraction - requires matrices of the same dimensions to subtract. e.g., u - v
### A vector can be added to a scalar, and that results in each element being incremented by the scalar value. e.g., 5 + u or 5*A
### Multiplication -
Vector multiplication is the basis of modelling. Represent the inputs in one matrix form and the weights and biases as another matrix; the result matrix is the output of the model.
#### Dot Product - elements at the same index are multiplied. e.g., np.dot(u,v)
Multiplying matrices requires the second dimension of the first matrix (m1xk) to match the first dimension of the second matrix (k,n), which results in a matrix of size mxn.
#### Tensor product - This is much more advanced than just the normal matrics multiplication. Here we are dealing with 3D matrics(Rank3, given scalar is rank 0, row or column arry being Rank 1 and m x n being Rank 2)

## Training
Training the model involves below steps
### Inputs gathering : This can be sample data or some realistic data
### Creating Target: These are the ideal value we intend to get
### Initialize variables(here they are literally weights and biases). First we begin with something random. The training is all about arriving at these two values which fit in perfectly to generate the target output with provided inputs.
### Training: Finally we perform the training with above items ready. This step is repeatitive process to be executed multiple time until the Loss Function result is stablitized(remains almost constant)
    - calculate outputs
    - compare outputs to targets through loss
    - print loss
    - Adjust weights and biases
    - Repeat ~
There is one crucial part here which decide the efficiency of this whole process - 'learning rate'. This can be any value from 1.0001 to 1.0. Smaller this value the slower the training runs and need more iterations to arrive at minimized loss output.


