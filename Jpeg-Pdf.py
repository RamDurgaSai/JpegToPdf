from PySide2.QtWidgets import QFileDialog,QWidget, QLabel,QPushButton,QApplication,QMainWindow,QHBoxLayout,QVBoxLayout
import sys,os
from PIL import  Image
from PyPDF2 import PdfFileMerger, PdfFileReader

from PySide2.QtGui import QPixmap


class JpegToPdf(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("JpegToPdf")

        self.setMinimumHeight(250)

        self.setMinimumWidth(250)

        self.qv_box=QVBoxLayout()
        self.w = QWidget()

        self.w.setLayout(self.qv_box)

        self.setCentralWidget(self.w)
        self.show()



        #Buttons ......
        self.button_1=QPushButton("Image1")

        self.button_1.clicked.connect(lambda :self.button_clicked(self.button_1))

        self.button_2 = QPushButton("Image2")

        self.button_2.clicked.connect(lambda: self.button_clicked(self.button_2))

        self.button_3 = QPushButton("Image3")

        self.button_3.clicked.connect(lambda: self.button_clicked(self.button_3))

        self.button_start = QPushButton("Start")

        #Labels.......
        self.button_1_label=QLabel()


        self.button_2_label = QLabel()

        self.button_3_label = QLabel()

        self.button_start_label = QLabel()
        
        self.button_start.clicked.connect(self.start)





        self.qv_box.addWidget(self.button_1)

        self.qv_box.addWidget(self.button_1_label)

        self.qv_box.addWidget(self.button_2)

        self.qv_box.addWidget(self.button_2_label)

        self.qv_box.addWidget(self.button_3)

        self.qv_box.addWidget(self.button_3_label)

        self.qv_box.addWidget(self.button_start)

        self.qv_box.addWidget(self.button_start_label)










    def button_clicked(self,b):

        self.image_path = QFileDialog.getOpenFileName()

        if b.text()=="Image1":
            self.image_1_path=self.image_path[0]
            self.button_1_label.setText("Selected Image is : "+os.path.basename(self.image_1_path))

        elif b.text()=="Image2":
            self.image_2_path=self.image_path[0]
            self.button_2_label.setText("Selected Image is : " + os.path.basename(self.image_2_path))

        elif b.text()=="Image3":
            self.image_3_path=self.image_path[0]
            self.button_3_label.setText("Selected Image is : " + os.path.basename(self.image_3_path))

    def start(self):

        image1 = Image.open(self.image_1_path)
        image2 = Image.open(self.image_2_path)
        image3 = Image.open(self.image_3_path)

        im1 = image1.convert('RGB')
        im2 = image2.convert('RGB')
        im3 = image3.convert('RGB')

        self.pdf_1_path=os.path.join(os.path.dirname(self.image_1_path),
                                     str(os.path.basename(self.image_1_path))[:-4]+".pdf")

        self.pdf_2_path = os.path.join(os.path.dirname(self.image_2_path),
                                       str(os.path.basename(self.image_2_path))[:-4] + ".pdf")

        self.pdf_3_path = os.path.join(os.path.dirname(self.image_3_path),
                                       str(os.path.basename(self.image_3_path))[:-4] + ".pdf")


        im1.save(self.pdf_1_path)
        im2.save(self.pdf_2_path)
        im3.save(self.pdf_3_path)

        merger = PdfFileMerger()

        with open(self.pdf_1_path,'rb') as pdf1:
            merger.append(PdfFileReader(pdf1))
        with open(self.pdf_2_path,'rb') as pdf2:
            merger.append(PdfFileReader(pdf2))
        with open(self.pdf_3_path,'rb') as pdf3:
            merger.append(PdfFileReader(pdf3))

        self.pdf_path=os.path.join(os.path.dirname(self.pdf_1_path),str("Merged pdf of  "
                                                                        +str(os.path.basename(self.pdf_1_path))[:-4]
                                                                        +" "
                                                                        +str(os.path.basename(self.pdf_2_path))[:-4]
                                                                        + " "
                                                                        +str(os.path.basename(self.pdf_3_path))[:-4]
                                                                        +" .pdf"
                                                                        ))
        merger.write(self.pdf_path)

        os.remove(self.pdf_1_path)
        os.remove(self.pdf_2_path)
        os.remove(self.pdf_3_path)
        print(self.pdf_path)




































myApp= QApplication(sys.argv)
jpeg_to_pdf=JpegToPdf()
sys.exit(myApp.exec_())


