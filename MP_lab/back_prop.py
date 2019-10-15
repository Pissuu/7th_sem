import numpy as np
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)
X = X/np.amax(X,axis=0) ##divides by largest number in respective column
print(X)
y = y/100 ##output is supposed to be a small number
print("y :",y)
def sigmoid (x):
    return 1/(1 + np.exp(-x))
def derivatives_sigmoid(x):
    return x * (1 - x)
epoch=70000
lr=0.6
inputlayer_neurons = 2 
hiddenlayer_neurons = 3 
output_neurons = 1 
wh=np.array([[0.7872,0.4873,0.4041],[0.9057,0.8723,0.9704]])
bh=np.array([[0.0751,0.3708,0.9870]])
wout=np.array([[0.6119],[0.0234],[0.9764]])
bout=np.array([[0.8051]])
for i in range(epoch):
    hinp1=np.dot(X,wh)
    hinp=hinp1 + bh
    hlayer_act = sigmoid(hinp)
    outinp1=np.dot(hlayer_act,wout)
    outinp= outinp1+ bout
    output = sigmoid(outinp)
    EO = y-output
    outgrad = derivatives_sigmoid(output)
    d_output = EO* outgrad    
    EH = d_output.dot(wout.T) 
    hiddengrad = derivatives_sigmoid(hlayer_act)
    d_hiddenlayer = EH * hiddengrad  
    wout += hlayer_act.T.dot(d_output) *lr
    wh += X.T.dot(d_hiddenlayer) *lr
print("Input: \n" + str(X))
print("Actual Output: \n" + str(y))
print("Predicted Output: \n" ,output)
