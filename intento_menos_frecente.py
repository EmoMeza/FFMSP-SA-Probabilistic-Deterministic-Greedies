
def less_freq_in_every_column(sequences,row,column):
    print("here")
    less_freq_matrix=[]
    for i in range(4):
        less_freq_matrix.append([])
        for j in range(column):
            less_freq_matrix[i].append(0)
    for i in range(column):
        counter_A=0
        counter_C=0
        counter_G=0
        counter_T=0
        counter_place=0
        for j in range(row):
            if(sequences[j][i]=="A"):
                counter_A=counter_A+1
            elif(sequences[j][i]=="C"):
                counter_C=counter_C+1
            elif(sequences[j][i]=="G"):
                counter_G=counter_G+1
            elif(sequences[j][i]=="T"):
                counter_T=counter_T+1
        if(counter_A<=min(counter_A,counter_C,counter_G,counter_T)):
            less_freq_matrix[i][counter_place].append("A")
            counter_place=counter_place+1
        if(counter_C<=min(counter_A,counter_C,counter_G,counter_T)):
            less_freq_matrix[i][counter_place].append("C")
            counter_place=counter_place+1
        if(counter_G<=min(counter_A,counter_C,counter_G,counter_T)):
            less_freq_matrix[i][counter_place].append("G")
            counter_place=counter_place+1
        if(counter_T<=min(counter_A,counter_C,counter_G,counter_T)):
            less_freq_matrix[i][counter_place].append("T")
            counter_place=counter_place+1
    return less_freq_matrix