import numpy as np
import pandas as pd
data = pd.read_csv("candidate.csv")
data1=np.array(data)
print("dataset",data1)
concepts=np.array(data.iloc[:,0:-1])
'''print(concepts)
[['japan' 'honda' 'blue' 1980 'economy']
 ['japan' 'toyota' 'green' 1970 'sports']
 ['japan' 'toyota' 'blue' 1940 'economy']
 ['japan' 'chrysler' 'red' 1980 'economy']
 ['japan' 'honda' 'white' 1980 'economy']]'''
target=np.array(data.iloc[:,-1])
'''print(target)
['yes' 'no' 'yes' 'no' 'yes']'''
def learn(concepts,target):
    specific_h=concepts[0].copy()
    print("Initializationa of specific_h and general_h")
    print(specific_h)
    general_h=[["?" for i in range(len(specific_h))]for i in range(len(specific_h))]
##general_h is a list of lists
    print(general_h)
    for i,h in enumerate(concepts):
        print("i=",i,"h=",h)
        if target[i]=='yes':
            for a in range(len(specific_h)):
                if(h[a]!=specific_h[a]):
                    specific_h[a]='?'
                    general_h[a][a]='?'
        if target[i]=='no':
            for a in range(len(specific_h)):
                if(h[a]!=specific_h[a]):
                    general_h[a][a]=specific_h[a]
                else:
                    general_h[a][a]='?'
        print("Steps in CEM",i+1)
        print(specific_h)
        print(general_h)
    return specific_h,general_h
s_final,g_final=learn(concepts,target)
print("final specific_h",s_final,sep="\n")
print("final general_h",g_final,sep="\n")
