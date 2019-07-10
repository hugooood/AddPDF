# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from AddBookListForm import Ui_AddBookList

reload(sys)
sys.setdefaultencoding('utf-8')

class Widget(QWidget,Ui_AddBookList):
    def __init__(self):
        super(Widget,self).__init__()
        self.setupUi(self)
        self.center()
        self.PDFURL = None
        self.BookListURL = None
        self.SaveURL = None
        self.AddPDFButton.clicked.connect(self.getPDF)
        self.AddBookListButton.clicked.connect(self.getBookList)
        self.SavePDFButton.clicked.connect(self.getSaveName)
        self.RunButton.clicked.connect(self.run)


    def center(self):   
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width())/2,(screen.height() - size.height())/2)

    def getPDF(self):
        self.AddPDFButton.setStyleSheet("color:black")
        url,_ = QFileDialog.getOpenFileName(self,'Open file','./PDF','pdf files(*.pdf)')
        self.ShowPDFUrlLineEdit.setText(url)
        self.PDFURL = url

    def getBookList(self):
        self.AddBookListButton.setStyleSheet("color:black")
        url,_ = QFileDialog.getOpenFileName(self,'Open file','./BookList','text files(*.txt)')
        self.ShowBookListUrlLineEdit.setText(url)
        self.BookListURL = url

    # 需要判断文件名是否合法
    def getSaveName(self):
        import os
        self.SavePDFButton.setStyleSheet("color:black")
        savename, ok = QInputDialog.getText(self, u'新的PDF命名', u'输入PDF名称:')
        if ok:
            if savename.split('.')[-1] == "pdf":
                self.SaveURL = os.getcwd() + "\\ModifiedPDF\\"+savename
                self.ShowSavePDFUrlLineEdit.setText(str(self.SaveURL))
            else:
                QMessageBox.warning(self, "警告", "请输入以xxx.pdf为格式的文件名", QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes )

    def run(self):
        from pdf_utils import MyPDFHandler,PDFHandleMode as mode

        if self.ShowPDFUrlLineEdit.text() == "":
            QMessageBox.warning(self, "警告", "PDF路径不能为空", QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes )
            # self.AddPDFButton.setStyleSheet("background-color: rgb(255, 0, 0)")
            self.AddPDFButton.setStyleSheet("color:red")
            return
        if self.ShowBookListUrlLineEdit.text() == "":
            QMessageBox.warning(self, "警告", "目录路径不能为空", QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes )
            self.AddBookListButton.setStyleSheet("color:red")
            return       
        if self.ShowSavePDFUrlLineEdit.text() == "":
            QMessageBox.warning(self, "警告", "保存路径不能为空", QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes )
            self.SavePDFButton.setStyleSheet("color:red")
            return          


        if self.PDFURL is not None:
            pdf_handler = MyPDFHandler(self.PDFURL,mode = mode.NEWLY)
        else:
            self.ShowInformationTextEdit.setText('self.PDFURL is None')
        

        try:
            if pdf_handler.add_bookmarks_by_read_txt(self.BookListURL,page_offset = 20):
                self.ShowInformationTextEdit.setText("<font color=green><strong><h3>Success! add_bookmarks_by_read_txt</h3></strong></fond>")
        except Exception:
            self.ShowInformationTextEdit.setText('<font color=red><strong><h3>Failed! add_bookmarks_by_read_txt</h3></strong></fond>')
        
        try:
            if pdf_handler.save2file(self.SaveURL):
                self.ShowInformationTextEdit.setText('<font color=green><strong><h3>Success! new file is: '+self.SaveURL.split('/')[-1]+'</h3></strong></fond>')
        except Exception:
            self.ShowInformationTextEdit.setText('<font color=red><strong><h3>Failed!</h3></strong></fond>')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Widget()
    win.show()
    sys.exit(app.exec_())