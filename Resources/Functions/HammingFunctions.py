def get_Hamming_Distance(sequence1, sequence2, metric):
    cont=0
    for i in range(len(sequence1)):
        if(sequence2.get_metric_Satisfied()==True):
            return metric
        if(cont>=metric):
            sequence2.change_metric_Satisfied(True)
            return metric
        if sequence1[i]!=sequence2.get_Character(i):
            cont=cont+1
    return cont

def min_Hamming_Distance(sequence,threshold):
    value=int(float(threshold)*float((sequence[0].get_Length()-1)))
    return value