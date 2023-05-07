from btag import *
import json
import sys
import os
import threading
from PyQt5.uic import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel, QAbstractTableModel, Qt
 
    
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
        self.data = pd.DataFrame()
        self.data_af = pd.DataFrame()
        self.bset = {0:[]}
        self.tlist = [0]
        self.tdict = {0:''}
        self.listn = 0
        self.vset = {}

        self.ui = loadUi(r'test.ui', self)
        self.ui.pushButtonl.clicked.connect(self.c_getlist)
        # self.dgt = DataGetThread(self)
        # self.dgt.start()
        self.ui.pushButtonv.clicked.connect(self.c_getdata)
        self.ui.pushButtonshow.clicked.connect(lambda:self.c_showdata(self.data))
        self.ui.pushButtonf.clicked.connect(self.c_tagf)
        self.ui.pushButtonsort.clicked.connect(self.c_sortv)
        self.ui.pushButtonshow2.clicked.connect(lambda:self.c_showdata(self.data_af))
        self.ui.pushButtonr.clicked.connect(self.c_readjs)
        self.ui.pushButtons.clicked.connect(self.c_savejs)
        self.ui.listView.clicked.connect(self.listchange)
        self.ui.lineEditt.editingFinished.connect(self.tlistenter)
        
    def c_showdata(self,data):
        model = PdTable(data)
        self.view = QTableView()
        self.view.setModel(model)
        self.view.setWindowTitle('数据表')
        self.view.resize(1280, 960)
        self.view.setAlternatingRowColors(True)
        self.view.show()

    def c_readjs(self):
        tid =self.tlist[self.listn]
        fjs =readjs(tid)
        if fjs != '':
            self.data = pd.read_json(fjs)
            self.bset[tid] = self.data['bvid'].tolist()
            self.vset[tid] = [Video(self.data.loc[i,'bvid'],self.data.loc[i].to_dict()) for i in range(len(self.data))]
            self.ui.labeld.setText('数据已读取')
        else:
            self.ui.pushButtonr.setText(f'未找到{tid}的json')
            QApplication.processEvents()
            time.sleep(1)
            self.ui.pushButtonr.setText('读取json')

    def c_savejs(self):
        if self.tlist[self.listn] != 0 and len(self.data) >0 :
            fjs = readjs(self.tlist[self.listn])
            if fjs == '':
                self.data.to_json(f'./data_test/{self.tlist[self.listn]}_{int(time.time())}.json','records',force_ascii=False)
            else:
                self.data.to_json(fjs,'records',force_ascii=False)
                os.rename(fjs, f'./data_test/{self.tlist[self.listn]}_{int(time.time())}.json')
            self.ui.labeld.setText('数据已保存')
        else:
            self.ui.pushButtons.setText('无数据')
            QApplication.processEvents()
            time.sleep(1)
            self.ui.pushButtons.setText('保存json')

    def tlistenter(self):
        s_tlist = self.ui.lineEditt.text()
        s_tlist = s_tlist.split(',')
        self.tlist =[]
        td = ''
        n = 5
        for tn in s_tlist:
            tid = totagid(tn)
            self.tlist.append(tid)
            self.tdict[tid] = tn
            td += f'{tn}:{tid}\n'
        self.ui.textBrowser_2.setPlainText(td)

    def c_getlist(self):
        s_tlist = self.ui.lineEditt.text()
        s_tlist = s_tlist.split(',')
        self.tlist =[]
        td = ''
        self.ui.textBrowser_2.setPlainText('拉取中')
        QApplication.processEvents()
        n = 5
        for tn in s_tlist:
            tid = totagid(tn)
            self.tlist.append(tid)
            self.tdict[tid] = tn
            td += f'{tn}:{tid}\n'
        self.bset = {}
        for tid in self.tlist:
            self.bset[tid] = readblist(tid,n)
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
        tid = self.tlist[self.listn]
        if tid == 0: return
        self.ui.labeld.setText('数据读取中')
        QApplication.processEvents()
        if tid in self.vset.keys():
            self.data = pd.DataFrame([v.stat for v in self.vset[tid]])
            self.ui.labeld.setText('数据已读取')
        else:
            i = 1
            vlist = []
            t = len(self.bset[tid])
            for bvid in self.bset[tid]:
                vlist.append(Video(bvid))
                self.ui.labeld.setText(f'数据读取中{i}/{t}')
                QApplication.processEvents()
                i+=1
            self.vset[tid] = vlist
            self.data = pd.DataFrame([v.stat for v in vlist])
            self.ui.labeld.setText('数据已获取')
        return

    def c_tagf(self):
        s_tlist = self.ui.plainTextEdit1.toPlainText()
        s_tlist = s_tlist.split(',')
        tlist1 = [totagid(tn) for tn in s_tlist]
        s_tlist = self.ui.plainTextEdit2.toPlainText()
        s_tlist = s_tlist.split(',')
        tlist2 = [totagid(tn) for tn in s_tlist]
        vlist_af = [Video(k) for k in v_in.keys() if tagcon(k,tlist1,tlist2)]
        self.data_af = pd.DataFrame([v.stat for v in vlist_af])
        self.ui.labelf.setText(f'筛选完成，共{len(vlist_af)}条')

    def c_sortv(self):
        self.data_af = self.data_af.sort_values('view',ascending=False)

# class DataGetThread(threading.Thread):
#     def __init__(self,fw):
#         threading.Thread.__init__(self)
#         self.fw = fw
#     def run(self): 
#         self.fw.c_getdata()
#         print('end')

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

if __name__ == '__main__':
    fjs = None
    app = QApplication(sys.argv)
    mainWindow = firstWindow()
    mainWindow.setWindowTitle('B站Tag视频搜索')
    mainWindow.show()
    sys.exit(app.exec_())
