# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyser.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import csv
import os
import matplotlib.pyplot as plt
import csv
import sentiment_analyser 


class Ui_MainWindow(object):
    def Display_Tweets(self):
        print("Positive Tweets----------------------------------------------------------\n\n")
        readtweets = open("positiveTweets.csv", "r")
        tweetlist = readtweets.readlines()
        for x in tweetlist:
            print(x)
        readtweets2 = open("negativeTweets.csv", "r")
        tweetlist2 = readtweets2.readlines()
        print("negative Tweets-------------------------------------------------------------\n\n")
        for y in tweetlist2:
            print(y)
        readtweets2.close()

    def graphs(self):
        os.system("python3 time_graphs.py")

    def senti_analysis(self):
        a = self.Keyword_box.text()
        sentiment_analyser.main(a)
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 1000)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(16)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "../hackathons/Simple_PySide_Base/icons/16x16/cil-magnifying-glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(22, 22, 37);\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(300, 60, 241, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Keyword_box = QtWidgets.QLineEdit(self.frame)
        self.Keyword_box.setGeometry(QtCore.QRect(0, 10, 240, 40))
        self.Keyword_box.setMinimumSize(QtCore.QSize(240, 40))
        self.Keyword_box.setMaximumSize(QtCore.QSize(240, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Keyword_box.setFont(font)
        self.Keyword_box.setStyleSheet("QLineEdit\n"
                                       "{\n"
                                       "    border: 2px solid rgb(48, 48, 81);\n"
                                       "    border-radius:20px;\n"
                                       "    color :#FFF;\n"
                                       "    padding-left: 68px;\n"
                                       "    padding-right: 20px;\n"
                                       "    background-color: rgb(30, 30, 48);\n"
                                       "}\n"
                                       "QLineEdit:hover{\n"
                                       "    border: 2px solid rgb(138, 102, 64);\n"
                                       "}\n"
                                       "QLineEdit:focus{\n"
                                       "    border:2px solid rgb(85, 150, 270);\n"
                                       "    background-color: rgb(43, 45, 56);\n"
                                       "}")
        self.Keyword_box.setText("")
        self.Keyword_box.setAlignment(
            QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.Keyword_box.setObjectName("Keyword_box")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(200, 190, 121, 81))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    border-color: rgb(85, 0, 0);\n"
                                      "    background-color:rgb(22, 22, 37);\n"
                                      "    border:none;\n"
                                      "    border-radius:20px;\n"
                                      "    color: rgb(108,117,125);\n"
                                      "\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    background-color:rgb(40,41,58);\n"
                                      "    border:none;\n"
                                      "    color:rgb(108,117,125);\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "\n"
                                      "    color:rgb(76,117,242);\n"
                                      "    background-color:rgb(30,30,48);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(130, 280, 591, 411))
        self.graphicsView.setStyleSheet("border-radius:20px;\n"
                                        "background-color=rgb(255, 255, 255);")
        self.graphicsView.setObjectName("graphicsView")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(360, 190, 121, 81))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    border-color: rgb(85, 0, 0);\n"
                                        "    background-color:rgb(22, 22, 37);\n"
                                        "    border:none;\n"
                                        "    border-radius:20px;\n"
                                        "    color: rgb(108,117,125);\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color:rgb(40,41,58);\n"
                                        "    border:none;\n"
                                        "    color:rgb(108,117,125);\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "\n"
                                        "    color:rgb(76,117,242);\n"
                                        "    background-color:rgb(30,30,48);\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(520, 190, 121, 81))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 0, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "    font-size = 10px;\n"
                                        "    border-color: rgb(85, 0, 0);\n"
                                        "    background-color:rgb(22, 22, 37);\n"
                                        "    border:none;\n"
                                        "    border-radius:20px;\n"
                                        "    color: rgb(108,117,125);\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color:rgb(40,41,58);\n"
                                        "    border:none;\n"
                                        "    color:rgb(108,117,125);\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "\n"
                                        "    color:rgb(76,117,242);\n"
                                        "    background-color:rgb(30,30,48);\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.Search_button = QtWidgets.QPushButton(self.centralwidget)
        self.Search_button.setGeometry(QtCore.QRect(340, 140, 170, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(16)
        self.Search_button.setFont(font)
        self.Search_button.setStyleSheet("QPushButton{\n"
                                         "    border-color: rgb(85, 0, 0);\n"
                                         "    background-color:rgb(55, 94, 115);\n"
                                         "    border:rgb(32, 32, 47);\n"
                                         "    border-radius:20px;\n"
                                         "    color: rgb(255, 255, 255);\n"
                                         "    border-left:3px solid rgb(130, 65, 0);\n"
                                         "    border-right:3px solid rgb(130, 65, 0);\n"
                                         "    border-bottom:3px solid rgb(130, 65, 0);\n"
                                         "    border-top:3px solid rgb(130, 65, 0);\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    background-color:rgb(138, 79, 149);\n"
                                         "    border:rgb(19, 73, 106);\n"
                                         "    border-left:1px solid rgb(30, 30, 48);\n"
                                         "    border-right:1px solid rgb(30, 30, 48);\n"
                                         "    border-bottom:1px solid rgb(30, 30, 48);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "    background-color:rgb(99, 37, 242);\n"
                                         "    border-left:1px solid rgb(30, 30, 48);\n"
                                         "    border-right:1px solid rgb(30, 30, 48);\n"
                                         "    border-bottom:none;\n"
                                         "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "../hackathons/Simple_PySide_Base/icons/16x16/cil-magnifying-glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(
            "../hackathons/Simple_PySide_Base/icons/16x16/cil-reload.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(
            "../hackathons/Simple_PySide_Base/icons/16x16/cil-magnifying-glass.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.Search_button.setIcon(icon1)
        self.Search_button.setAutoDefault(False)
        self.Search_button.setDefault(False)
        self.Search_button.setObjectName("Search_button")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(62, 704, 751, 241))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.Display_Tweets)
        self.pushButton_3.clicked.connect(self.graphs)
        self.Search_button.clicked.connect(self.senti_analysis)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Keyword_box.setPlaceholderText(
            _translate("MainWindow", "Keyword"))
        self.pushButton.setText(_translate("MainWindow", "Top +ve/-ve "))
        self.pushButton_2.setText(_translate("MainWindow", "Region"))
        self.pushButton_3.setText(_translate("MainWindow", "Time-by-Time"))
        self.Search_button.setText(_translate("MainWindow", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
