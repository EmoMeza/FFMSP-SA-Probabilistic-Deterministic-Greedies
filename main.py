import utility_functions as uf

def main():
    # sequence=["ACGTA","CCCCG","GTACT","GTCCC","GTGGA","GTGGG"]
    file_number=input("Enter the number of the file you want to open: ")
    sequence=uf.get_Input_From_File(int(file_number))
    uf.Greedy(sequence)


if __name__ == '__main__':
    main()