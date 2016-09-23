import sys,imageTrain

class conecptSearch:
    def minus(x,y):
        return x-y
    test_file = 'test.txt'
    train = imageTrain
    wordlist = train.imageTrain.wordlist
    samplelist = train.imageTrain.vectors
    lineList = []
    testPicList = []
    resultPicsList = []
    namelist = train.imageTrain.namelist
    test_read = open(test_file,'r+')
    for line in test_read:
        vector = []
        resList = []
        resultPics = []
        result = len(wordlist)+1
        lineList = line.split()
        testPic = lineList[0]
        lineList = lineList[1:]
        for i in wordlist:
            try:
                index = lineList.index(i)
                vector.append(1)
            except ValueError:
                vector.append(0)
        for sample in samplelist:
            tmp = map(minus,vector,sample)
            res = sum([abs(x) for x in tmp])
            if (res<result):
                resList = []
                resList.append(samplelist.index(sample))
                result = res
            else:
                if (res==result):
                    resList.append(samplelist.index(sample))
        for trainPic in namelist:
            try:
                index = resList.index(namelist.index(trainPic))
                resultPics.append(trainPic)
            except ValueError:
                True
        testPicList.append(testPic)
        resultPicsList.append(resultPics)
    print testPicList #list of pics tested
    print resultPicsList #most similar pics in train