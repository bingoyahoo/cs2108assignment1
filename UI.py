import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()

window.show()

window.setWindowTitle("CS2108 A1")

sys.exit(app.exec_())