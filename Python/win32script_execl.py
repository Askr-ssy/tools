from win32com.client import Dispatch
import win32com.client


class easyExcel:
    """
    A utility to make it easier to get at Excel.  Remembering
    to save the data is your problem, as is  error handling.
    Operates on one workbook at a time.
    """
    def __init__(self, filename=None):
        self.xlApp = win32com.client.Dispatch('Excel.Application')
        self.xlApp.visible=0
        if filename:
            self.filename = filename
            self.xlBook = self.xlApp.Workbooks.Open(filename)
        else:
            self.xlBook = self.xlApp.Workbooks.Add()
            self.filename = ''
    def save(self, newfilename=None):  
    # 保存文件
        if newfilename:
            self.filename = newfilename
            self.xlBook.SaveAs(newfilename)
        else:
            self.xlBook.Save()
    def close(self):  
    # 关闭文件
        self.xlBook.Close(SaveChanges=0)
        del self.xlApp
    def getCell(self, sheet, row, col):  
    # 获取单元格的数据 "Get value of one cell" 
        sht = self.xlBook.Worksheets(sheet)
        return sht.Cells(row, col).Value
    def setCell(self, sheet, row, col, value):  
    # 设置单元格的数据
        sht = self.xlBook.Worksheets(sheet)
        sht.Cells(row, col).Value = value
    def setCellformat(self, sheet, row, col):  
    # 设置单元格的数据
        sht = self.xlBook.Worksheets(sheet)
        sht.Cells(row, col).Font.Size = 15  
    # 字体大小
        sht.Cells(row, col).Font.Bold = True  
    # 是否黑体
        sht.Cells(row, col).Name = "Arial"  
    #字体类型
        sht.Cells(row, col).Interior.ColorIndex = 3  
    # 表格背景
        # sht.Range("A1").Borders.LineStyle = xlDouble
        sht.Cells(row, col).BorderAround(1, 4)  
    # 表格边框
        sht.Rows(3).RowHeight = 30  
    # 行高
        sht.Cells(row, col).HorizontalAlignment = -4131  
    # 水平居中xlCenter
        sht.Cells(row, col).VerticalAlignment = -4160
    def deleteRow(self, sheet, row):
        sht = self.xlBook.Worksheets(sheet)
        sht.Rows(row).Delete()  
    # 删除行
        sht.Columns(row).Delete()  
    # 删除列
    def getRange(self, sheet, row1, col1, row2, col2):  
    # 获得一块区域的数据，返回为一个二维元组
        sht = self.xlBook.Worksheets(sheet)
        return sht.Range(sht.Cells(row1, col1), sht.Cells(row2, col2)).Value
    def addPicture(self, sheet, pictureName, Left, Top, Width, Height):  
    # 插入图片
        sht = self.xlBook.Worksheets(sheet)
        sht.Shapes.AddPicture(pictureName, 1, 1, Left, Top, Width, Height)
    def cpSheet(self, before):  
    # 复制工作表
        shts = self.xlBook.Worksheets
        shts(1).Copy(None, shts(1))
    def inserRow(self, sheet, row):
        sht = self.xlBook.Worksheets(sheet)
        sht.Rows(row).Insert(1)


xls = easyExcel(
    'C:\\Users\\1data-ssy\\Desktop\\Nlp\\code\\History_File\\2牛魔王票务\\EPR\\自身epr.xls')
sht=xls.xlBook.Worksheets[0]
sht.Activate()
# print(sht.Cells('A1:A1').value)
