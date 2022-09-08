import utility_functions as uf

def main():
    #sequence, threshold=uf.get_Inputs()
    sequence=["ACGT","CCCC","GTAC","GTCC"]
    threshold=4
    uf.GRASP2(sequence, threshold)

    # sequences=["0101", "0111", "0011", "1100","1000"]
    
    # print(sequences[0], sequences[1], sequences[2])

    # print("s= "+ str(sequences[3]))

    # answer=uf.get_Hamming_Distance(sequences[3],sequences[0])
    # if(answer>=3):
    #     print("s1= "+str(answer))

    # answer=uf.get_Hamming_Distance(sequences[3],sequences[1])
    # if(answer>=3):
    #     print("s2= "+str(answer))
    
    # answer=uf.get_Hamming_Distance(sequences[3],sequences[2])
    # if(answer>=3):
    #     print("s3= "+str(answer))

    # print("s= "+ str(sequences[4]))

    # answer=uf.get_Hamming_Distance(sequences[4],sequences[0])
    # if(answer>=3):
    #     print("s1= "+str(answer))
    
    # answer=uf.get_Hamming_Distance(sequences[4],sequences[1])
    # if(answer>=3):
    #     print("s2= "+str(answer))
    
    # answer=uf.get_Hamming_Distance(sequences[4],sequences[2])
    # if(answer>=3):
    #     print("s3= "+str(answer))
    

if __name__ == '__main__':
    main()