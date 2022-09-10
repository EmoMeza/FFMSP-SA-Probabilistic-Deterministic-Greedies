import random
import Functions.FrequentFunctions as ff
import Functions.HammingFunctions as hf

def constructSolution(sequences,less_freq,threshold):
    answer=[]
    metric=hf.min_Hamming_Distance(sequences,threshold)
    for i in range(sequences[0].get_Length()-1):
        if(len(answer)<metric):
            answer.append(ff.get_less_frequent(less_freq,i)) 
        else:
            answer.append(get_character_for_answer(answer,sequences,metric,less_freq[i]))            
    print(answer)

def get_character_for_answer(answer,sequences,metric,less_freq):
    selective_answer=[]
    
    value_A=get_metric_value(sequences,answer,metric,"A")
    answer.pop()
    value_C=get_metric_value(sequences,answer,metric,"C")
    answer.pop()
    value_G=get_metric_value(sequences,answer,metric,"G")
    answer.pop()
    value_T=get_metric_value(sequences,answer,metric,"T")
    answer.pop()
    
    if(value_A==max(value_A,value_C,value_G,value_T)):
        selective_answer.append("A")
    if(value_C==max(value_A,value_C,value_G,value_T)):
        selective_answer.append("C")
    if(value_G==max(value_A,value_C,value_G,value_T)):
        selective_answer.append("G")
    if(value_T==max(value_A,value_C,value_G,value_T)):
        selective_answer.append("T")
    return get_character(selective_answer,less_freq)

def get_metric_value(sequences,answer,metric,character):
    answer.append(character)
    counter=0
    for i in range(len(sequences)):
        hammin_distance=hf.get_Hamming_Distance(answer,sequences[i].get_String())
        if(hammin_distance>=metric):
            counter=counter+1
    return counter

def get_character(selective_answer,less_freq):
    if(len(selective_answer)==1):
        return selective_answer[0]
    number_repeated=get_repeated(selective_answer,less_freq)
    if(number_repeated==0):
        return random.choice(selective_answer)
    if(number_repeated==1):
        return less_freq[0]
    elif(number_repeated>1):
        return random.choice(less_freq)

def get_repeated(selective_answer,less_freq):
    count=0
    for i in range(len(selective_answer)):
        if(selective_answer[i] in less_freq):
            count=count+1
    return count