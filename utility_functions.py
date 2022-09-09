from cgi import print_form
from itertools import count
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

def less_freq_in_every_column(sequences):
    answer=[]
    for i in range(len(sequences[0])-1):
        counter_A=0
        counter_C=0
        counter_G=0
        counter_T=0
        selective_charachter=[]
        for j in range(len(sequences)):
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
    less_freq=[]
    less_freq=less_freq_in_every_column(sequence)
    contrucSolution(sequence,less_freq,threshold)

def min_Hamming_Distance(len_sequences,threshold):
    value=int(threshold*len_sequences)
    return value

def contrucSolution(sequence,less_freq,threshold):
    metric=min_Hamming_Distance(len(sequence[0])-1,threshold)
    answer=[]
    for i in range(len(sequence[0])-1):
        if(len(answer)<metric):
            print("less than metric "+str(i))
            answer.append(check_less_freq(less_freq,i)) 
        else:
            print("more than metric "+str(i))
            answer.append(check_Metric(answer,sequence,metric,less_freq[i]))            
    print(answer)
        
    


def check_Metric(answer,sequence,metric,less_freq):
    selective_answer=[]
    
    value_A=get_metric_value(sequence,answer,metric,"A")
    answer.pop()
    value_C=get_metric_value(sequence,answer,metric,"C")
    answer.pop()
    value_G=get_metric_value(sequence,answer,metric,"G")
    answer.pop()
    value_T=get_metric_value(sequence,answer,metric,"T")
    answer.pop()
    
    if(value_A==max(value_A,value_C,value_G,value_T)):
        selective_answer.append("A")
    if(value_C==max(value_A,value_C,value_G,value_T)):
        selective_answer.append("C")
    if(value_G==max(value_A,value_C,value_G,value_T)):
        selective_answer.append("G")
    if(value_T==max(value_A,value_C,value_G,value_T)):
        selective_answer.append("T")
    return get_metric_answer(selective_answer,less_freq)


def get_metric_value(sequence,answer,metric,character):
    answer.append(character)
    counter=0
    for i in range(len(sequence)-1):
        hammin_distance=get_Hamming_Distance(answer,sequence[i])
        if(hammin_distance>=metric):
            counter=counter+1
    return counter

def get_metric_answer(selective_answer,less_freq):
    if(len(selective_answer)==1):
        return selective_answer[0]
    number_repeated=get_repeated(selective_answer,less_freq)
    print(number_repeated)
    if(number_repeated==0):
        return random.choice(selective_answer)
    if(number_repeated==1):
        return less_freq[0]
    elif(number_repeated>1):
        return random.choice(less_freq)


def get_repeated(selective_answer,less_freq):
    count=0
    print(less_freq)
    print(selective_answer)
    for i in range(len(selective_answer)):
        if(selective_answer[i] in less_freq):
            count=count+1
    return count    

def check_less_freq(less_freq,i):
    characters=less_freq[i]
    if(len(characters)==1):
        return characters[0]
    else:
        return random.choice(characters)