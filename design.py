# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageSearchUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(665, 536)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_query_img = QtGui.QLabel(self.centralwidget)
        self.label_query_img.setText(_fromUtf8(""))
        self.label_query_img.setObjectName(_fromUtf8("label_query_img"))
        self.horizontalLayout_6.addWidget(self.label_query_img)
        self.horizontalLayout.addLayout(self.horizontalLayout_6)
        self.btn_picker = QtGui.QPushButton(self.centralwidget)
        self.btn_picker.setMinimumSize(QtCore.QSize(147, 32))
        self.btn_picker.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_picker.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("assets/ic_camera.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_picker.setIcon(icon)
        self.btn_picker.setObjectName(_fromUtf8("btn_picker"))
        self.horizontalLayout.addWidget(self.btn_picker)
        self.btn_search = QtGui.QPushButton(self.centralwidget)
        self.btn_search.setMinimumSize(QtCore.QSize(104, 32))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("assets/ic_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search.setIcon(icon1)
        self.btn_search.setObjectName(_fromUtf8("btn_search"))
        self.horizontalLayout.addWidget(self.btn_search)
        self.tags_search = QtGui.QLineEdit(self.centralwidget)
        self.tags_search.setObjectName(_fromUtf8("tags_search"))
        self.horizontalLayout.addWidget(self.tags_search)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.checkBoxColorHist = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxColorHist.setEnabled(True)
        self.checkBoxColorHist.setChecked(True)
        self.checkBoxColorHist.setObjectName(_fromUtf8("checkBoxColorHist"))
        self.horizontalLayout_3.addWidget(self.checkBoxColorHist)
        self.checkBoxVisualConcept = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxVisualConcept.setEnabled(True)
        self.checkBoxVisualConcept.setChecked(True)
        self.checkBoxVisualConcept.setTristate(False)
        self.checkBoxVisualConcept.setObjectName(_fromUtf8("checkBoxVisualConcept"))
        self.horizontalLayout_3.addWidget(self.checkBoxVisualConcept)
        self.checkBoxVisualKeyword = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxVisualKeyword.setEnabled(True)
        self.checkBoxVisualKeyword.setFocusPolicy(QtCore.Qt.TabFocus)
        self.checkBoxVisualKeyword.setChecked(True)
        self.checkBoxVisualKeyword.setObjectName(_fromUtf8("checkBoxVisualKeyword"))
        self.horizontalLayout_3.addWidget(self.checkBoxVisualKeyword)
        self.checkBoxDeepLearning = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxDeepLearning.setEnabled(True)
        self.checkBoxDeepLearning.setChecked(True)
        self.checkBoxDeepLearning.setObjectName(_fromUtf8("checkBoxDeepLearning"))
        self.horizontalLayout_3.addWidget(self.checkBoxDeepLearning)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.listWidgetResults = QtGui.QListWidget(self.centralwidget)
        self.listWidgetResults.setEnabled(True)
        self.listWidgetResults.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.listWidgetResults.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidgetResults.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.listWidgetResults.setAlternatingRowColors(False)
        self.listWidgetResults.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.listWidgetResults.setIconSize(QtCore.QSize(140, 140))
        self.listWidgetResults.setResizeMode(QtGui.QListView.Adjust)
        self.listWidgetResults.setViewMode(QtGui.QListView.IconMode)
        self.listWidgetResults.setUniformItemSizes(True)
        self.listWidgetResults.setObjectName(_fromUtf8("listWidgetResults"))
        self.verticalLayout.addWidget(self.listWidgetResults)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.btn_reset = QtGui.QPushButton(self.centralwidget)
        self.btn_reset.setMinimumSize(QtCore.QSize(66, 32))
        self.btn_reset.setObjectName(_fromUtf8("btn_reset"))
        self.horizontalLayout_5.addWidget(self.btn_reset)
        self.btn_quit = QtGui.QPushButton(self.centralwidget)
        self.btn_quit.setMinimumSize(QtCore.QSize(66, 32))
        self.btn_quit.setObjectName(_fromUtf8("btn_quit"))
        self.horizontalLayout_5.addWidget(self.btn_quit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tags_search, self.checkBoxVisualConcept)
        MainWindow.setTabOrder(self.checkBoxVisualConcept, self.checkBoxVisualKeyword)
        MainWindow.setTabOrder(self.checkBoxVisualKeyword, self.checkBoxDeepLearning)
        MainWindow.setTabOrder(self.checkBoxDeepLearning, self.btn_reset)
        MainWindow.setTabOrder(self.btn_reset, self.btn_quit)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CS2108 Image Search", None))
        self.btn_picker.setText(_translate("MainWindow", "Choose Image", None))
        self.btn_search.setText(_translate("MainWindow", "Search", None))
        self.checkBoxColorHist.setText(_translate("MainWindow", "Color Histogram", None))
        self.checkBoxVisualConcept.setText(_translate("MainWindow", "Visual Concept", None))
        self.checkBoxVisualKeyword.setText(_translate("MainWindow", "Visual Keyword", None))
        self.checkBoxDeepLearning.setText(_translate("MainWindow", "Deep Learning", None))
        self.btn_reset.setText(_translate("MainWindow", "Clear", None))
        self.btn_quit.setText(_translate("MainWindow", "Quit", None))

