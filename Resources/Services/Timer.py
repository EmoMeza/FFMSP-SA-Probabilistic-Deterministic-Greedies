import time
import Resources.Functions.Greedys as gd
import Resources.Services.FileManager as fm

def timer(sequence,threshold):
    average_time=0
    for i in range(0,10):
        start_time=time.time()
        gd.Greedy(sequence,threshold)
        end_time=time.time()
        average_time+=end_time-start_time
    return average_time/10

def get_answer_Time():
    average_time=[]
    threshold=0.75
    for i in range(0,30):
        if(i<10):
            sequence=fm.get_Input_From_File(i+1)
            average_time.append(timer(sequence,threshold))
        if(i==10):
            threshold=0.80
        if(i<20 and i>=10):
            sequence=fm.get_Input_From_File(i-9)
            average_time.append(timer(sequence,threshold))
        if(i==20):
            threshold=0.85
        if(i<30 and i>=20):
            sequence=fm.get_Input_From_File(i-19)
            average_time.append(timer(sequence,threshold))
    fm.save_To_File(average_time)
    return True