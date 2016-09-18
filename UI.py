import sys
import os
import cv2
from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
import design

class Window(QtGui.QMainWindow, design.Ui_MainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.setupUi(self)
		# QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
		# QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))
		# QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("motif"))
		# QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("cde"))
		# self.show()


		# self.setGeometry(50, 50, 500, 300)
		# self.setWindowTitle("CS2108 Image Search")
		# self.setWindowIcon(QtGui.QIcon("assets/ic_image_search.png"))

		# extractAction = QtGui.QAction("&Exit", self)
		# extractAction.setShortcut("Ctrl+Q")
		# extractAction.setStatusTip("Leave the app")
		# extractAction.triggered.connect(self.close_application)

		# self.statusBar()

		# mainMenu = self.menuBar() # Need a variable because we are modifying it with more actions
		# fileMenu = mainMenu.addMenu("&File")
		# self.menubar.setNativeMenuBar(False)
		# fileMenu.addAction(extractAction)

		self.home()

	def home(self):
		"""Specific to page"""
		# btn = QtGui.QPushButton("Quit", self)
		# btn.clicked.connect(self.close_application)
		# btn.resize(btn.minimumSizeHint())
		# btn.move(50,50)

		# btn_picker = QtGui.QPushButton("Choose an image", self)
		self.btn_picker.clicked.connect(self.choose_image)
		self.btn_search.clicked.connect(self.search_image)
		self.btn_quit.clicked.connect(self.close_application)
		self.btn_reset.clicked.connect(self.clear_results)


		# # Toolbar
		# extractAction = QtGui.QAction(QtGui.QIcon("assets/ic_image_search.png"), "Quit", self)
		# extractAction.triggered.connect(self.close_application)
		
		# self.toolbar = self.addToolBar("Extraction")
		# self.toolbar.addAction(extractAction)


		self.show()

	def closeEvent(self, event):
		event.ignore()
		self.close_application()

	def close_application(self):
		choice = QtGui.QMessageBox.question(self, "Quit?", 
			"Are you sure to quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

		if choice == QtGui.QMessageBox.Yes:
			sys.exit()
		else:
			pass

	def choose_image(self):
		print "Chose"
		
		self.filename = QtGui.QFileDialog.getOpenFileName(self, "Open Image", "Images (*.jpg *.gif *.png)")
		# file = open(name, "r") 	
		self.label_query_img.setPixmap(QPixmap(self.filename).scaledToWidth(100) )

		# process query image to feature vector
		# initialize the image descriptor
		cd = ColorDescriptor((8, 12, 3))
		self.filename = str(self.filename)
		query = cv2.imread(self.filename)

		# load the query image and describe it
		self.queryfeatures = cd.describe(query)


	def search_image(self):
		   # perform the search
		searcher = Searcher("index.csv")
		results = searcher.search(self.queryfeatures, limit=16)

		for (score, img_id) in results:
			fullpath = os.path.join(os.path.curdir, "dataset", img_id)
			img_widget_icon = QListWidgetItem(QIcon(fullpath), img_id)
			# img_widget_icon.setSizeHint(QtCore.QSize(180, 180))
			self.listWidgetResults.addItem(img_widget_icon)


	def clear_results(self):
		self.listWidgetResults.clear()



def main():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

main()