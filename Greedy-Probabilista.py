import sys
import Resources.Services.FileManager as fm
import Resources.Functions.Greedys as gd
import time

def main():
    file_name=sys.argv[2]
    threshold=sys.argv[4]
    sequences=fm.open_File_By_Name(file_name)
    initial_time=time.time()
    quality=gd.Probabilistic_Greedy(sequences,threshold)
    final_time=time.time()
    print("Time: "+str(final_time-initial_time))
    print("Quality: "+str(quality))

if __name__ == '__main__':
    if(len(sys.argv)==1):
        print("Incorrect execution:\tNo Arguments\n")
        print("For help, enter the following argument:")
        print("\tpython3 Greedy-Probabilista.py -h")
        print("This program will display the time and quality of the solution obtained")


    elif(len(sys.argv)==2 and sys.argv[1]=="-h"):
        print("\t\t\t~~~~~~~~")
        print("\t\t\t| Help |")
        print("\t\t\t~~~~~~~~\n")
        print("For correct execution of the program, you must enter the following arguments:\n")
        print("\tpython3 Greedy-Probabilista.py -i [filename] -th [number]\n")
        print("Example: python3 Greedy-Probabilista.py -i sequences.txt -th 0.5")
        print("Because of problems nature, threshold must be a number between 0 and 1")

    elif((len(sys.argv)==5 and sys.argv[1]=="-i" and sys.argv[3]=="-th")):
        main()
    else:
        print("Incorrect execution")
        print("For help, enter the following argument:")
        print("python3 Greedy-Probabilista.py -h")