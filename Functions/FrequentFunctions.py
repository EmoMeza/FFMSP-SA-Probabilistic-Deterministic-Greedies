import random

def create_less_frequent_until_metric(sequences,metric):
    answer=[]
    for i in range(metric):
        counter_A=0
        counter_C=0
        counter_G=0
        counter_T=0
        selective_charachter=[]
        for j in range(len(sequences)):
            if(sequences[j].get_Character(i)=="A"):
                counter_A=counter_A+1
            elif(sequences[j].get_Character(i)=="C"):
                counter_C=counter_C+1
            elif(sequences[j].get_Character(i)=="G"):
                counter_G=counter_G+1
            elif(sequences[j].get_Character(i)=="T"):
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

def create_less_frequent_in_column(sequences,index):
    answer=[]
    counter_A=0
    counter_C=0
    counter_G=0
    counter_T=0
    selective_charachter=[]
    for j in range(len(sequences)):
        if(sequences[j].get_Character(index)=="A"):
            counter_A=counter_A+1
        elif(sequences[j].get_Character(index)=="C"):
            counter_C=counter_C+1
        elif(sequences[j].get_Character(index)=="G"):
            counter_G=counter_G+1
        elif(sequences[j].get_Character(index)=="T"):
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

def get_less_frequent(sequences,i):
    characters=create_less_frequent_in_column(sequences,i)
    if(len(characters)==1):
        return characters[0][0]
    else:
        return random.choice(characters[0])

