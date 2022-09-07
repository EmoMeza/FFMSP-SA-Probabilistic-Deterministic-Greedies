
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
    #check the 1s and 0s in the same position, if they are different, create a new sequence with 1s in the different positions and 0s in the same positions
    #return the new sequence
    #print(sequence1, sequence2)
    new_sequence=""
    for i in range(len(sequence1)):
        if sequence1[i]==sequence2[i]:
            new_sequence+="0"
        else:
            new_sequence+="1"
    return new_sequence
    