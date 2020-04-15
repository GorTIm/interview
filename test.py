def descriptiveSeqGenerate(N,first):
    if N==0:
        return first
    str_first=str(first)
   
    re=""
    repeted=1
    for i in range(1,len(str_first)):
        if str_first[i]==str_first[i-1]:
            repeted+=1
        else:
            re+=str(repeted)+str_first[i-1]
            repeted=1
    re+=str(repeted)+str_first[-1]

    return descriptiveSeqGenerate(N-1,int(re))


if __name__=="__main__":
    Nth=input("Nth = ")
    first=input("1st entry =")

    print(descriptiveSeqGenerate(int(Nth),int(first) ))