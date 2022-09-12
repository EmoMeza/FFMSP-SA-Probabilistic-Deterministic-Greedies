import Resources.Functions.UtilityFunctions as uf
import Resources.Functions.HammingFunctions as hf

def Probabilistic_Greedy(sequences,threshold):
    metric=hf.min_Hamming_Distance(sequences,threshold)
    answer=uf.build_PG_Solution(sequences,metric)
    print(answer)
    print(uf.answer_Quality(sequences,answer,metric))

def Deterministic_Greedy(sequences,threshold):
    metric=hf.min_Hamming_Distance(sequences,threshold)
    answer=uf.build_DG_Solution(sequences,metric)
    print(answer)
    print(uf.answer_Quality(sequences,answer,metric))