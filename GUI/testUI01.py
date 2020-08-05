import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtGui import QPixmap

#파일명만 바꿔서
form_class = uic.loadUiType("testUI02.ui")[0]
#MainBoard
#giveHint
#etc..


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        menu = QMenu(self)
        menu.addAction('First Item')
        menu.addAction('Second Item')
        menu.addAction('Third Item')
        menu.addAction('Fourth Item')
        self.popupbutton.setMenu(menu)


'''
class MyWindow2(QMainWindow, form_class2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn1.setCheckable(True)
        self.btn1.toggle()
        self.btn2.setText('Button&2')

        # label
        self.label.setAlignment(Qt.AlignCenter)
        font = self.label.font()
        font.setPointSize(10)
        font.setFamily('Times New Roman')
        font.setBold(True)
        self.label.setFont(font)
        #checkBox
        self.cb.toggle()
        #RadioButton
        self.rbtn1.setChecked(True)
        self.rbtn2.setText('도옹구란 버튼')
        #ProgressBar - Button
        self.btnS.clicked.connect(self.doAction)
        self.timer = QBasicTimer()
        self.step = 0
        #Slider, Dial
        self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)
        #PixMap
        pixmap = QPixmap('Hanabi.PNG')
        self.lbl_img.setPixmap(pixmap)
        lbl_size = QLabel('Width: ' + str(pixmap.width()) + ', Height: ' + str(pixmap.height()))
        lbl_size.setAlignment(Qt.AlignCenter)
        #SpinBox
        self.spinbox.valueChanged.connect(self.value_changed)
        #doubleSpinBox
        self.dspinbox.setPrefix('$ ')
        self.dspinbox.valueChanged.connect(self.value_changed2)


    #SpinBox
    def value_changed(self):
        self.lbl2.setText(str(self.spinbox.value()))

    #DoubleSpinBox
    def value_changed2(self):
        self.lbl4.setText('$ ' + str(self.dspinbox.value()))

    #ProgressBar - Button
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btnS.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btnS.setText('Start')
        else:
            self.timer.start(100, self)
            self.btnS.setText('Stop')



'''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
#    myWindow2 = MyWindow2()
#    myWindow2.show()
    app.exec_()