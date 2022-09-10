def get_Hamming_Distance(sequence1, sequence2):
    cont=0
    for i in range(len(sequence1)):
        if sequence1[i]!=sequence2[i]:
            cont=cont+1
    return cont

def min_Hamming_Distance(sequence,threshold):
    value=int(float(threshold)*float((sequence[0].get_Length()-1)))
    return value