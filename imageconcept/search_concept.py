import os
import numpy as np

FILE_TEST_RES = 'test_res.txt'
FILE_TRAIN_RES = 'train_res.txt'

def search_concept( filepath , path= r"D:\CS2108\ImageData\ImageData",limit = 10):
    result = {}
    txtpath = filepath.replace(r'.jpg',r'.txt')
    testpic = open(txtpath,'r')
    v = testpic.read().split()
    v = map(float,v)
    tmpv = sorted(v)
    tmp = []
    for m in range(limit):
        x = tmpv.pop()
    for m in v:
        if (m>0):
            if(m not in tmpv):
                tmp.append(m)
            else:
                tmp.append(0)
        else:
            tmp.append(0)
    v = tmp
    train = open(os.path.join(os.path.dirname(__file__), FILE_TRAIN_RES ),'r')
    for lines in train:
        queryv = lines.split()[2:]
        queryv = map(float,queryv)
        d = chi2_distance(queryv,v)
        result[lines.split()[0].replace(r'.txt',r'.jpg')] = d
    train.close()
    result = sorted([(v, k) for (k, v) in result.items()])
    # print result
    return result[:limit]


def chi2_distance( histA, histB,eps = 1e-10):
	# compute the chi-squared distance
	d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
		for (a, b) in zip(histA, histB)])
	# return the chi-squared distance
	return d

if __name__ == '__main__':
    search_concept(raw_input('please input file path\n'))
