import cv2
import numpy as np
import glob
import argparse
# import search_sift
import cPickle as pickle
import os

OUTPUT_DICTIONARY = "output_dict.txt"
OUTPUT_IMGID_HIST = "output_histograms.txt" # Contains img_id1 -> hist1, img_id2 -> hist2, ...

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = False, default='../ImageData/train/data/*/',
    help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = False, default='index.csv',
    help = "Path to where the computed index will be stored")
args = vars(ap.parse_args())

# sab = search_sift.SIFTandBOW(False)

sift = cv2.SIFT()
dictionarySize = 10
BOW = cv2.BOWKMeansTrainer(dictionarySize)

def generate_sift_feature(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kp, des = sift.detectAndCompute(gray,None)
    return kp, des

def addDescriptor(des):
    #add the descriptor into the bag of words
    BOW.add(des)

def clusterBow():
    #cluster the keypoints in the bag of words
    return BOW.cluster()

def extractBow():
    #set up the bow to use for extracting the histogram
    bf = cv2.BFMatcher(cv2.NORM_L2)
    sift2 = cv2.DescriptorExtractor_create("SIFT")
    return cv2.BOWImgDescriptorExtractor(sift2, bf)

def histogramBow(image, bow_extract):
    #compute the histogram based on the bow
    kp,des = generate_sift_feature(image)
    histogram = bow_extract.compute(image, kp)
    histogram = cv2.normalize(histogram, histogram).flatten()
    return histogram
    
def chi2_distance(histA, histB, eps = 1e-10):
    # compute the chi-squared distance
    d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
    for (a, b) in zip(histA, histB)])

    # return the chi-squared distance
    return d

# use glob to grab the image paths and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    # extract the image ID (i.e. the unique filename) from the image
    # path and load the image itself
    imageID = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)

    kp, des = generate_sift_feature(image)
    addDescriptor(des)

dictionary = clusterBow()
bow_extract = extractBow()
bow_extract.setVocabulary(dictionary)

dict_imgid_hist = {}
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    imageID = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)
    img_id = os.path.basename(imagePath)

    histogram = histogramBow(image, bow_extract)
    dict_imgid_hist[img_id] = histogram

# Store dictionary
file_dictionary = open(OUTPUT_DICTIONARY, "wb")
pickle.dump(dictionary, file_dictionary)
file_dictionary.close()

# Store Image histograms
file_img_hist = open(OUTPUT_IMGID_HIST, "wb")
pickle.dump(dict_imgid_hist, file_img_hist)
file_img_hist.close()



