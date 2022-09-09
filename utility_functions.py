import os
from fileinput import filename
from select import select
from turtle import position
import numpy as np
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



def less_freq_in_every_column(sequences,row,column):
    answer=[]
    for i in range(column-1):
        counter_A=0
        counter_C=0
        counter_G=0
        counter_T=0
        selective_charachter=[]
        for j in range(row):
            if(sequences[j][i]=="A"):
                counter_A=counter_A+1
            elif(sequences[j][i]=="C"):
                counter_C=counter_C+1
            elif(sequences[j][i]=="G"):
                counter_G=counter_G+1
            elif(sequences[j][i]=="T"):
                counter_T=counter_T+1
        if(counter_A==min(counter_A,counter_C,counter_G,counter_T)):
            selective_charachter.append("A")
        if(counter_C==min(counter_A,counter_C,counter_G,counter_T)):
            selective_charachter.append("C")
        if(counter_G==min(counter_A,counter_C,counter_G,counter_T)):
            selective_charachter.append("G")
        if(counter_T==min(counter_A,counter_C,counter_G,counter_T)):
            selective_charachter.append("T")
        answer.append(selective_charachter)
    return answer


def Greedy(sequence,threshold):
    n=len(sequence)
    m=len(sequence[0])
    less_freq=[]
    less_freq=less_freq_in_every_column(sequence,n, m)
    contrucSolution(sequence,n,less_freq,threshold)

def min_Hamming_Distance(len_sequences,threshold):
    value=int(threshold*len_sequences)
    return value

def contrucSolution(sequence,len_sequences,less_freq,threshold):
    metric=min_Hamming_Distance(len_sequences,threshold)
    answer=[]
    for i in range(len(sequence[0])):
        if(len(answer)<=metric):
            answer.append(check_less_freq(less_freq,i)) 
        else:
            answer.append(check_Metric(answer,sequence,metric))            
    print(answer)
        
    
def check_less_freq(less_freq,i):
    characters=less_freq[i]
    if(len(characters)==1):
        return characters[0]
    else:
        return random.choice(characters)

def check_Metric(answer,sequence,metric):
    copy_answer=answer
    value_A=check_sequence(sequence,copy_answer,metric,"A")
    #remove the last element of the list copy_answer
    copy_answer.pop()
    value_C=check_sequence(sequence,copy_answer,metric,"C")
    copy_answer.pop()
    value_G=check_sequence(sequence,copy_answer,metric,"G")
    copy_answer.pop()
    value_T=check_sequence(sequence,copy_answer,metric,"T")
    #print(value_A,value_C,value_G,value_T)
    return True

def check_sequence(sequence,answer,metric,character):
    answer.append(character)
    counter=0
    for i in range(len(answer)):
        hammin_distance=get_Hamming_Distance(answer,sequence[i])
        if(hammin_distance>=metric):
            counter=counter+1
    return counter