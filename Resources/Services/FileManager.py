import os
import Resources.Classes.Sequences as seq


def open_File_By_Name(name):
    current_path=os.getcwd() 
    file_path=current_path+"/Resources/Examples/"+str(name)
    file=open(file_path,"r")
    sequences=[]
    for line in file:
        sequence=seq.Sequences(line)
        sequences.append(sequence)
    file.close()
    return sequences

def get_Input_From_File(number):
    current_path=os.getcwd() 
    if(number<10):
        filename="100-300-00"+str(number)+".txt"
    elif(number==10):
        filename="100-300-010.txt"
    elif(number==69):
        filename="emo_ejemplo.txt"
    file_path=current_path+"/Resources/Examples/"+str(filename)
    file=open(file_path,"r")
    sequences=[]
    for line in file:
        sequence=seq.Sequences(line)
        sequences.append(sequence)
    file.close()
    return sequences
def save_To_File(average_time,number):
    current_path=os.getcwd() 
    if(number==0):
        file_path=current_path+"/Resources/Data/ProbalisticTime.txt"
    if(number==1):
        file_path=current_path+"/Resources/Data/DeterministicTime.txt"
    file=open(file_path,"w")
    for i in range(0,len(average_time)):
        if(i==0):
            if(number==0):
                file.write("Probabilistic Greedy\n")
            if(number==1):
                file.write("Deterministic Greedy\n")
            file.write("Threshold: 0.75\n")
        if(i<10):
            file.write("100-300-00"+str(i+1)+".txt -> "+str(average_time[i][0])+"\n\tquality average ="+str(average_time[i][1])+"\n")
        if(i==10):
            file.write("Threshold: 0.80\n")
        if(i<20 and i>=10):
            file.write("100-300-0"+str(i-9)+".txt -> "+str(average_time[i][0])+"\n\tquality average ="+str(average_time[i][1])+"\n")
        if(i==20):
            file.write("Threshold: 0.85\n")
        if(i<30 and i>=20):
            file.write("100-300-"+str(i-19)+".txt -> "+str(average_time[i][0])+"\n\tquality average ="+str(average_time[i][1])+"\n")
    file.close()