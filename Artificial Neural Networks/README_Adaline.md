Adaline is one of the simplest and earliest neural networks. It stands for "Adaptive Linear Neuron," first developed by Widrow and Hoff (see original publication for details and diagrams on the architecture):
Widrow, B., & Hoff, M. E. (1960). Adaptive switching circuits (No. TR-1553-1). STANFORD UNIV CA STANFORD ELECTRONICS LABS.

Adaline is a binary classifier with a linear decision boundary, meaning it can only classify two things at a time and can only solve linear problems. 

Adaline learns the best set of weight connections for a given input to approximate a desired target value. The dot product of the weight connections (w) and the inputs (x) are summed. This gives the output before being put through the step function (before a decision is made). This output is used to calculate both the error and the final output (the decision made by the Adaline).
To obtain the final response, the output is fed through the step function. The step function has a threshold at 0.5. If the value entered into the function is above this threshold, it will return 1. If it's below, the function will return 0. This is the final response, categorizing a specific input into one of the binary options.

We then want to determine how well the network has learned. To do this, we calculate the error by taking the difference between the output before the step function and the target values. Next, to improve learning, we update the weights based on this error, to shift the learned output closer to the desired target values: 
w_new = w_old + eta * (error . x^T)
Where w_old are the weight connections from the previous iteration and eta is the learning rate.
This process is repeated until a desired minimum error has been reached or a max number of iterations has been reached. 

A quick way to determine if your network has learned properly is to compare the targets with the generated outputs. 

Architecture:
![Adaline Architecture](https://github.com/Python-Club-UO/AUTOP/blob/master/Artificial%20Neural%20Networks/Adaline%20Architecture.png)

Step Function:
![step function](https://github.com/Python-Club-UO/AUTOP/blob/master/Artificial%20Neural%20Networks/Step%20Function.png)


-------

French
