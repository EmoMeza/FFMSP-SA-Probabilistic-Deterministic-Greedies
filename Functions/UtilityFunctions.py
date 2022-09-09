import random
import Functions.FrequentFunctions as ff
import Functions.HammingFunctions as hf

def constructSolution(sequence,less_freq,threshold):
    answer=[]
    metric=hf.min_Hamming_Distance(sequence,threshold)
    for i in range(len(sequence[0])-1):
        if(len(answer)<metric):
            print("less than metric "+str(i))
            answer.append(ff.get_less_frequent(less_freq,i)) 
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
        hammin_distance=hf.get_Hamming_Distance(answer,sequence[i])
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