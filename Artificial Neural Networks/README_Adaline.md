Adaline is one of the simplest and earliest neural networks. It stands for "Adaptive Linear Neuron," first developed by Widrow and Hoff (see original publication for details and diagrams on the architecture):
Widrow, B., & Hoff, M. E. (1960). Adaptive switching circuits (No. TR-1553-1). STANFORD UNIV CA STANFORD ELECTRONICS LABS.

Adaline is a binary classifier with a linear decision boundary, meaning it can only classify two things at a time and can only solve linear problems. 

Adaline learns the best set of weight connections for a given input to approximate a desired target value. The dot product of the weight connections (w) and the inputs (x) are summed. This gives the output before being put through the step function (before a decision is made). This output is used to calculate both the error and the final output (the decision made by the Adaline).
To obtain the final response, the output is fed through the step function. The step function has a threshold at 0.5. If the value entered into the function is above this threshold, it will return 1. If it's below, the function will return 0. This is the final response, categorizing a specific input into one of the binary options.

We then want to determine how well the network has learned. To do this, we calculate the error by taking the difference between the output before the step function and the target values. Next, to improve learning, we update the weights based on this error, to shift the learned output closer to the desired target values: 

![Weight Update Function](https://github.com/Python-Club-UO/AUTOP/blob/master/Artificial%20Neural%20Networks/weightupdate.JPG)

Where w_old are the weight connections from the previous iteration and eta is the learning rate.
This process is repeated until a desired minimum error has been reached or a max number of iterations has been reached. 

A quick way to determine if your network has learned properly is to compare the targets with the generated outputs. 

Architecture:


![Adaline Architecture](https://github.com/Python-Club-UO/AUTOP/blob/master/Artificial%20Neural%20Networks/Adaline%20Architecture.png)

Step Function:



![step function](https://github.com/Python-Club-UO/AUTOP/blob/master/Artificial%20Neural%20Networks/Step%20Function.png)


-------

Adaline est l'un des plus simples et des plus anciens réseaux de neurones. Il est l'abréviation de "Adaptive Linear Neuron", développé à l'origine par Widrow et Hoff (voir la publication originale pour des détails et des schémas sur l'architecture):
Widrow, B., & Hoff, M. E. (1960). Adaptive switching circuits (No. TR-1553-1). STANFORD UNIV CA STANFORD ELECTRONICS LABS.

Adaline est un classificateur binaire avec une limite de décision linéaire, ce qui signifie qu'il ne peut classifier que deux choses à la fois et ne peut résoudre que des problèmes linéaires.

Adaline apprend le meilleur ensemble de connexions de poids pour une entrée donnée afin de se rapprocher d'une valeur cible souhaitée. Le produit scalaire des connexions de poids (w) et des entrées (x) est additionné. Cela donne la sortie avant de passer par la fonction d'étape (avant qu'une décision ne soit prise). Cette sortie est utilisée pour calculer à la fois l'erreur et la sortie finale (la décision prise par l'Adaline). Pour obtenir la réponse finale, la sortie est alimentée par la fonction d'étape. La fonction d'étape a un seuil de 0,5. Si la valeur entrée dans la fonction est supérieure à ce seuil, elle renvoie 1. Si elle est inférieure à 0,5, la fonction retournera 0. Ça c'est la réponse finale, qui catégorise une entrée spécifique dans l'une des options binaires.

Nous voulons ensuite déterminer dans quelle mesure le réseau a bien appris. Pour ce faire, nous calculons l'erreur en prenant la différence entre la sortie avant la fonction d'étape et les valeurs cibles. Ensuite, pour améliorer l'apprentissage, nous mettons à jour les poids en fonction de cette erreur, afin de rapprocher la sortie apprise des valeurs cibles souhaitées : 

![Weight Update Function](https://github.com/Python-Club-UO/AUTOP/blob/master/Artificial%20Neural%20Networks/weightupdate.JPG)


Où w_old sont les connexions de poids de l'itération précédente et eta est le taux d'apprentissage. Ce processus est répété jusqu'à ce qu'une erreur minimale souhaitée ait été atteinte ou qu'un nombre maximal d'itérations ait été atteint.

Un moyen rapide de déterminer si votre réseau a correctement appris est de comparer les cibles avec les sorties générées.

Architecture:


![Adaline Architecture](https://github.com/Python-Club-UO/AUTOP/blob/master/Artificial%20Neural%20Networks/Adaline%20Architecture.png)

Fonction d'étape:



![step function](https://github.com/Python-Club-UO/AUTOP/blob/master/Artificial%20Neural%20Networks/Step%20Function.png)
