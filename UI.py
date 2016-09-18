import sys
from PyQt4 import QtGui


class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("CS2108 Image Search")
		self.setWindowIcon(QtGui.QIcon("assets/ic_image_search.png"))

		self.show()



app = QtGui.QApplication(sys.argv)

GUI = Window()

sys.exit(app.exec_())