import os
from fileinput import filename
import random

def get_Input_From_File(number):
    
    current_path=os.getcwd()
    
    if(number<10):
        filename="100-300-00"+str(number)+".txt"
    elif(number==10):
        filename="100-300-010.txt"
    elif(number==69):
        filename="emo_ejemplo.txt"

    file_path=current_path+"/examples/"+str(filename)
    file=open(file_path,"r")
    sequences=[]
    
    for line in file:
        sequences.append(line)
    file.close()

    return sequences


def get_Hamming_Distance(sequence1, sequence2):
    cont=0
    for i in range(len(sequence1)):
        if sequence1[i]!=sequence2[i]:
            cont=cont+1
    return cont

def local_Search():
    no_Local=True
    while no_Local:
        if(True):
            return True
        else:
            no_Local=False
    return False

def GRASP(number_of_iterations):
    i=1
    for i in range (number_of_iterations):
        #build a greedy radoomized solution
        x= local_Search()
        if(i==1):
            best_x=x
        else:
            if(x<best_x):
                best_x=x
    return best_x

def less_freq_in_every_column(sequences,row,column):
    print("here")
    less_freq=[]
    for i in range(column-1):
        counter_A=0
        counter_C=0
        counter_G=0
        counter_T=0
        for j in range(row):
            if(sequences[j][i]=="A"):
                counter_A=counter_A+1
            elif(sequences[j][i]=="C"):
                counter_C=counter_C+1
            elif(sequences[j][i]=="G"):
                counter_G=counter_G+1
            elif(sequences[j][i]=="T"):
                counter_T=counter_T+1
        less_freq.append("column nr "+str(i)+": ")
        if(counter_A<=min(counter_A,counter_C,counter_G,counter_T)):
            less_freq.append("A")
        if(counter_C<=min(counter_A,counter_C,counter_G,counter_T)):
            less_freq.append("C")
        if(counter_G<=min(counter_A,counter_C,counter_G,counter_T)):
            less_freq.append("G")
        if(counter_T<=min(counter_A,counter_C,counter_G,counter_T)):
            less_freq.append("T")
        less_freq.append("|")
    return less_freq


def Greedy(sequence):
    threshold=createThreshold()
    #create a matrix of n sequences of m
    n=len(sequence)
    m=len(sequence[0])
    matrix=[]
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(sequence[i][j])
    #print the whole matrix
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print()
    #get the less frequent letter in each column
    less_freq=[]
    less_freq=less_freq_in_every_column(sequence,n, m)
    #print the less frequent letter in each column in the column their belong
    for i in range(len(less_freq)):
        print(less_freq[i], end=" ")
    print()

def createThreshold():
    #return a random float number between 0 and 1, with 3 decimals
    threshold=round(random.uniform(0, 1), 3)
    return threshold