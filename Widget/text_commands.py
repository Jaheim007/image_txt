from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from Widget.text import Ui_MainWindow
import pytesseract
from fpdf import FPDF

class command(QMainWindow, Ui_MainWindow):
    def __init__(self):    
        super().__init__()
        self.setupUi(self)
        self.select_btn.clicked.connect(self.browse)
        self.police_btn.clicked.connect(self.text)
        self.pdf_btn.clicked.connect(self.pdf)
        
    def browse(self): 
        global image_text   
        File = QFileDialog.getOpenFileName(self, 'Open File', '/Users/imac-13/Desktop/text_image/Static', 'Image files (*.jpg *.png *.webp)')
        
        imagepath = File[0]
        pixmap = QPixmap(imagepath)
        self.image_show.setPixmap(QPixmap(pixmap)) 
        image_text = pytesseract.image_to_string(imagepath)
        
    def text(self):
        self.text_show.setText(image_text)
        
    def pdf(self):     
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 25) 
        pdf.cell(200, 10, txt = image_text, 
        align = 'L') 
        pdf.ln()
        pdf.output("image_text.pdf")
        
    
    
        
        
    