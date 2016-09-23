import sys

class imageTrain:
    train_file = 'train_test.txt'
    wordlist = []
    namelist = []
    vectors = []

    train = open(train_file,'r+')
    for line in train:
        linelist = line.split()
        linelist = linelist[1:]
        for i in linelist:
            try:
                index = wordlist.index(i)
            except ValueError:
                wordlist.append(i)

    vsize = len(wordlist)
    train.close()
    train = open(train_file,'r+')
    
    for line in train:
        linelist = line.split()
        namelist.append(linelist[0])
        linelist = linelist[1:]
        vectorindex =[]
        for i in linelist:
            ind = wordlist.index(i)
            vectorindex.append(ind)
        vector = []
        for i in range(0,vsize):
            if i in vectorindex:
                vector.append(1)
            else:
                vector.append(0)
        vectors.append(vector)
        
    print wordlist #all trained words to describe
    print namelist #name of all used pics
    print vectors #vector of pics




