import sys

def del_spa(file1):
    
    with open(file1,"r") as f:
        con = f.read()
        result = " ".join(con.split())

    return result

def wri_res(result):
    
    with open("output.txt","w") as f:
        f.write(result)

if __name__=="__main__":
    
    a = "machine.txt"
    file1 = sys.argv[1] if len(sys.argv)>1 else a
    res = del_spa(file1)
    wri_res(res)
    print(res)
    
