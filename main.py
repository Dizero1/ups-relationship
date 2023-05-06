from btag import *
import json
import sys
import os
from PyQt5.uic import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel,QAbstractTableModel, Qt
 
 
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
        self.ui.pushButtonl.clicked.connect(self.c_getlist)
        self.ui.pushButtonshow.clicked.connect(self.c_showdata)
        self.ui.pushButtonr.clicked.connect(self.c_readjs)
        self.ui.pushButtons.clicked.connect(self.c_savejs)
        self.ui.listView.clicked.connect(self.listchange)
        self.tlist =[0]
        self.tdict ={0:''}
        self.listn =0
        # self._data = data

    def c_showdata(self):
        df = pd.DataFrame(self.data)
    
        model = PdTable(df)
        self.view = QTableView()
        self.view.setModel(model)
        self.view.setWindowTitle('数据表')
        self.view.resize(1280, 960)
        self.view.setAlternatingRowColors(True)
        self.view.show()

    def c_readjs(self):
        fjs =readjs(self.tlist[self.listn])
        if fjs != '':
            self.data = pd.read_json(fjs)
            self.bset[self.tlist[self.listn]]=self.data['bvid'].tolist()
            self.ui.labelr.setText('数据已读取')

        else:
            self.ui.pushButtonr.setText(f'未找到{self.tlist[self.listn]}的json')
            QApplication.processEvents()
            time.sleep(1)
            self.ui.pushButtonr.setText('读取json')

    def c_savejs(self):
        if self.tlist[self.listn] != 0 and len(self.data) >0 :
            self.data.to_json(fjs,'records',force_ascii=False)
            os.rename(fjs, f'./data_test/{self.tlist[self.listn]}_{int(time.time())}.json')
        else:
            self.ui.pushButtons.setText('无数据')
            QApplication.processEvents()
            time.sleep(1)
            self.ui.pushButtons.setText('保存json')


    def c_getlist(self):
        s_tlist = self.ui.plainTextEdit.toPlainText()
        s_tlist = s_tlist.split(',')
        self.tlist =[]
        td = ''
        for tn in s_tlist:
            tid = totagid(tn)
            self.tlist.append(tid)
            self.tdict[tid] = tn
            td += f'{tn}:{tid}\n'
        self.bset = {}
        for tid in self.tlist:
            self.bset[tid] = readblist(tid)
        self.ui.textBrowser_2.setPlainText(td)
        self.listn = -1
        self.listchange()

    def listchange(self):
        self.listn = self.listn + 1 if self.listn+1 < len(self.tlist) else 0
        tid = self.tlist[self.listn]
        self.ui.labelt.setText(f'当前tag {self.tdict[tid]} {tid}')
        self.model = [QStringListModel(self.bset[tid]) for tid in self.tlist]
        self.ui.listView.setModel(self.model[self.listn])

    def c_getdata(self):
        pass

def readjs(tid, i = -1): 
    folder = "./data_test/"
    files = os.listdir(folder)
    t =str(tid)
    def file_filter(f):
        return False if re.match(f'{tid}_.*\.json',f)==None else True
    files = list(filter(file_filter, files))
    if files != []:
        return folder+files[i] 
    return ''

def readblist(tid,n=5):
    blist = set()
    for i in range(1,n+1):
        blist = blist or set(bvidlist_bytid(tid,i))
        time.sleep(0.05)
    return list(blist)


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
fjs = None
# data = None
# vlist = []
# data = pd.DataFrame([v.stat for v in vlist])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = firstWindow()
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
