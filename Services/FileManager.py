import os



def open_File_By_Name(name):
    current_path=os.getcwd() 
    file_path=current_path+"/Examples/"+str(name)
    file=open(file_path,"r")
    sequences=[]
    for line in file:
        sequences.append(line)
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
    file_path=current_path+"/Examples/"+str(filename)
    file=open(file_path,"r")
    sequences=[]
    for line in file:
        sequences.append(line)
    file.close()
    return sequences
#create a program that can recieve muiltiple strings and write them to a file
def save_To_File(average_time):
    current_path=os.getcwd() 
    file_path=current_path+"/Data/times.txt"
    file=open(file_path,"w")
    for i in range(0,len(average_time)):
        if(i==0):
            file.write("Threshold: 0.75\n")
        if(i<10):
            file.write("100-300-00"+str(i+1)+".txt -> "+str(average_time[i])+"\n")
        if(i==10):
            file.write("Threshold: 0.80\n")
        if(i<20 and i>=10):
            file.write("100-300-0"+str(i-9)+".txt -> "+str(average_time[i])+"\n")
        if(i==20):
            file.write("Threshold: 0.85\n")
        if(i<30 and i>=20):
            file.write("100-300-"+str(i-19)+".txt -> "+str(average_time[i])+"\n")
    file.close()