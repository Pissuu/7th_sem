import csv
import numpy as np
import pandas as pd
import math
file=pd.read_csv("id3_self.csv")
attribute_names=[]
attribute_names=list(file)#creates list with all header names
del(attribute_names[-1])#removes play_tennis as an attribute_name
class attribute:
    def __init__(self):
        self.name=""
objs = [attribute() for i in attribute_names]
##print(attribute_names)
j=0
for i in attribute_names:
    objs[j].name=i
##    print(objs[j].name)
    j=j+1
""" created a class called attributes with yes
and no as the instance attributes;
a list of objects have been created,
the objects can be accessed by iterating the list"""
attributes=[]
attributes_dic={}
##print((len(file.columns)-1))
for i in range(len(file.columns)-1):
    for j in file[objs[i].name]:
        if j not in attributes:
            attributes.append(j)
    attributes_dic[objs[i].name]=attributes
    attributes=[]
##a dictionary called attributes_dic is created and looks as documented below
"""{'outlook': ['sunny', 'overcast', 'rain'], 'temperature': ['hot', 'mild', 'cool'],
'humidity': ['high', 'normal'], 'wind': ['weak', 'strong']}"""
##print(file.iloc[1][1])
yes_dic={}
no_dic={}
yes=0
no=0
##creating variables no and yes that are class yes and no
##print(file.iloc[0][4])
##print(len(file.index))
for key,values in attributes_dic.items():
    for i in values:
        no_dic[i]=0
        yes_dic[i]=0
for i in range(len(file.index)):
    for j in range(len(file.index)-2):
        if file.iloc[i][4]=="yes":
            yes_dic[file.iloc[i][j]]+=1
        else:
            no_dic[file.iloc[i][j]]+=1
"""creates dictionary called yes_dic of occurance of number of yes for each value:
{'sunny': 0, 'hot': 1, 'high': 2, 'weak': 3, 'strong': 0,
'overcast': 1, 'rain': 2, 'mild': 1, 'cool': 1, 'normal': 1}"""
##print(yes_dic)
for i in range(len(file.index)):
    if file.iloc[i][4]=="yes":
        yes+=1
    if file.iloc[i][4]=="no":
        no+=1
class_entropy=0
class_entropy=-(yes/(yes+no))*math.log((yes/(yes+no)),2)-(no/(yes+no))*math.log((no/(yes+no)),2)
temp_yes=0
temp_no=0
i_dic={}
I=0
##print(no_dic)
"""creating another dictionary to store the Information values of the attributes in a list form"""
for key,value in attributes_dic.items():
    for i in value:
        temp_yes=yes_dic[i]
        temp_no=no_dic[i]
        if temp_no==0 or temp_yes==0:
            I=0
        else:
            I=-(temp_yes/(temp_yes+temp_no))*math.log((temp_yes/(temp_yes+temp_no)),2)-(temp_no/(temp_yes+temp_no))*math.log((temp_no/(temp_yes+temp_no)),2)
        i_dic[i]=I
"""print(i_dic)
{'sunny': 0, 'overcast': 0, 'rain': 0, 'hot': 0.8112781244591328, 'mild': 0,
'cool': 0, 'high': 0.9709505944546686, 'normal': 0, 'weak': 0.8112781244591328, 'strong': 0}"""
entropy_dic={}
for key,value in attributes_dic.items():
    temp_value=0
    for i in value:
        temp_yes=yes_dic[i]
        temp_no=no_dic[i]
        temp_i=i_dic[i]
        temp_value=temp_value+(((temp_yes+temp_no)/(yes+no))*temp_i)
        entropy_dic[key]=temp_value
"""print(entropy_dic)
{'outlook': 0.0, 'temperature': 0.5408520829727552, 'humidity': 0.8091254953788906, 'wind': 0.5408520829727552}"""
gain_dic={}
for i in attribute_names:
    gain_dic[i]=class_entropy-entropy_dic[i]
"""print(gain_dic)
{'outlook': 1.0, 'temperature': 0.4591479170272448, 'humidity': 0.19087450462110944, 'wind': 0.4591479170272448}"""
max_val=0
max_key=""
for key,value in gain_dic.items():
    if value>max_val:
        max_key=key
        max_val=value
print(max_key,":")
attribute_val=attributes_dic['outlook']
for i in attribute_val:
    if yes_dic[i]==0:
        print(i,"-no")
    if no_dic[i]==0:
        print(i,"-yes")
    if no_dic[i]!=0 and yes_dic[i]!=0:
        print(i,"-?")
    

    
            
            


