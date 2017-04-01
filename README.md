## Introduction:
This is a simple __Image-based retrieval system__ written in Python 2.7. It uses basic visual features like Color Histogram, Visual Concept, Visual Keywords, Deep Learning and text retrieval to search for 16 images in the database that is most similar to the one uploaded by an user. The user can also tweak the weights to fine-tune the ranking of the results. 

Here is a screenshot:

![Image Retrieval](https://github.com/bingoyahoo/cs2108assignment1/blob/master/Latest%20Screenshot.png)


---
## How to run

1. Install all dependencies including cv2, numpy, PyQt4
  
  a. To install PyQt4: 
    
    i. For Mac users, use brew and just run "brew install pyqt". 
    
    ii. For Windows users, go to the [PyQt Download page](https://www.riverbankcomputing.com/software/pyqt/download) , choose the version for Py2.7, Qt4.8 and finally 32/64 bit depending on your system.

2. Simply run `python UI.py` from terminal/command prompt! Enjoy!

---
## Developers Tips:
- Put all of your code and index files into a separate folder for easier packaging.
- Name the folder `xxxxxsearch` where xxxxx is the feature name.
- Follow the demo, import your files into `UI.py` and call the functions.
- Note: You need to create an `__init__.py` file in that folder for importing. Ths `__init__.py` file can be empty.


---
## Note:
- This system only works for .jpg images for now.
