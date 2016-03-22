# -*- coding: cp936 -*-
import xlrd

class ExcelClass:
##    self.data = xlrd.book.Book()
##    self.table = xlrd.sheet.Sheet()
    def __init__(self, filename, sheetid):
        try:
            self.data = xlrd.open_workbook(filename,encoding_override='utf-8')
            ##self.table = data.sheet_by_name(sheetname)
            self.table = self.data.sheet_by_index(sheetid)
        except Exception,e:
            print str(e)
        self.nrows = self.table.nrows #行数

    def getRow(self,rowid):
        if rowid < self.nrows:
            cols =  self.table.row_values(rowid)
            return cols
        else:
            return []

    def getCell(self,rowid,colid):
        return self.table.cell(rowid,colid).value

    def __del__(self):
        """ close """
        print 'close file'

if __name__ == '__main__':
    
    f = ExcelClass(u'data.xlsx',0)
    print f.getCell(3,0)
        
