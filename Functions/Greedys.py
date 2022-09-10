import Functions.FrequentFunctions as ff
import Functions.UtilityFunctions as uf
import Functions.HammingFunctions as hf

def Greedy(sequences,threshold):
    less_freq=[]
    metric=hf.min_Hamming_Distance(sequences,threshold)
    less_freq=ff.create_less_frequent(sequences)
    uf.constructSolution(sequences,less_freq,metric)