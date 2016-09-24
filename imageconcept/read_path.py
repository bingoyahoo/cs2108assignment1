import os

#to create new txt file for paths of pics of train pics
#for usage of semanticFeature

def read_path(path):
    wf = open('testFile.txt','w')
    if not os.path.isdir(path):
        if os.path.isfile(path):
            return read_file(path)
    if os.path.isfile(path):
        return read_file(path)
    for root, dirs, list in os.walk(path):
        for i in list:
            dir = os.path.join(root, i)
            wf.write(dir+'\n')
    wf.close()
    return os.getcwd()+'testFile.txt'

def read_file(path):
    wf = open('testFile.txt','w')
    wf.write(path+'\n')
    wf.close()
    return os.getcwd()+'testFile.txt'

def classification(path,semanticFeaturePath='D:\CS2108\semanticFeature'):
    os.system(semanticFeaturePath+' '+'image_classification.exe'+' '+path)

if __name__ == '__main__':
    print os.getcwd()
    path = raw_input('input train path or file path\n')
    classification(read_path(path))