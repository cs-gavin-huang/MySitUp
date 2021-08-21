# -*- coding: utf-8 -*-
import sys
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import copy
import xml.etree.cElementTree as et
import os
import cv2
import math
from PIL import Image

cUI, cBASE = uic.loadUiType("image_widget.ui")

class CImageWidget(QWidget,cUI):
    def __init__(self):
    

    def closeEvent(self,event):

    def set_info(self, image_path, kp_list=None):

    def set_current_cls(self, cls):

    def get_info(self):

    def draw_background(self, painter):

    def draw_image(self, painter):
    
    def draw_kp_info(self, painter):
    
    def paintEvent(self, event):
    
    def mousePressEvent(self, e):

if __name__ == "__main__":
    cApp = QApplication(sys.argv)
    cImageWidget = CImageWidget()
    cImageWidget.show()
    cImageWidget.set_info('./1.jpg')
    sys.exit(cApp.exec_())