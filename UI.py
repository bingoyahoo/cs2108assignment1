import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("CS2108 Image Search")
		self.setWindowIcon(QtGui.QIcon("assets/ic_image_search.png"))

		self.home()

	def home(self):
		"""Specific to page"""
		btn = QtGui.QPushButton("Quit", self)
		btn.clicked.connect(self.close_application)
		btn.resize(btn.minimumSizeHint())

		btn_picker = QtGui.QPushButton("Choose an image", self)
		btn_picker.clicked.connect(self.choose_image)
		btn_picker.resize(btn.minimumSizeHint())
		btn_picker.move(100, 100)

		btn_picker = QtGui.QPushButton("Search", self)
		btn_picker.clicked.connect(self.search_image)
		btn_picker.resize(btn.minimumSizeHint())
		btn_picker.move(200, 100)

		self.show()

	def close_application(self):
		print "Closing"
		sys.exit()

	def choose_image(self):
		pass

	def search_image(self):
		pass



def main():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

main()