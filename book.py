# -*- coding:utf-8 -*-
# 往pdf文件中添加书签
from PyPDF2 import PdfFileReader as reader,PdfFileWriter as writer

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    book = reader('./book.pdf')

    pdf = writer()
    pdf.cloneDocumentFromReader(book)

    # 添加书签
    # 注意：页数是从0开始的，中文要用unicode字符串，否则会出现乱码
    # 如果这里的页码超过文档的最大页数，会报IndexError异常
    pdf.addBookmark(u'Hello World! 你好，世界！',2)

    # 保存修改后的PDF文件内容到文件中
    # 注意：这里必须用二进制的'wb'模式来写文件，否则写到文件中的内容都为乱码
    with open('./book-with-bookmark.pdf','wb') as fout:
        pdf.write(fout)

if __name__ == '__main__':
    main()