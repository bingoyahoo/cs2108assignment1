import cv2
import numpy as np
import glob
import argparse
import search_sift
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

sab = search_sift.SIFTandBOW()

# use glob to grab the image paths and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    # extract the image ID (i.e. the unique filename) from the image
    # path and load the image itself
    imageID = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)

    kp,des = sab.generate_sift_feature(image)
    sab.addDescriptor(des)

dictionary = sab.clusterBow()

bow_extract = sab.extractBow()
bow_extract.setVocabulary(dictionary)

dict_imgid_hist = {}
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    imageID = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)
    img_id = os.path.basename(imagePath)

    histogram = sab.histogramBow(image)
    dict_imgid_hist[img_id] = histogram

# Store dictionary
file_dictionary = open(OUTPUT_DICTIONARY, "wb")
pickle.dump(dictionary, file_dictionary)
file_dictionary.close()

# Store Image histograms
file_img_hist = open(OUTPUT_IMGID_HIST, "wb")
pickle.dump(dict_imgid_hist, file_img_hist)
file_img_hist.close()



