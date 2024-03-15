"""
this is a python file that define all the functions in the mainwindow
"""

import sys
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Ui_main import Ui_MainWindow
from PyQt5.QtGui import *

import os
import cv2  
from datetime import datetime

# from function python file (rgb_to_gray.py) import the function
from rgb_to_gray import *
from fuction2 import *
from fuction3 import *
from fuction6 import *
# import numpy as np


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.i = 0
        self.current_path = os.getcwd()
        self.lineEdit_image_path.setText(os.path.join(self.current_path,  "img1.jpg"))
        self.img = cv2.imread(os.path.join(self.current_path,  "img1.jpg"))
        self.dst = self.img
        self.lineEdit_save_path.setText("dst.jpg")
        self.textEdit_action_show.append("your processing")
        
    # define the function of button (open image),
    # where 'pushButton_open_image' denoted the ID of this button,
    # 'on' denoted act on this button,
    # 'clicked' denoted the action.
    @pyqtSlot()
    def on_pushButton_open_image_clicked(self):
        # open the folder of computer, and read the file name of the input image
        image_file_name, _ = QFileDialog.getOpenFileName(self)
        # show the path of input image in the lineEdit
        self.lineEdit_image_path.setText(image_file_name)
        # load the image
        self.img = cv2.imread(image_file_name)
        # due to PyQt can only show QImage, so read the input image again based on QImage
        origin_img = QImage()
        origin_img.load(image_file_name)
        # change the scale of the input image, and show the image into the rectangle.
        # where graphicsView_original_image denote the ID of the left rectangle, which used to show the image
        origin_img=origin_img.scaled(self.graphicsView_original_image.width(), self.graphicsView_original_image.height())
        scene=QGraphicsScene()
        scene.addPixmap(QPixmap().fromImage(origin_img))
        self.graphicsView_original_image.setScene(scene)

        self.dst = self.img
        # show the processing information on the bottom rectangle
        self.i += 1 
        self.textEdit_action_show.append("step_{}: from {} load one image, and show it on the left".format(self.i,  image_file_name))

    # define the function of button (RGB to GRAY),
    # where 'pushButton_rgb_gray' denoted the ID of this button,
    # 'on' denoted act on this button,
    # 'clicked' denoted the action.
    @pyqtSlot()
    def on_pushButton_rgb_gray_clicked(self):
        # if current image is a RGB image, clicked this button will change to gray image
        # otherwise it will recommend you input RGB image
        img_shape = self.dst.shape
        if len(img_shape) != 3:
            self.textEdit_action_show.append("error: please input RGB image")
        else:
            # using the function of file(rgb_to_gray) to change a RGB image into GRAY image
            self.dst = rgb2gray(self.dst)
            # convert current result image into QImage, change its scale, and show it on the right rectangle,
            # the ID of right rectangle is graphicsView_current_image
            current_img = QImage(self.dst.data, self.dst.shape[1], self.dst.shape[0], QImage.Format_Grayscale8)
            current_img = current_img.scaled(self.graphicsView_current_image.width(),self.graphicsView_current_image.height())
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap().fromImage(current_img))
            self.graphicsView_current_image.setScene(scene)
            # show the processing information on the bottom rectangle
            self.i += 1 
            self.textEdit_action_show.append("step_{}: change RGB image to gray, and show it on the right".format(self.i))

    # define the function of button (function_2),
    # where 'pushButton_function_2' denoted the ID of this button,
    # 'on' denoted act on this button,
    # 'clicked' denoted the action.
    @pyqtSlot()
    def on_pushButton_function_2_clicked(self):
        # if current image is a RGB image, clicked this button will change to gray image
        # otherwise it will recommend you input RGB image
        img_shape = self.dst.shape
        if len(img_shape) != 3:
            self.textEdit_action_show.append("error: please input RGB image")
        else:
            # using the function of file(function_2) to flip a RGB image
            self.dst = myproc(self.dst)
            # convert current result image into QImage, change its scale, and show it on the right rectangle,
            # the ID of right rectangle is graphicsView_current_image
            current_img = QImage(self.dst.data, self.dst.shape[1], self.dst.shape[0], QImage.Format_RGB888)
            current_img = current_img.scaled(self.graphicsView_current_image.width(),self.graphicsView_current_image.height())
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap().fromImage(current_img))
            self.graphicsView_current_image.setScene(scene)
            # show the processing information on the bottom rectangle
            self.i += 1 
            self.textEdit_action_show.append("step_{}: Execute Function 2, and show the result on the right".format(self.i))

    # define the function of button (function_3),
    # where 'pushButton_function_3' denoted the ID of this button,
    # 'on' denoted act on this button,
    # 'clicked' denoted the action.
    @pyqtSlot()
    def on_pushButton_function_3_clicked(self):
        # if current image is a RGB image, clicked this button will blur it to gray image
        # otherwise it will recommend you input RGB image
        img_shape = self.dst.shape
        if len(img_shape) != 3:
            self.textEdit_action_show.append("error: please input RGB image")
        else:
            # using the function of file(function_3) to ......
            self.dst = myproc(self.dst)
            # convert current result image into QImage, change its scale, and show it on the right rectangle,
            # the ID of right rectangle is graphicsView_current_image
            current_img = QImage(self.dst.data, self.dst.shape[1], self.dst.shape[0], QImage.Format_RGB888)
            current_img = current_img.scaled(self.graphicsView_current_image.width(),self.graphicsView_current_image.height())
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap().fromImage(current_img))
            self.graphicsView_current_image.setScene(scene)
            # show the processing information on the bottom rectangle
            self.i += 1 
            self.textEdit_action_show.append("step_{}: Execute Function 3, and show the result on the righ".format(self.i))

    # define the function of button (function_4),
    # where 'pushButton_function_4' denoted the ID of this button,
    # 'on' denoted act on this button,
    # 'clicked' denoted the action.
    @pyqtSlot()
    def on_pushButton_function_4_clicked(self):
        # if current image is a RGB image, clicked this button will ......
        # otherwise it will recommend you input RGB image
        img_shape = self.dst.shape
        if len(img_shape) != 3:
            self.textEdit_action_show.append("error: please input RGB image")
        else:
            # using the function of file(function_4) to ........
            self.dst = myproc(self.dst)
            # convert current result image into QImage, change its scale, and show it on the right rectangle,
            # the ID of right rectangle is graphicsView_current_image
            current_img = QImage(self.dst.data, self.dst.shape[1], self.dst.shape[0], QImage.Format_RGB888)
            current_img = current_img.scaled(self.graphicsView_current_image.width(),self.graphicsView_current_image.height())
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap().fromImage(current_img))
            self.graphicsView_current_image.setScene(scene)
            # show the processing information on the bottom rectangle
            self.i += 1 
            self.textEdit_action_show.append("step_{}: Execute Function 4, and show the result on the righ".format(self.i))

    # define the function of button (function_5),
    # where 'pushButton_function_5' denoted the ID of this button,
    # 'on' denoted act on this button,
    # 'clicked' denoted the action.
    @pyqtSlot()
    def on_pushButton_function_5_clicked(self):
        # if current image is a RGB image, clicked this button will .....
        # otherwise it will recommend you input RGB image
        img_shape = self.dst.shape
        if len(img_shape) != 3:
            self.textEdit_action_show.append("error: please input RGB image")
        else:
            # using the function of file(function_5) to .....
            self.dst = myproc(self.dst)
            # convert current result image into QImage, change its scale, and show it on the right rectangle,
            # the ID of right rectangle is graphicsView_current_image
            current_img = QImage(self.dst.data, self.dst.shape[1], self.dst.shape[0], QImage.Format_RGB888)
            current_img = current_img.scaled(self.graphicsView_current_image.width(),self.graphicsView_current_image.height())
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap().fromImage(current_img))
            self.graphicsView_current_image.setScene(scene)
            # show the processing information on the bottom rectangle
            self.i += 1 
            self.textEdit_action_show.append("step_{}: Execute Function 5, and show the result on the righ".format(self.i))

    # define the function of button (function_6),
    # where 'pushButton_function_6' denoted the ID of this button,
    # 'on' denoted act on this button,
    # 'clicked' denoted the action.
    @pyqtSlot()
    def on_pushButton_function_6_clicked(self):
        # if current image is a RGB image, clicked this button will ......
        # otherwise it will recommend you input RGB image
        img_shape = self.dst.shape
        if len(img_shape) != 3:
            self.textEdit_action_show.append("error: please input RGB image")
        else:
            # using the function of file(function_6) to .....
            self.dst = function6(self.dst)
            # convert current result image into QImage, change its scale, and show it on the right rectangle,
            # the ID of right rectangle is graphicsView_current_image
            current_img = QImage(self.dst.data, self.dst.shape[1], self.dst.shape[0], QImage.Format_RGB888)
            current_img = current_img.scaled(self.graphicsView_current_image.width(),self.graphicsView_current_image.height())
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap().fromImage(current_img))
            self.graphicsView_current_image.setScene(scene)
            # show the processing information on the bottom rectangle
            self.i += 1 
            self.textEdit_action_show.append("step_{}: Execute Function 6, and show the result on the righ".format(self.i))


    # define the function of button (save),
    # where 'pushButton_save_image' denoted the ID of this button,
    # 'on' denoted act on this button,
    # 'clicked' denoted the action.
    @pyqtSlot()
    def on_pushButton_save_image_clicked(self):
        # read the information of the lineEdit(ID: lineEdit_save_path)
        file_name = self.lineEdit_save_path.text()
        # create the path to save the result image and save the image
        save_path = os.path.join(self.current_path,  file_name)
        cv2.imwrite(save_path, self.dst)
        # show the processing information on the bottom rectangle
        self.i += 1 
        self.textEdit_action_show.append("step_{}: the result saved in {} ".format(self.i,  save_path))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

