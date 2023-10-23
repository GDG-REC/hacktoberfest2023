import numpy as np

class NN:
    """
    A class to represent a simple feedforward Neural Network with methods for both forward and backward propagation.
    """

    def __init__(self, layer_dims):
        """
        Constructor for the NN class.

        Parameters:
        - layer_dims: List of dimensions for each layer in the network
        """
        self.parameters = self.initialize_parameters_deep(layer_dims)

    def initialize_parameters(self, n_x, n_h, n_y):
        """
        Argument:\n
        n_x -- size of the input layer\n
        n_h -- size of the hidden layer\n
        n_y -- size of the output layer\n

        \nReturns:\n
        parameters -- python dictionary containing your parameters:
                        W1 -- weight matrix of shape (n_h, n_x)\n
                        b1 -- bias vector of shape (n_h, 1)\n
                        W2 -- weight matrix of shape (n_y, n_h)\n
                        b2 -- bias vector of shape (n_y, 1)\n
        """
        W1 = np.random.randn(n_h,n_x) * 0.01
        b1 = np.zeros((n_h,1))
        W2 = np.random.randn(n_y,n_h) * 0.01
        b2 = np.zeros((n_y,1))
        return {"W1": W1, "b1": b1, "W2": W2, "b2": b2}

    def initialize_parameters_deep(self, layer_dims):
        """
        Arguments:
        layer_dims -- python array (list) containing the dimensions of each layer in the network\n

        Returns:\n
        parameters -- python dictionary containing your parameters "W1", "b1", ..., "WL", "bL":\n
                        Wl -- weight matrix of shape (layer_dims[l], layer_dims[l-1])\n
                        bl -- bias vector of shape (layer_dims[l], 1)\n
        """
        parameters = {}
        L = len(layer_dims)

        for l in range(1, L):
            parameters['W' + str(l)] = np.random.randn(layer_dims[l], layer_dims[l-1]) * 0.01
            parameters['b' + str(l)] = np.zeros((layer_dims[l],1))

        return parameters

    def linear_forward(self, A, W, b):
        """
        Implement the linear part of a layer's forward propagation.\n

        Arguments:\n
        A -- activations from previous layer (or input data): (size of previous layer, number of examples)\n
        W -- weights matrix: numpy array of shape (size of current layer, size of previous layer)\n
        b -- bias vector, numpy array of shape (size of the current layer, 1)\n

        Returns:\n
        Z -- the input of the activation function, also called pre-activation parameter\n
        cache -- a python tuple containing "A", "W" and "b" ; stored for computing the backward pass efficiently
        """
        Z = np.dot(W, A) + b
        return Z, (A, W, b)

    def linear_activation_forward(self, A_prev, W, b, activation):
        """
        Implement the forward propagation for the LINEAR->ACTIVATION layer\n

        Arguments:
        A_prev -- activations from previous layer (or input data): (size of previous layer, number of examples)\n
        W -- weights matrix: numpy array of shape (size of current layer, size of previous layer)\n
        b -- bias vector, numpy array of shape (size of the current layer, 1)\n
        activation -- the activation to be used in this layer, stored as a text string: "sigmoid" or "relu"\n

        Returns:\n
        A -- the output of the activation function, also called the post-activation value\n
        cache -- a python tuple containing "linear_cache" and "activation_cache";
                        stored for computing the backward pass efficiently\n
        """
        if activation == "sigmoid":
            Z, linear_cache = self.linear_forward(A_prev, W, b)
            A, activation_cache = self.sigmoid(Z)
        elif activation == "relu":
            Z, linear_cache = self.linear_forward(A_prev, W, b)
            A, activation_cache = self.relu(Z)

        return A, (linear_cache, activation_cache)

    def L_model_forward(self, X):
        """
        Implement forward propagation for the [LINEAR->RELU]*(L-1)->LINEAR->SIGMOID computation\n

        Arguments:\n
        X -- data, numpy array of shape (input size, number of examples)\n
        parameters -- output of initialize_parameters_deep()\n

        Returns:\n
        AL -- activation value from the output (last) layer\n
        caches -- list of caches containing:\n
                    every cache of linear_activation_forward() (there are L of them, indexed from 0 to L-1)
        """
        caches = []
        A = X
        L = len(self.parameters) // 2

        for l in range(1, L):
            A_prev = A
            A, cache = self.linear_activation_forward(A_prev, self.parameters['W' + str(l)], self.parameters['b' + str(l)], "relu")
            caches.append(cache)

        AL, cache = self.linear_activation_forward(A, self.parameters['W' + str(L)], self.parameters['b' + str(L)], "sigmoid")
        caches.append(cache)

        return AL, caches

    def compute_cost(self, AL, Y):
        """
        Implement the cost function\n

        Arguments:\n
            AL -- probability vector corresponding to your label predictions, shape : (1, number of examples)\n
            Y -- true "label" vector\n

        Returns:\n
        cost -- cross-entropy cost
        """
        m = Y.shape[1]
        cost = (-1/m) * (np.dot(Y, np.log(AL).T) + np.dot((1-Y), np.log(1-AL).T))
        return np.squeeze(cost)

    def linear_backward(self, dZ, cache):
        """
        Implement the linear portion of backward propagation for a single layer (layer l)\n

        Arguments:
            dZ -- Gradient of the cost with respect to the linear output (of current layer l)\n
            cache -- tuple of values (A_prev, W, b) coming from the forward propagation in the current layer\n

        Returns:\n
        dA_prev -- Gradient of the cost with respect to the activation (of the previous layer l-1), same shape as A_prev\n
        dW -- Gradient of the cost with respect to W (current layer l), same shape as W\n
        db -- Gradient of the cost with respect to b (current layer l), same shape as b
        """
        A_prev, W, b = cache
        m = A_prev.shape[1]
        dW = (1/m) * np.dot(dZ, A_prev.T)
        db = (1/m) * np.sum(dZ, axis=1, keepdims=True)
        dA_prev = np.dot(W.T, dZ)
        return dA_prev, dW, db

    def linear_activation_backward(self, dA, cache, activation):
        """
        Implement the backward propagation for the LINEAR->ACTIVATION layer.\n

        Arguments:
            dA -- post-activation gradient for current layer l\n
            cache -- tuple of values (linear_cache, activation_cache) we store for computing backward propagation efficiently\n
            activation -- the activation to be used in this layer, stored as a text string: "sigmoid" or "relu"\n

        Returns:\n
        dA_prev -- Gradient of the cost with respect to the activation (of the previous layer l-1), same shape as A_prev\n
        dW -- Gradient of the cost with respect to W (current layer l), same shape as W\n
        db -- Gradient of the cost with respect to b (current layer l), same shape as b
        """
        linear_cache, activation_cache = cache

        if activation == "relu":
            dZ = self.relu_backward(dA, activation_cache)
        elif activation == "sigmoid":
            dZ = self.sigmoid_backward(dA, activation_cache)

        return self.linear_backward(dZ, linear_cache)

    def L_model_backward(self, AL, Y, caches):
        """
        Implement the backward propagation for the [LINEAR->RELU] * (L-1) -> LINEAR -> SIGMOID group

        Arguments:\n
            AL -- probability vector, output of the forward propagation (L_model_forward())\n
            Y -- true "label" vector (containing 0 if non-cat, 1 if cat)\n
            caches -- list of caches containing:\n
                every cache of linear_activation_forward() with "relu" (it's caches[l], for l in range(L-1) i.e l = 0...L-2)\n
                the cache of linear_activation_forward() with "sigmoid" (it's caches[L-1])\n

        Returns:\n
            grads -- A dictionary with the gradients\n
                grads["dA" + str(l)] = ...\n
                grads["dW" + str(l)] = ...\n
                grads["db" + str(l)] = ...
        """
        grads = {}
        L = len(caches)
        Y = Y.reshape(AL.shape)
        dAL = - (np.divide(Y, AL) - np.divide(1 - Y, 1 - AL))

        current_cache = caches[L-1]
        grads["dA" + str(L-1)], grads["dW" + str(L)], grads["db" + str(L)] = self.linear_activation_backward(dAL, current_cache, "sigmoid")

        for l in reversed(range(L-1)):
            current_cache = caches[l]
            dA_prev_temp, dW_temp, db_temp = self.linear_activation_backward(grads["dA" + str(l + 1)], current_cache, activation = "relu")
            grads["dA" + str(l)] = dA_prev_temp
            grads["dW" + str(l + 1)] = dW_temp
            grads["db" + str(l + 1)] = db_temp
        return grads

    def update_parameters(self, grads, learning_rate):
        """
        Update parameters using gradient descent\n

        Arguments:
            params -- python dictionary containing your parameters\n
            grads -- python dictionary containing your gradients, output of L_model_backward

        Returns:
            parameters -- python dictionary containing your updated parameters\n
                    parameters["W" + str(l)] = ...\n
                    parameters["b" + str(l)] = ...
        """
        L = len(self.parameters) // 2
        for l in range(L):
            self.parameters["W" + str(l+1)] -= learning_rate * grads["dW" + str(l+1)]
            self.parameters["b" + str(l+1)] -= learning_rate * grads["db" + str(l+1)]

    def sigmoid(self, Z):
        """
        Implements the sigmoid activation in numpy\n

        Arguments:\n
            Z -- numpy array of any shape\n

        Returns:\n
            A -- output of sigmoid(z), same shape as Z\n
            cache -- returns Z as well, useful during backpropagation\n
        """
        A = 1/(1+np.exp(-Z))
        return A, Z

    def relu(self, Z):
        """
        Implements the RELU function.\n

        Arguments:\n
            Z -- Output of the linear layer, of any shape\n

        Returns:\n
            A -- Post-activation parameter, of the same shape as Z\n
            cache -- a python dictionary containing "A" ; stored for computing the backward pass efficiently
        """
        A = np.maximum(0,Z)
        return A, Z

    def relu_backward(self, dA, cache):
        """
        Implement the backward propagation for a single RELU unit.\n

        Arguments:\n
            dA -- post-activation gradient, of any shape\n
            cache -- 'Z' where we store for computing backward propagation efficiently\n

        Returns:\n
            dZ -- Gradient of the cost with respect to Z
        """
        Z = cache
        dZ = np.array(dA, copy=True)
        dZ[Z <= 0] = 0
        return dZ

    def sigmoid_backward(self, dA, cache):
        """
        Implement the backward propagation for a single SIGMOID unit.\n

        Arguments:\n
            dA -- post-activation gradient, of any shape\n
            cache -- 'Z' where we store for computing backward propagation efficiently\n

        Returns:\n
            dZ -- Gradient of the cost with respect to Z\n
        """
        Z = cache
        s = 1/(1+np.exp(-Z))
        dZ = dA * s * (1-s)
        return dZ
