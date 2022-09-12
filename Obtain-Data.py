import sys
import Resources.Services.Timer as tm
import time

def main():
    print("This procces will take about 8 to 9 minutes depending on your computer") 
    tm.get_answer_Time()
    print("Done")
    print("The results are in the folder Data inside the folder Resources")
if __name__ == '__main__':
    if(len(sys.argv)==1):
        print("Incorrect execution:\tNo Arguments\n")
        print("For help, enter the following argument:")
        print("\tpython3 Obtain-Data.py -h")

    elif(len(sys.argv)==2 and sys.argv[1]=="-h"):
        print("\t\t\t~~~~~~~~")
        print("\t\t\t| Help |")
        print("\t\t\t~~~~~~~~\n")
        print("For correct execution of the program, you must enter the following arguments:\n")
        print("\tpython3 Obtain-Data.py -t\n")
        print("Remember that this program is only for obtaining data, so it is not necessary to enter any more arguments\n")
        print("This program will save the data in the Data folder inside Resources")
        print("The data will save the average execution time for each of the 10 instances and the quality of the solution obtained")

    elif(len(sys.argv)==2 and sys.argv[1]=="-t"):
        main()
    else:
        print("Incorrect execution")
        print("For help, enter the following argument:")
        print("python3 Obtain-Data.py -h")