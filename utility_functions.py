import random
from typing import Counter

def get_Inputs():
    #get a set of n sequenses of m over a alphabet of k
    #k_alfabet are 4 letters, A, C, G, T
    #get sequences
    n=int(input("How many sequences\n"))
    m=int(input("How long is the sequence\n"))
    #get sequences
    sequences=[]
    for i in range(n):
        sequences.append(input("Enter sequence\n"))
    #get a threshold for the similarity
    threshold=float(input("Enter threshold:\n"))
    return sequences, threshold

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
    for i in range(column):
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


def GRASP2(sequence, threshold):
    #return a random float number between 0 and 1, with 3 decimals
    alpha=round(random.uniform(0, 1), 3)
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

