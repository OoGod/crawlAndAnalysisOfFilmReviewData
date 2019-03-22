def add_con(file1):
    with open(file1,'r') as f:
        con = f.read()

    with open('test1.txt','a') as f:
        f.write(con)
        f.write('\n')

if __name__ == "__main__":
    file1 = 'output_tra.txt'
    add_con(file1)

