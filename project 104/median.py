import csv
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
if l % 2==0:
    median1=float(newData[l//2])
    median2=float(newData[l//2-1])
    median=(median1+median2)/2
else:
    median=float(newData[l//2])
print(median)    