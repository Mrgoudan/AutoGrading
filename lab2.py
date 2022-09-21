import sys
import os
import csv
import subprocess as sub
from tabnanny import check
import time
names = []
with open('repoName.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        names.append(row[0])
with open("correct.txt","r") as f:
    correct = f.read()

print(names)
path  = os.getcwd()+"/student"
print(path)
makeerror=[]
fullmark = []
for name in names:
    clone = "git clone git@github.umn.edu:umn-csci-3081-F22/"+name+"-lab02.git" 

    os.chdir(path) # Specifying the path where the cloned project needs to be copied
    os.system(clone) # Cloning
    try:
        sub.check_call(["make"], cwd=os.getcwd()+"/"+name+"-lab02")
    except:
        makeerror.append(name)
    
for name in names:
    time.sleep(2)
    try:
        print("trying")
        out = sub.check_output(["./run"],cwd=os.getcwd()+"/"+name+"-lab02")
        print(out)

    except:
        pass
print(fullmark)
    



