import cPickle as pickle
import os

OUTPUT_PROBABILITIES = "output_probabilities.txt"

file_dictionary = open(os.path.join(os.path.dirname(__file__), OUTPUT_PROBABILITIES), "rb")
dictionary = pickle.load(file_dictionary)
file_dictionary.close()

print dictionary
print len(dictionary)

