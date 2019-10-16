import csv
lines=csv.reader(open('babu.csv'))
dataset=list(lines)
data_len=len(dataset)
##print(data_len)
attribute_len=len(dataset[1])-1
yes_dic=[]
for i in range(data_len):
    yes_dic.append(dataset[i][attribute_len])
general=[['?'for i in range(attribute_len)]for i in range(attribute_len)]
specific=['0'for i in range(attribute_len)]
for i in range(attribute_len):
    if yes_dic[i]=="yes":
        for j in range(data_len):
            if specific[j]=='0':
                specific[j]=dataset[i][j]
            if specific[j]!=dataset[i][j]:
                specific[j]='?'
                general[j][j]='?'
    if yes_dic[i]=="no":
        for j in range(data_len):
##            if specific[j]==dataset[i][j]:
##                general[j][j]='?'
            if specific[j]!=dataset[i][j] and specific[j]!='?':
                general[j][j]=specific[j]
        
            
    print(i+1,"iteration")
    print(specific)
    print(general)
    print("     ")

print("final answers")
print(specific)
print(general)
