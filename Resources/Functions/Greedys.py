import Resources.Functions.UtilityFunctions as uf
import Resources.Functions.HammingFunctions as hf

def Greedy(sequences,threshold):
    metric=hf.min_Hamming_Distance(sequences,threshold)
    answer=uf.constructSolution(sequences,metric)
    print(answer)
    print(uf.answer_Quality(sequences))

def Greedy2(sequences,threshold):
    metric=hf.min_Hamming_Distance(sequences,threshold)
    answer=uf.constructSolution2(sequences,metric)
    print(answer)
    print(uf.answer_Quality(sequences))