import time
import Resources.Functions.Greedys as gd
import Resources.Services.FileManager as fm

def timer(sequence,threshold,number):
    if(number==0):
        average_time=0
        quality=0
        for i in range(0,10):
            start_time=time.time()
            quality=float(gd.Probabilistic_Greedy(sequence,threshold)+quality)
            end_time=time.time()
            average_time+=end_time-start_time
        answer=[]
        answer.append(average_time/10)
        quality=quality/10
        answer.append(str(quality))
    if(number==1):
        quality=0
        average_time=0
        for i in range(0,10):
            start_time=time.time()
            quality=float(gd.Deterministic_Greedy(sequence,threshold)+quality)
            end_time=time.time()
            average_time+=end_time-start_time
        answer=[]
        answer.append(average_time/10)
        quality=quality/10
        answer.append(str(quality))
    return answer
    
def get_answer_Time():
    for j in range(0,2):
        average_time=[]
        threshold=0.75
        for i in range(0,30):
            if(i<10):
                sequence=fm.get_Input_From_File(i+1)
                average_time.append(timer(sequence,threshold,j))
            if(i==10):
                threshold=0.80
            if(i<20 and i>=10):
                sequence=fm.get_Input_From_File(i-9)
                average_time.append(timer(sequence,threshold,j))
            if(i==20):
                threshold=0.85
            if(i<30 and i>=20):
                sequence=fm.get_Input_From_File(i-19)
                average_time.append(timer(sequence,threshold,j))
        fm.save_To_File(average_time,j)
    return True