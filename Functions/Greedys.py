import Functions.UtilityFunctions as uf
import Functions.HammingFunctions as hf

def Greedy(sequences,threshold):
    less_freq=[]
    metric=hf.min_Hamming_Distance(sequences,threshold)
    print("Less frequent characters: ",less_freq)
    answer=uf.constructSolution(sequences,metric)
    print(answer)
    print(uf.answer_Quality(sequences))