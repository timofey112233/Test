# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import *
from instr import *
from PyQt5.QtWidgets import  QWidget, QLabel, QVBoxLayout   

class FinalWin(QWidget):
    def __init__(self,exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        workheart_label = QLabel(txt_workheart + self.results())
        index_label = QLabel(txt_index + str(self.index))
        vbox = QVBoxLayout()
        vbox.addWidget(index_label)
        vbox.addWidget(workheart_label)
        self.setLayout(vbox)
    def results(self):
        self.index = 4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3)-200)/10
        if int(self.exp.age) >= 15:
            if self.index >= 15:
                return txt_starttest1
            elif self.index >= 11 and self.index <15:
                return txt_res2
            elif self.index >= 6 and self.index <11:
                return txt_res3 
            elif self.index >= 0.5 and self.index <6:
                return txt_res4
            else:
                return txt_res5
        elif int(self.exp.age) == 13 and int(self.exp.age) == 14:
            if self.index >= 16.5:
                return txt_starttest1
            elif self.index >= 12.5 and self.index <16.5:
                return txt_res2
            elif self.index >= 7.5 and self.index <12.5:
                return txt_res3 
            elif self.index >= 2 and self.index <7.5:
                return txt_res4
            else:
                return txt_res5
        elif int(self.exp.age) == 11 and int(self.exp.age) == 12:
            if self.index >= 18:
                return txt_starttest1
            elif self.index >= 14 and self.index <18:
                return txt_res2
            elif self.index >= 9 and self.index <14:
                return txt_res3 
            elif self.index >= 3.5 and self.index <9:
                return txt_res4
            else:
                return txt_res5
        elif int(self.exp.age) == 9 and int(self.exp.age) == 10:
            if self.index >= 19.5:
                return txt_starttest1
            elif self.index >= 15.5 and self.index <19.5:
                return txt_res2
            elif self.index >= 10.5 and self.index <15.5:
                return txt_res3 
            elif self.index >= 5 and self.index <10.5:
                return txt_res4
            else:
                return txt_res5
        elif int(self.exp.age) == 7 and int(self.exp.age) == 8:
            if self.index >= 21:
                return txt_starttest1
            elif self.index >= 17 and self.index <21:
                return txt_res2
            elif self.index >= 12 and self.index <17:
                return txt_res3 
            elif self.index >= 6.5 and self.index <12:
                return txt_res4
            else:
                return txt_res5
        else:
            return '0'
