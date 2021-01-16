from pandas import np

###########################################################
# Model of neural network with two inputs and three outputs
###########################################################
# I1 o o O1
#     X  O2
# I2 o o O3

def feedForwardNetwork(inputs, weights, bias):
    relu_v = np.vectorize(relu)
    output = relu_v(np.dot(inputs, weights[0]) + bias[0])
    return output[-1].tolist().index(max(output[-1].tolist()))

def relu(x):
    return max(0, x)