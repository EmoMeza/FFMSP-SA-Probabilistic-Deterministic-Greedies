import sys
import Resources.Services.FileManager as fm
import Resources.Services.Timer as tm
import Resources.Functions.Greedys as gd

def main():
    if(sys.argv[1]=="-t"):
        tm.get_answer_Time()
    else:
        file_name=sys.argv[2]
        threshold=sys.argv[4]
        sequences=fm.open_File_By_Name(file_name)
        greedy=input("Which greedy do you want to use? (1 or 2): ")
        if(greedy=="1"):
            gd.Greedy(sequences,threshold)
        elif(greedy=="2"):
            gd.Greedy2(sequences,threshold)

if __name__ == '__main__':
    if(len(sys.argv)==1):
        print("No arguments")

    if(len(sys.argv)==2 and sys.argv[1]=="-h"):
        print("Help:")
        print("For correct execution of the program, you must enter the following arguments:")
        print("Usage: python3 main.py -i [filename] -th [number]")
        print("Example: python3 main.py -i sequences.txt -th 0.5")
        print("Because of problems nature, threshold must be a number between 0 and 1")

    if((len(sys.argv)==5 and sys.argv[1]=="-i" and sys.argv[3]=="-th")or(len(sys.argv)==2 and sys.argv[1]=="-t")):
        print("Correct execution")
        main()

    else:
        print("Incorrect execution")
        print("For help, enter the following argument:")
        print("python3 main.py -h")