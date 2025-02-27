import os
import sys
import shutil
from PIL import Image


all=os.listdir()
newall=all.copy()
for file in all:
    if file[-4:]!=".bmp":
        newall.remove(file)




def number4to5p(picturestr,n=1):
    
    i=0
    n=n-1
    for i in newall:
        if i[-4-len(picturestr):-4].isnumeric():
            n+=1
        shutil.move(i,str(n))
def number4to5(picturestr,n=1):
    
    i=0
    n=n-1
    for i in newall:
        if i[-4-len(picturestr):-4]==picturestr:
            n+=1
        shutil.move(i,str(n))

def numbertolast(start,name):
    n=0
    i=0
    for i in newall:
        if i[start:start+len(name)]==name:
            n+=1
        shutil.move(i,str(n))

def nextsame(range1,range2,n=1):
    
    i=0
    for i in range(0,len(newall)-1):
        if newall[i][range1:range2]==newall[i+1][range1:range2]:
            shutil.move(newall[i],str(n))
        else:
            shutil.move(newall[i],str(n))
            n+=1
    shutil.move(newall[len(newall)-1],str(n))

def check(a,b):
        n=0
        i=0
        for i in newall:
            print(i[a:b])


def trash(a,b,c):
    n=0
    i=0
    for i in newall:
        if i[a:b]==c:
            shutil.move(i,"new")
def throw(a,b,c):
    
    i=0
    if c=="num":
        for i in newall:
            if i[a:b].isnumeric():
                shutil.move(i,"new")
    else:
        for i in newall:
            if type(i[a:b])==str:
                shutil.move(i,"new")    
def trash3(a):
    
    n=0
    i=0
    
    for i in newall:
        h=Image.open(i)
        if h.width !=a:
            h.close()
            shutil.move(i,"new")

def trash4(c):
    n=0
    i=0
    for i in newall:
        if len(i)>=c:
            shutil.move(i,"no")
            
def cut():
    n=0
    i=0
    for i in newall:
        img = Image.open(i)
        new_img = img.crop((0, 0, 1280, 720))
        new_img.save("no\\"+i)


  


   

         


   
