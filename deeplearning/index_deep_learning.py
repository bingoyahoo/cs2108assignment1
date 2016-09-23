from classify_image import run_inference_on_image
import argparse
import glob
import cPickle as pickle

OUTPUT_PROBABILITIES = "output_probabilities.txt"

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = False, default='../ImageData/train/data/*/',
    help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = False, default='index.csv',
    help = "Path to where the computed index will be stored")
args = vars(ap.parse_args())

dict_imgid_prob = {}
# use glob to grab the image paths and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    # extract the image ID (i.e. the unique filename) from the image
    # path and load the image itself
    imageID = imagePath[imagePath.rfind("/") + 1:]

    dict_imgid_prob[imageID] = run_inference_on_image(imagePath)

print dict_imgid_prob
# Store dictionary
file_dictionary = open(OUTPUT_PROBABILITIES, "wb")
pickle.dump(dict_imgid_prob, file_dictionary)
file_dictionary.close()


