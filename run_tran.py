import sys
from translate import translate
from del_spa import del_spa


def wri_con(res):
    with open("output_tra.txt","w") as f:
        f.write(res)
    print("翻译结果已写入output_tra.txt")

if __name__ == "__main__":
    b = 'test.txt'
    a = sys.argv[1] if len(sys.argv)>1 else b
    con = del_spa(a)
    result = translate(con)
    print(result)
    wri_con(result)
    
