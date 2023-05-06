from btag import *
import json
import sys
import os
from PyQt5.uic import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import (QAbstractTableModel, Qt)
 
 
class PdTable(QAbstractTableModel):
    #copy
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data
 
    def rowCount(self, parent=None):
        return self._data.shape[0]
 
    def columnCount(self, parent=None):
        return self._data.shape[1]
 
    # 显示数据
    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None
 
    # 显示行和列头
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self._data.axes[0][col]
        return None
 

class firstWindow(QMainWindow):
    def __init__(self):
        super(firstWindow, self).__init__()
        self.ui = loadUi(r'test.ui', self)
        self.ui.pushButton.clicked.connect(self.clickToPrint)
        self.ui.pushButton_show.clicked.connect(self.clicktoshow)
        # self._data = data

    def clickToPrint(self):
        info = self.ui.textEdit.toPlainText()
        print('1')

    def clicktoshow(self):
        df = pd.DataFrame(self._data)
    
        model = PdTable(df)
        self.view = QTableView()
        self.view.setModel(model)
        self.view.setWindowTitle('数据表')
        self.view.resize(1280, 960)
        self.view.setAlternatingRowColors(True)
        self.view.show()

def readjs(tid, i = -1): 
    folder = "./data_test/"
    files = os.listdir(folder)
    t =str(tid)
    def file_filter(f):
        return False if re.match(f'{tid}_.*\.json',f)==None else True
    files = list(filter(file_filter, files))
    return folder+files[i] 

tid = 2885698
tname = '小由'

# print(f'loading:videolist of \'{tname}\' tag(40 in 1 page)')
# blist = []
# n = 5
# for i in range(1,n+1):
#     blist = blist + bvidlist_bytid(tid,i)
# blist = list(set(blist))   
# print(f'loading:video of the list')

# input('continue:')
# vlist = [Video(bvid) for bvid in blist]
# print('loading completed')
fjs =readjs(tid)
data = pd.read_json(fjs)
# vlist = []
# data = pd.DataFrame([v.stat for v in vlist])
data.to_json(fjs,'records',force_ascii=False)
os.rename(fjs, f'./data_test/{tid}_{int(time.time())}.json')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = firstWindow()
    mainWindow._data = data
    mainWindow.show()
    sys.exit(app.exec_())
    

# num = 1
# num = int(input('which video:'))
# while num > 0:
#     key = input('which key:')
#     if key == 'all':
#         print(vlist[num-1].stat)
#     else:
#         try:
#             print(vlist[num-1].stat[key])
#         except:
#             print(key, 'keyerror')
#     try:
#         num = int(input('which video:'))
#     except:
#         pass
#     else:
#         num=0
