# ml-engineering-workbench

Playground to try ML model development, train it, evaluate, host it in production and expose as an API which can be called from the Java backend.


# Building model involves below steps:
## Data - needed to train the model
## Model - A simple model to begin with that forms the base of further training(could start with linear model- which has straightforward predictability on a plane, vs non-linear, which are complex and do not fit in the plane). Ultimatiely the model will result in either the linear an non-linear(solved by neural networks) based on the training data and the accuracy needs.
## Objective Funtion - The formulae used to evalute if the model output is accurate enough. There are two kinds,
### Loss/Cost function - Lower the value, better the accuracy. Minimizes the error of prediction. Mostly used i Supervised learning.
### Gain/Reward function - Opposite to the Loss function, higher the value better the accuracy. Used in Reinforced Learning.
The Machine learning process mostly involves optimizing these functions to improve the training efficiency and accuracy of predictability.
## Optimization Algorithm - This involves technique to generate different inputs that can be supplied to the model to test and match to the Objective Function. It essentially the process to find out the Gradient Descent to generate the input values used to train the model. The rate of learning ('n', also called as 'eta') is chosen optimally such that the learning time vs the quality of inputs are efficiently selected. General considerations to arrive at 'eta' - The learning needs to be high enough to reach the minimum in reasonable amount of time. Or low enough so that we dont oscillate around minimum.

# Different learning techniques:
## Supervised - The inputs are labelled and the mdoel is tested to match the label for each input data
## Unsupervised -  The inputs are not labbled, and the model is trained to come up a classification based on similarity of the data. This will solve the problem with the supervised learning when the data set is huge and takes very long time for human to label. In this learning the training process involves providing instrutions to divide the data into groups(ex. Divide animal photos into two groups(algorithm will decide the grouping to the best of its abilities) or determine if the weather is sunny or not - respond with True or False). This classification process is also called as Clustering.

## Reinforcement - Here the algorithm is trained by rewarding it when its meets the expection, providing it more motivation to improve its efficiency further.

# Supervised Learning:
The supervised learning involves two types,
## Classification - Produces output like, Car or Bike. Uses Cross Entropy.
## Regression - Produces output in the form in a number like, 1.24, 4.23, etc. Uses L2-Norm - Euclidean distance of the outputs and the targets. Ei(yi-ti)pow2. Distance away from Target - T

# Modelling
This step involves coming up a base model. In simple terms this is a y = f(x). Given a list of input data the linear model will look like a simple Algebra function - f(x) = wx + b. Here the x is the input, w is co-efficient and b is intercept. 
However in the ML jargon the w is called the weight and b in the bia(s). These are called a Parameters in machine learning.
There are diffrent types to represnt a model. ex: f(x) = xw + b or xpow(T).w + b or wpow(T).x + b
The goal of the machine learning algorith is to come up with the values for w and b to keep the f(x) = y as close as possible to the expected result.


# Algebra Tutorials
## Concepts
### Matrices two dimentional array. An mxn matrix has m rows and n columns
### A matrix with size 1x1 is scaler
### A matrix with size as 1xn or mx1 is a vector, a horzontal and vertical vector respectively.
### A vector can be plotted on  2D plane, two vector intersect on a plane.
### matrices of size 1x1, 1xn, mx1 or mxn are all called Tensors. More comlpex tensor is something which has third dimension represented as kxmxn, where k denotes  matrices in k layers one behing the other.
### Transpose - inverting the element in a vector


## Operations
### Addition - need same dimension(forms) matrices to add Ex: u + v
### Substraction - need same dimension matrices to substract Ex: u-v
### A vector can be added to scalar, and that results in each element to be incremented by the scalar value. Ex: 5 + u or 5*A
### Multiplication - 
Vector multiplication is the basis of the modelling. represent the inputs in one matrix form and the weights and biases as another matrix, the result matrix is the result of the model.
#### Dot Product - element at same index are multiplied ex: np.dot(u,v)
Multiplying matrics will need the 2nd dimension of first matrix(m1xk) to match with the first dimension of second matrix(k,n), which results in matric of size mxn. 
#### Tensor product - 
