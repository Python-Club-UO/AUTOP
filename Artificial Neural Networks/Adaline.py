import numpy as np


#Step function use for recall
def step(x):
    if x<0:
        return -1
    else:
        if x>0:
            return 1
        else:
            return x
            
#%% Learning 
def learn(inputs,targets,eta,nbOfEpochs):
    (nbPairs,dimIn)=np.shape(inputs) #number of pairs to learn and dimension of the Inputs
    dimOut=len(targets[1,:]) #dimension of the Outputs
    w=(np.random.random_sample((dimOut,dimIn))*2-1)*0.1 #random weight (-0.1,0.1)
    #w=np.zeros((dimOut,dimIn))
    mse=np.zeros(nbOfEpochs) #initialization of MSE list
    #computation
    for j in range(0,nbOfEpochs): #computation of epochs
    
        errList=np.zeros(nbPairs)  #initialisation of errList for one epoch
        randList = np.arange(len(inputs)) 
        np.random.shuffle(randList) #random sample of randList
        
        for i in range(0,nbPairs):
        
            choice=randList[i] #selection of a pairs
            x=np.reshape(inputs[choice,:],(dimIn,1)) #selection of a given input -> reshape in matrix
            t=np.reshape(targets[choice,:],(dimOut,1)) # corresponding target -> reshape in matrix              
            a=np.dot(w,x) #computation of the activation
            e=t-a #computation of the error
            w = w + eta * (np.dot(e,np.transpose(x))) #weights update
            errList[i]=np.dot(np.transpose(e),e) # quadratic error  [0,0]           
        mse[j]=np.mean(errList) #MSE error

    return (w,mse) #weights and MSE are returned
 
#%% Recall   
def recall(inputs,targets,w,outFunc): # fucntion (ex. step) can be passed like argument

    (nbPairs,dimIn)=np.shape(inputs)

    for i in range(0, nbPairs):
        x=np.reshape(inputs[i,:],(dimIn,1))
        a=np.dot(w,x) #computation of the activation
        y=outFunc(a) 
        print (repr(np.ravel(x).tolist()).rjust(2), repr(np.ravel(y).tolist()).rjust(3))
        
        

import matplotlib.pyplot as plt


#application of the step function as the output function
outFunc=np.vectorize(Adaline.step)


#Task; can be modified
inputs=np.array([[1, 1, 1],[1, 1, -1],[1, -1, 1],[1, -1, -1]])
targets=np.array([[1],[-1],[-1],[-1]])

#initialisation
eta=0.01 #learning parameter
nbOfEpochs=200    

#simulation 
(w,mse)=Adaline.learn(inputs,targets,eta,nbOfEpochs)    
    
        
#fig = plt.figure(figsize=(15, 8))
plt.figure()
plt.xlabel('number of Epochs')
plt.ylabel('MSE')
plt.plot(mse)
plt.show()

#recall
Adaline.recall(inputs,targets,w,outFunc)




#Run Main.py before testing noisy recall

#initialization
(nbPairs,dimIn)=np.shape(inputs)
dimOut=len(targets[1,:])

#generate a noisy input
x=np.array([[-1],[1],[-1]])

#compute activation and output
a=np.dot(w,x)
y=outFunc(a)

print
print ('Network output = ',repr(np.ravel(y).tolist()).rjust(2))
