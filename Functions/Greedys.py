import Functions.FrequentFunctions as ff
import Functions.UtilityFunctions as uf

def Greedy(sequences,threshold):
    less_freq=[]
    less_freq=ff.create_less_frequent(sequences)
    uf.constructSolution(sequences,less_freq,threshold)