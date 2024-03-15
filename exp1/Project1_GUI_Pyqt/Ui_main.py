"""
this is a python file that define all the shape in the mainwindow(GUI)
if you need to create a button or lineEdit, you can create it on this file
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")  # the name of mainwindow
        MainWindow.resize(712, 607)  # the size of mainwindow
        # add QWidget in MainWindow
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        # add a QWidget in centralWidget
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 671, 261))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        # add a QHBoxLayout in horizontalLayoutWidget_2
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # add a QGraphicsView in horizontalLayoutWidget_2, and its ID is graphicsView_original_image
        self.graphicsView_original_image = QtWidgets.QGraphicsView(self.horizontalLayoutWidget_2)
        self.graphicsView_original_image.setStyleSheet("border-image: url(:/images/img1.jpg);")
        self.graphicsView_original_image.setObjectName("graphicsView_original_image")
        self.horizontalLayout_2.addWidget(self.graphicsView_original_image)
        # add a QGraphicsView in horizontalLayoutWidget_2, and its ID is graphicsView_current_image
        self.graphicsView_current_image = QtWidgets.QGraphicsView(self.horizontalLayoutWidget_2)
        self.graphicsView_current_image.setStyleSheet("border-image: url(:/images/dst.jpg);")
        self.graphicsView_current_image.setObjectName("graphicsView_current_image")
        self.horizontalLayout_2.addWidget(self.graphicsView_current_image)

        # add a QWidget in centralWidget
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 290, 671, 34))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        # add a QHBoxLayout in horizontalLayoutWidget
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # add a QLabel in horizontalLayoutWidget, and its ID is label_image_path
        self.label_image_path = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_image_path.setObjectName("label_image_path")
        self.horizontalLayout.addWidget(self.label_image_path)
        # add a QLineEdit in horizontalLayoutWidget, and its ID is lineEdit_image_path
        self.lineEdit_image_path = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_image_path.setObjectName("lineEdit_image_path")
        self.horizontalLayout.addWidget(self.lineEdit_image_path)
        # add a QPushButton in horizontalLayoutWidget, and its ID is pushButton_open_image
        self.pushButton_open_image = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_open_image.setObjectName("pushButton_open_image")
        self.horizontalLayout.addWidget(self.pushButton_open_image)

        # add a QWidget in centralWidget
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 400, 671, 34))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        # add a QHBoxLayout in horizontalLayoutWidget_3
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # add a QLabel in horizontalLayoutWidget_3
        self.label_save_image = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_save_image.setObjectName("label_save_image")
        self.horizontalLayout_3.addWidget(self.label_save_image)
        # add a QLineEdit in horizontalLayoutWidget_3, and its ID is lineEdit_save_path
        self.lineEdit_save_path = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_save_path.setObjectName("lineEdit_save_path")
        self.horizontalLayout_3.addWidget(self.lineEdit_save_path)
        # add a QPushButton in horizontalLayoutWidget_3, and its ID is pushButton_save_image
        self.pushButton_save_image = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_save_image.setObjectName("pushButton_save_image")
        self.horizontalLayout_3.addWidget(self.pushButton_save_image)

        # add a QTextEdit in centralWidget, and its ID is textEdit_action_show
        self.textEdit_action_show = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit_action_show.setGeometry(QtCore.QRect(20, 450, 671, 141))
        self.textEdit_action_show.setStyleSheet("")
        self.textEdit_action_show.setLocale(QtCore.QLocale(QtCore.QLocale.Japanese, QtCore.QLocale.Japan))
        self.textEdit_action_show.setReadOnly(True)
        self.textEdit_action_show.setObjectName("textEdit_action_show")

        # add a QWidget in centralWidget
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 340, 671, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        # add a QHBoxLayout in horizontalLayoutWidget_4
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        # add a QPushButton in horizontalLayoutWidget_4, and its ID is pushButton_rgb_gray
        self.pushButton_rgb_gray = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_rgb_gray.setObjectName("pushButton_rgb_gray")
        self.horizontalLayout_4.addWidget(self.pushButton_rgb_gray)
        # add a QPushButton in horizontalLayoutWidget_4, and its ID is pushButton_function_2
        self.pushButton_function_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_function_2.setObjectName("pushButton_function_2")
        self.horizontalLayout_4.addWidget(self.pushButton_function_2)
        # add a QPushButton in horizontalLayoutWidget_4, and its ID is pushButton_function_3
        self.pushButton_function_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_function_3.setObjectName("pushButton_function_3")
        self.horizontalLayout_4.addWidget(self.pushButton_function_3)
        # add a QPushButton in horizontalLayoutWidget_4, and its ID is pushButton_function_4
        self.pushButton_function_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_function_4.setObjectName("pushButton_function_4")
        self.horizontalLayout_4.addWidget(self.pushButton_function_4)
        # add a QPushButton in horizontalLayoutWidget_4, and its ID is pushButton_function_5
        self.pushButton_function_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_function_5.setObjectName("pushButton_function_5")
        self.horizontalLayout_4.addWidget(self.pushButton_function_5)
        # add a QPushButton in horizontalLayoutWidget_4, and its ID is pushButton_function_6
        self.pushButton_function_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_function_6.setObjectName("pushButton_function_6")
        self.horizontalLayout_4.addWidget(self.pushButton_function_6)

        MainWindow.setCentralWidget(self.centralWidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # change the name of each one
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Y_K_C"))
        self.label_image_path.setText(_translate("MainWindow", "image path:"))
        self.pushButton_open_image.setText(_translate("MainWindow", "open image"))
        self.label_save_image.setText(_translate("MainWindow", "save path:"))
        self.pushButton_save_image.setText(_translate("MainWindow", "save"))
        self.pushButton_rgb_gray.setText(_translate("MainWindow", "RGB to GRAY"))
        self.pushButton_function_2.setText(_translate("MainWindow", "Function 2"))
        self.pushButton_function_3.setText(_translate("MainWindow", "Function 3"))
        self.pushButton_function_4.setText(_translate("MainWindow", "Function 4"))
        self.pushButton_function_5.setText(_translate("MainWindow", "Function 5"))
        self.pushButton_function_6.setText(_translate("MainWindow", "Function 6"))

import rec_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
