import os
import sqlite3
import cv2
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QComboBox, QMessageBox, \
    QLabel, QHBoxLayout, QFileDialog
from PySide2.QtGui import QPixmap, QImage, QFont, QIcon
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import datetime
from fpdf import FPDF
import json
import shutil
from other_files.threads import *
from ui_files.vits import *
from other_files.ui_functions import *
