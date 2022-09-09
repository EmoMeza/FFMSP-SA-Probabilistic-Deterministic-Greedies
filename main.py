import utility_functions as uf

def main():
    # file_number=input("Enter the number of the file you want to open: ")
    # threshold=float(input("Enter the threshold value"))
    file_number=69
    threshold=0.75
    sequence=uf.get_Input_From_File(int(file_number))
    uf.Greedy(sequence,threshold)


if __name__ == '__main__':
    main()