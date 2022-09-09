import Functions.FrequentFunctions as ff
import Functions.UtilityFunctions as uf

def Greedy(sequence,threshold):
    less_freq=[]
    less_freq=ff.create_less_frequent(sequence)
    uf.constructSolution(sequence,less_freq,threshold)