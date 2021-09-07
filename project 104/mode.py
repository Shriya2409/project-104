import csv
from collections import Counter

with open('height_weight.csv', newline='')as f:
    reader=csv.reader(f)
    fileData=list(reader)

fileData.pop(0)
newData=[]

for i in range(len(fileData)):
    n=fileData[i][2]
    newData.append(float(n))   

l=len(newData)
newData.sort()
data=Counter(newData)
mode_range={"90-110": 0, "110-130": 0, "130-150": 0}
for height, occurence in data.items():
    if 50<float(height)<60:
       mode_range["90-110"]+=occurence
    elif 60<float(height)<70:
        mode_range["110-130"]+=occurence
    elif 70<float(height)<80:
        mode_range["130-150"]+=occurence   
range2=0        
mode_occurence=0
for range, mode_occurence in mode_range.items():
    if occurence>mode_occurence:
        range2, mode_occurence=[int(range.split("-")[0]), int(range.split("-")[1])],occurence
mode=float((range2[0]+range2[1])/2)        
print(mode)