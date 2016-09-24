import cPickle as pickle
import os
import numpy as np


class DeepLearningSearcher():

	def __init__(self, indexPath):
		OUTPUT_PROBABILITIES = "output_probabilities.txt"

		self.indexPath = indexPath
		file_dictionary = open(os.path.join(os.path.dirname(__file__), OUTPUT_PROBABILITIES), "rb")
		self.dictionary = pickle.load(file_dictionary)
		file_dictionary.close()

		# print self.dictionary
		# print len(self.dictionary)

	def search_deep_learn(self, queryProbability, limit=16):
		results = {}
		queryProbability = np.array(queryProbability)
		for img_id in self.dictionary:
			probabilities = self.dictionary[img_id]
			d = self.chi2_distance(np.array(probabilities), queryProbability)
			results[img_id] = d

		results = sorted([(v, k) for (k, v) in results.items()])
		return results[:limit]


	def chi2_distance(self, histA, histB, eps = 1e-10):
		# Return the chi-squared distance
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])

		return d

