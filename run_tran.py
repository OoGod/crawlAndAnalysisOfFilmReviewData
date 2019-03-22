import sys
from translate import translate
from del_spa import del_spa
from add_con import add_con


def wri_con(res):
    with open("output_tra.txt","w") as f:
        f.write(res)
    print("翻译结果已写入output_tra.txt")

if __name__ == "__main__":
    b = 'test.txt'
    a = sys.argv[1] if len(sys.argv)>1 else b
    con = del_spa(a)
    print("原文：",con)
    result = translate(con)
    print("翻译结果：",result)
    wri_con(result)
    add_con("output_tra.txt")
    
