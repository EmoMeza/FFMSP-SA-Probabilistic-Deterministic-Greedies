import os


def open_File_By_Name(name):
    current_path=os.getcwd() 
    file_path=current_path+"/examples/"+str(name)
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
    file_path=current_path+"/examples/"+str(filename)
    file=open(file_path,"r")
    sequences=[]
    for line in file:
        sequences.append(line)
    file.close()
    return sequences