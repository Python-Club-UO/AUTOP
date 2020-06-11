# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:59:00 2020

@author: Matt & Kinsey
"""
#%% Libraries
import numpy as np
import matplotlib.pyplot as plt
#%% Step function 
def step(x):                                                                    # x (value) that is put into step function returns -1 if x<0, 1 if x>0, and else x=0, return 0
    if x<0:
        return -1
    elif x>0:
        return 1
    else:
        return x
#%% Learning function         
def learn(inputs,targets,nbPairs,dimIn,dimTar,eta,nbOfEpochs):                  # learning function (training the neural net)
    w=(np.random.random_sample((dimTar,dimIn))*2-1)*0.1                         # generate random weights by the specified dimensions(between -0.1,0.1) --> Forms the weight matrix
    mse=[]                                                                      # create an empty MSE list (for storing errors later)
    for j in range(0,nbOfEpochs):                                               # start of training from 0 to the specified number of epochs
        errList=np.zeros(nbPairs)                                               # initialisation of errList for one epoch
        randList = np.arange(len(inputs))                                       # create a list of the inputs
        np.random.shuffle(randList)                                             # random sample of the List
        for i in range(0,nbPairs):                                              # for each input/target pair
            choice=randList[i]                                                  # selection a pair from the random ordered list
            x=np.reshape(inputs[choice,:],(dimIn,1))                            # selection of a given input -> reshape in matrix
            t=np.reshape(targets[choice,:],(dimTar,1))                          # corresponding target -> reshape in matrix              
            a=np.dot(w,x)                                                       # computation of the activation
            e=t-a                                                               # computation of the error (target - actual)
            w = w + eta * (np.dot(e,np.transpose(x)))                           # update the weights matrix
            errList[i]=np.dot(np.transpose(e),e)                                # calculate the quadratic error  (squared error) for each pair        
        mse.append(np.mean(errList))                                            # save the mean squared error to the MSE list 
    return (w,mse)                                                              # function returns the weights matrix and MSE are returned
#%% Recall function   
def recall(inputs,targets,nbPairs,dimIn,w,step):                                # recall function (for testing how well the network learned)
    obtained=[]                                                                 # create an empty list to store all obtained values (answers)
    for i in range(0, nbPairs):                                                 # for each pair
        x=np.reshape(inputs[i,:],(dimIn,1))                                     # selection of a given input -> reshape in matrix
        a=np.dot(w,x)                                                           # computation of the activation
        y=step(a)                                                               # apply the activationg (step) function to obtain the output
        obtained.append(y)                                                      # save the obtained value (answer) to list 
    return (obtained)                                                           # return the list of obtained values
#%% Initialization      
inputs=np.array([[1, 1, 1],[1, 1, -1],[1, -1, 1],[1, -1, -1]])                  # set input array
targets=np.array([[1],[-1],[-1],[-1]])                                          # set desired targets array
eta=0.01                                                                        # learning parameter
nbOfEpochs=200                                                                  # total number of learning epochs
(nbPairs,dimIn)=np.shape(inputs)                                                # get the number of pairs to learn and dimension of the Inputs
dimTar=len(targets[1,:])                                                        # dimension of the Targets
#%% simulation 
(w,mse)=learn(inputs,targets,nbPairs,dimIn,dimTar,eta,nbOfEpochs)               # execution of learning function
#%% Plotting   
plt.figure()                                                                    # create new figure
plt.xlabel('number of Epochs')                                                  # set the x axis label
plt.ylabel('MSE')                                                               # set the y axis label
plt.plot(mse)                                                                   # plot the mean squared error across time (epochs)
plt.show()                                                                      # display the figure
#%% recall 
obtained=recall(inputs,targets,nbPairs,dimIn,w,step)                            # execution of recall
targets=targets.tolist()                                                        # convert targets array to a list (just for making printing little easier, NOT NEEDED)
print (f'Inputs \n{inputs}')                                                    # print the inputs
print (f'Targets \n{targets}')                                                  # print the targets
print (f'Obtained \n{obtained}')                                                # print the obtained (answers)
##### Compare the targets to the obtained (learned answers), did the network succeed? ######
