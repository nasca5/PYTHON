import sys

Option = sys.argv[1]

if Option == "-a" :
    Memo = sys.argv[2]  
    f = open("./project/diary.txt", 'a')
    f.write(Memo)
    f.write('\n')
    f.close()

elif Option == "-v" :
    f = open("./project/diary.txt", "r")
    Memo = f.read()
    print(Memo)
    f.close()
