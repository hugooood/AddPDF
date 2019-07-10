# coding:utf-8
# 添加PDF书签
from pdf_utils import MyPDFHandler,PDFHandleMode as mode
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    pdf_handler = MyPDFHandler(u'book.pdf',mode = mode.NEWLY)
    pdf_handler.add_bookmarks_by_read_txt('./BookList1.txt',page_offset = 20)
    pdf_handler.save2file(u'test.pdf')

if __name__ == '__main__':
    main()