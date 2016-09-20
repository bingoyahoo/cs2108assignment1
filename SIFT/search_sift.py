import cv2
import numpy as np
import cPickle as pickle
import os
import heapq


class SIFTandBOW:
    sift = cv2.SIFT()
    dictionarySize = 10
    BOW = cv2.BOWKMeansTrainer(dictionarySize)

    def __init__(self):
        OUTPUT_DICTIONARY = "output_dict.txt"
        OUTPUT_IMGID_HIST = "output_histograms.txt"
        file_dictionary = open(os.path.join(os.path.dirname(__file__), OUTPUT_DICTIONARY), "rb")
        file_img_hist = open(os.path.join(os.path.dirname(__file__), OUTPUT_IMGID_HIST), "rb")

        self.dictionary = pickle.load(file_dictionary)
        self.img_hist = pickle.load(file_img_hist)

        self.bow_extract = self.extractBow()
        self.bow_extract.setVocabulary(self.dictionary)
        
        file_dictionary.close()
        file_img_hist.close()


    def generate_sift_feature(self,img):
        gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        kp, des = self.sift.detectAndCompute(gray,None)
        return kp, des

    def addDescriptor(self,des):
        #add the descriptor into the bag of words
        self.BOW.add(des)

    def clusterBow(self):
        #cluster the keypoints in the bag of words
        return self.BOW.cluster()
    
    def extractBow(self):
        #set up the bow to use for extracting the histogram
        bf = cv2.BFMatcher(cv2.NORM_L2)
        sift2 = cv2.DescriptorExtractor_create("SIFT")
        return cv2.BOWImgDescriptorExtractor( sift2, bf)

    def histogramBow(self, image):
        #compute the histogram based on the bow
        kp,des = self.generate_sift_feature(image)
        histogram = self.bow_extract.compute(image, kp)
        histogram = cv2.normalize(histogram, histogram).flatten()
        return histogram
        
    def chi2_distance(self, histA, histB, eps = 1e-10):
        # compute the chi-squared distance
        d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
        for (a, b) in zip(histA, histB)])

        # return the chi-squared distance
        return d

    def search(self, query_hist, limit):
        scores = {}
        for x in self.img_hist.iteritems():
            img_id = x[0] + ".jpg"
            db_histogram = x[1]
            # print len(x)
            distance = self.chi2_distance(query_hist, db_histogram)
            scores[img_id] = distance

        heap = []
        for doc in scores:
            scores[doc] = scores[doc]
            heapq.heappush(heap, (scores[doc], doc))


        largest = heapq.nsmallest(limit, heap) # Filter to Top K results based on score
        # return [doc_id for score, doc_id in largest]
        return largest



def main():
    # OUTPUT_DICT = "dict.txt" #
    # dictionary = open(OUTPUT_DICT, "rb")
    # file_dictionary = pickle.load(dictionary)
    # print file_dictionary
    pass

if __name__ == '__main__':
    main()