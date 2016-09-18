import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("CS2108 Image Search")
		self.setWindowIcon(QtGui.QIcon("assets/ic_image_search.png"))

		extractAction = QtGui.QAction("&Exit", self)
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip("Leave the app")
		extractAction.triggered.connect(self.close_application)

		self.statusBar()

		mainMenu = self.menuBar() # Need a variable because we are modifying it with more actions
		fileMenu = mainMenu.addMenu("&File")
		mainMenu.setNativeMenuBar(False)
		fileMenu.addAction(extractAction)

		self.home()

	def home(self):
		"""Specific to page"""
		btn = QtGui.QPushButton("Quit", self)
		btn.clicked.connect(self.close_application)
		btn.resize(btn.minimumSizeHint())
		btn.move(50,50)

		btn_picker = QtGui.QPushButton("Choose an image", self)
		btn_picker.clicked.connect(self.choose_image)
		btn_picker.resize(btn.minimumSizeHint())
		btn_picker.move(100, 100)

		btn_picker = QtGui.QPushButton("Search", self)
		btn_picker.clicked.connect(self.search_image)
		btn_picker.resize(btn.minimumSizeHint())
		btn_picker.move(200, 100)


		# Toolbar
		extractAction = QtGui.QAction(QtGui.QIcon("assets/ic_image_search.png"), "Quit", self)
		extractAction.triggered.connect(self.close_application)
		
		self.toolbar = self.addToolBar("Extraction")
		self.toolbar.addAction(extractAction)


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
		pass

	def search_image(self):
		pass



def main():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

main()