import sys
import os
import Services.FileManager as fm
import Functions.Greedys as gd



def main():
    file_name=sys.argv[2]
    threshold=sys.argv[4]
    sequence=fm.open_File_By_Name(file_name)
    gd.Greedy(sequence,threshold)
    

if __name__ == '__main__':
    print(sys.argv)
    print(len(sys.argv))
    if(len(sys.argv)==1):
        print("No arguments")
    if(len(sys.argv)==2 and sys.argv[1]=="-h"):
        print("Help:")
        print("For correct execution of the program, you must enter the following arguments:")
        print("Usage: python3 main.py -i [filename] -th [number]")
        print("Example: python3 main.py -i sequences.txt -th 0.5")
        print("Because of problems nature, threshold must be a number between 0 and 1")
    if(len(sys.argv)==5 and sys.argv[1]=="-i" and sys.argv[3]=="-th"):
        print("Correct execution")
        main()
    else:
        print("Incorrect execution")
        print("For help, enter the following argument:")
        print("python3 main.py -h")
        