# напиши здесь код для второго экрана приложения
from instr import *
from PyQt5.Gui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from final_winmimport *
time = QTime(0, 0, 0)
class Experiment():
    def __init__(self,age,test1,test2,test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3

class TestWin(QWidget):
    def __init__(self):
            super().__init__()
            self.set_appear()
            self.initUI()
            self.connects()
            self.show()
        def timer_test(self):
            global time
            time = QTime(0,0,15)
            self.timer = QTimer()
            self.timer.timeout.connect(self.timer1Event)
            self.timer.start(1000)
        def timer1Event(self):
            global time
            time = time.addSecs(-1)
            self.timer_label.setText(time.toString('hh:mm:ss'))
            self.timer_label.setFont(QFont('Times',36,QFont.Bold))
            self.timer_label.setStyleSheet('color: rgb(0,0,0)')
            if time.toString('hh:mm:ss') == '00:00:00':
                self.timer.stop()
        def timer_sits(self):
            global time
            time = QTime(0,0,30)
            self.timer = QTimer()
            self.timer.timeout.connect(self.timer2Event)
            self.timer.start(1500)
        def timer2Event(self)
            global time
            time = time.addSecs(-1)
            self.timer_label.setText(time.toString('hh:mm:ss')[6:8])
            self.timer_label.setFont(QFont('Times',36,QFont.Bold))
            self.timer_label.setStyleSheet('color: rgb(0,0,0)')
            if time.toString('hh:mm:ss') == '00:00:00':
                self.timer.stop()
        def timer_final(self):
            global time
            time = QTime(0,1,0)
            self.timer = QTimer()
            self.timer.timeout.connect(self.timer3Event)
            self.timer.start(1000)
        def timer3Event(self):
            global time
            time = time.addSecs(-1)
            self.timer_label.setFont(QFont('Times',36,QFont.Bold))
            self.timer_label.setText(time.toString('hh,mm,ss'))
            if int(time.toString('hh:mm:ss'[6:8]) >= 45:)
                self.timer_label.setStyleSheet('color: rgb(0,255,0)')
            elif int(time.toString('hh:mm:ss'[6:8]) <= 15:)
                self.timer_label.setStyleSheet('color: rgb(0,0,0)')
            else:
                self.timer_label.setStyleSheet('color: rgb(0,255,0)')
        def set_appear(self):
            self.setWindowTitle(txt_title)
            self.resize(win_width, win,height)
            self.move(win_x, win_y)
        def initUI(self):
            self.hint_name = QLabel(txt_hintman)
            self.age_label = QLabel(txt_hintage)
            self.test1_label = QLabel(txt_hinttest1)
            self.test2_label = QLabel(txt_hinttest2)
            self.test2_label = QLabel(txt_hinttest3)
            self.timer_label = QLabel("00:00")
            self.start_test1 = QPushButton(txt_test1)
            self.start_test2 = QPushButton(txt_test2)
            self.start_test3 = QPushButton(txt_test3)
            self.send_results = QPushButton(txt_sendresults)
            self.name = QLineEdit(txt_name)
            self.age = QLineEdit(txt_age)
            self.test1 = QLineEdit(txt_test1)
            self.test2 = QLineEdit(txt_test2)
            self.test3 = QLineEdit(txt_test3)
            self.vbox1 =QVBoxLayout()
            self.vbox2 =QVBoxLayout()
            self.hbox = QHBoxLayout()
            self.vbox2.addWidget(self.timer_label)
            self.vbox1.addWidget(self.hint_name)
            self.vbox1.addWidget(self.name)
            self.vbox1.addWidget(self.age_label)
            self.vbox1.addWidget(self.age)
            self.vbox1.addWidget(self.test1_label)
            self.vbox1.addWidget(self.start_test1)
            self.vbox1.addWidget(self.test1)
            self.vbox1.addWidget(self.test2_label)
            self.vbox1.addWidget(self.start_test2)
            self.vbox1.addWidget(self.test3_label)
            self.vbox1.addWidget(self.start_test3)
            self.vbox1.addWidget(self.test2)
            self.vbox1.addWidget(self.test3)
            self.vbox1.addWidget(self.send_results)
            self.hbox.addLayout(self.vbox1)
            self.hbox.addLayout(self.vbox2)
            self.setLayout(self.hbox)

    def connects(self):
        self.send_results
        self.start_test1.clicked.connect(self.timer_test)
        self.start_test2.clicked.connect(self.timer_sits)
        self.start_test3.clicked.connect(self.timer_final)

    def next_win(self):
        self.hide()
        self.exp = Experiment(self.age.text(),self.test1.text(),self.test2.text(),self.test3.text)
        self.final_win = FinalWin(self.exp)