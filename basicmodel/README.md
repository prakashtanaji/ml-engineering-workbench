# numpy-aiml.ipynb:
## This model training is all based on the numpy library. The matric multiplications for training are all conducted using the system CPU. The model training using this method is very slow and inefficient, however its a good starting point to learn about the ML training and provides clarity on the exact steps involved unlike the advances frameworks which abstract lot of details. 

# tensor-aiml.ipynb
## The trensor-flow library is open sourced by Google in 2015 and it provides most sophisticated highly evolved toolingn to train the model as well as model inferencing.
The Tensor flow is enabled with high level API provided by Keras. The advantage is, Keras allows to integrate with various low level operations through frameworks like - TensorFlow, PyTorch, JAX(newer framework from Google).
The benefit of Keras is, the same APIs could be used to switch between different framworks without having to rewrite the code.


The code to train the model with TensorFlow follows similar structure as with numpy.
It still needs same four ingredients:
1) Data
2) Model
3) Objective Function
4) Optimization Algorithm

The tensor flow provides much similar and abstracted way to train the model but with much ease and efficiency.


