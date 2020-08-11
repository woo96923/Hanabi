import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon
from PyQt5.QtCore import Qt, QRect
from Game.GameManager import GameManager as GM
from Game.GameManagerTest import initCards
FONTSIZE = 10

#파일명만 바꿔서
MainAlpha = uic.loadUiType("HanabiAlpha.ui")[0]
GiveHintAlpha = uic.loadUiType("testUI02.ui")[0]
#MainBoard
#giveHint
#etc..

SIDE_MARGIN = 1


class HanabiGui(QMainWindow, MainAlpha):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 배경 사진 넣기
        background = QImage("background.jpeg")
        palette = QPalette()
        palette.setBrush(10, QBrush(background))
        self.setPalette(palette)

        # 임의 부여함.
        self.beginnerIndex = 0
        self.clientIndex = 0

        '''
        initCards : 랜덤으로 줘야 해 - 서버에서 해서 뿌려야 할 것 같음. 진영 용택 논의 필요
        clientIndex : 서버에서 받아야 함
        beginnerIndex : 서버에서 받아야 함
        '''
        self.gm = GM(initCards(5), self.clientIndex, self.beginnerIndex)
        self.gm.distributeCards()
        self.btnGiveHint.clicked.connect(self.clickedGiveHint)
        self.deckList = [[self.player0Deck0, self.player0Deck1, self.player0Deck2, self.player0Deck3],
                         [self.player1Deck0, self.player1Deck1, self.player1Deck2, self.player1Deck3],
                         [self.player2Deck0, self.player2Deck1, self.player2Deck2, self.player2Deck3],
                         [self.player3Deck0, self.player3Deck1, self.player3Deck2, self.player3Deck3]]
        for deck in self.gm.playerDecks:
            print(deck)
        for i, deck in enumerate(self.deckList):
            # clinet 위치를 어떻게 잡느냐가 관건..
            if i == self.clientIndex:
                for j in range(4):
                    SetCardDesign("mine", deck[j])
            else:
                for j in range(4):
                    SetCardDesign(self.gm.playerDecks[i].getCardOrNone(j).getColor(), deck[j])

        self.btnThrow.clicked.connect(self.ShowThrowDeck)
        self.btnDrop.clicked.connect(self.ShowDropDeck)
        self.btnGiveHint.clicked.connect(self.ShowGiveHint)
        #다음 내용은 불변.
        # 창 아이콘
        self.setWindowIcon(QIcon('Hanabi.PNG'))
        #창크기 조절, 출력
        self.setFixedSize(1910, 990)
        self.setWindowTitle('Hanabi')
        self.show()

    def ShowThrowDeck(self):
        print("Opening a Throw window...")
        self.w = AppThrowDeck()
        self.w.setGeometry(QRect(700, 400, 300, 200))
        self.w.show()

    def ShowDropDeck(self):
        print("Opening a Drop window...")
        self.w = AppDropDeck()
        self.w.setGeometry(QRect(700, 400, 300, 200))
        self.w.show()

    def ShowGiveHint(self):
        print("Opening a GiveHint window...")
        # 플레이어 덱 정보를 넘겨야 하므로 gm.playerDecks 를 매개변수로 넣는다.
        self.w = AppGiveHint(self.gm.playerDecks)
        self.w.setGeometry(QRect(700, 400, 300, 200))
        self.w.show()

    def clickedGiveHint(self):
        winGiveHint = GiveHint()
        winGiveHint.show()


        
#    def show(self):
#        super().show()

class GiveHint(QDialog):
    def __init__(self):
        super().__init__()
        #self.setupUi(GiveHintAlpha)
        #self.setFixedSize(900, 500)
        self.setWindowTitle('Give Hint')
        label = QLabel('나는 라벨', self)
        label.setAlignment(Qt.AlignCenter)
        font = label.font()
        font.setPointSize(10)
        font.setFamily('Times New Roman')
        font.setBold(True)
        label.setFont(font)

    def clickedGiveHint(self):
        winGiveHint = GiveHint()
        winGiveHint.show()




    def showModal(self):
        return super().exec_()

def SetCardDesign(color, deck):
    if color == "R":
        deck.setStyleSheet("background-color : rgb(255, 79, 79);"
                           "border-width: 2px;"
                           "border-style : solid;"
                           "border-radius: 20px;"
                           "border-color : rgb(0, 0, 0)"
                           )
    elif color == "G":
        deck.setStyleSheet("background-color : " + "rgb(11, 222, 0);"
                           "border-width: 2px;"
                           "border-style : solid;"
                           "border-radius: 20px;"
                           "border-color : rgb(0, 0, 0)"
                           )
    elif color == "B":
        deck.setStyleSheet("background-color : rgb(49, 190, 255);"
                           "border-width: 2px;"
                           "border-style : solid;"
                           "border-radius: 20px;"
                           "border-color : rgb(0, 0, 0)"
                           )
    elif color == "Y":
        deck.setStyleSheet("background-color : rgb(243, 243, 0);"
                           "border-width: 2px;"
                           "border-style : solid;"
                           "border-radius: 20px;"
                           "border-color : rgb(0, 0, 0)"
                           )
    elif color == "W":
        deck.setStyleSheet("background-color :  rgb(255, 255, 255);"
                           "border-width: 2px;"
                           "border-style : solid;"
                           "border-radius: 20px;"
                           "border-color : rgb(0, 0, 0)"
                           )
    elif color == "mine":
        deck.setStyleSheet("background-color :  rgb(12, 0, 186);"
                           "border-width: 2px;"
                           "border-style : solid;"
                           "border-radius: 20px;"
                           "border-color : rgb(0, 0, 0)"
                           )

class AppThrowDeck(QWidget): #카드 버리기 창
    def __init__(self):
        QWidget.__init__(self)
    def paintEvent(self, e):
        self.setWindowTitle('버리기')
        deck0 = QPushButton("왜안돼?")
        deck1 = QPushButton("왜안돼?")
        deck2 = QPushButton("왜안돼?")
        deck3 = QPushButton("왜안돼?")

        layout1 = QHBoxLayout()
        layout1.addWidget(deck0)
        layout1.addWidget(deck1)
        layout1.addWidget(deck2)
        layout1.addWidget(deck3)
        deck0.setMaximumHeight(400)
        deck1.setMaximumHeight(400)
        deck2.setMaximumHeight(400)
        deck3.setMaximumHeight(400)
        self.setLayout(layout1)

playerDeck = ["R1", "R2", "R3", "R4"]

#카드 내기 창
class AppDropDeck(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        '''
        rbtn1~4 : 체크된 상태에서 내기 버튼 누르면 체크된 카드가 내진다.
        list_rbtn : rbtn을 관리하기 위한 리스트
        '''
        self.rbtn1 = QRadioButton()
        self.rbtn2 = QRadioButton()
        self.rbtn3 = QRadioButton()
        self.rbtn4 = QRadioButton()
        self.btnfin = QPushButton("선택")
        self.btnfin.clicked.connect(self.finBtn)

    def paintEvent(self, e):
        self.setWindowTitle('내기')
        deck0 = QLabel()
        deck1 = QLabel()
        deck2 = QLabel()
        deck3 = QLabel()
        deck0.setAlignment(Qt.AlignCenter)
        deck1.setAlignment(Qt.AlignCenter)
        deck2.setAlignment(Qt.AlignCenter)
        deck3.setAlignment(Qt.AlignCenter)
        space = QLabel(" ")




        layout0 = QVBoxLayout()

        layout0.setAlignment(Qt.AlignCenter)
        layoutrbtn = QHBoxLayout()
        layoutrbtn.addWidget(self.rbtn1)
        layoutrbtn.addWidget(self.rbtn2)
        layoutrbtn.addWidget(self.rbtn3)
        layoutrbtn.addWidget(self.rbtn4)

        #카드배치
        layout1 = QHBoxLayout()
        layout1.addWidget(deck0)
        layout1.addWidget(deck1)
        layout1.addWidget(deck2)
        layout1.addWidget(deck3)
        #카드 크기
        deck0.setMaximumSize(140, 160)
        deck1.setMaximumSize(140, 160)
        deck2.setMaximumSize(140, 160)
        deck3.setMaximumSize(140, 160)
        deck0.setMinimumSize(140, 160)
        deck1.setMinimumSize(140, 160)
        deck2.setMinimumSize(140, 160)
        deck3.setMinimumSize(140, 160)
        self.btnfin.setMaximumWidth(140)

        #위젯 배치
        layoutSpace = QHBoxLayout()
        layoutSpace.addWidget(space)
        layoutSpace.addWidget(self.btnfin)
        layoutSpace.addWidget(space)
        layout0.addLayout(layout1)
        layout0.addLayout(layoutrbtn)
        layout0.addWidget(space)
        layout0.addLayout(layoutSpace)

        #카드 디자인
        SetCardDesign("mine", deck0)
        SetCardDesign("mine", deck1)
        SetCardDesign("mine", deck2)
        SetCardDesign("mine", deck3)

        self.setLayout(layout0)

    def finBtn(self):
        list_rbtn = [self.rbtn0, self.rbtn1, self.rbtn2, self.rbtn3]
        for i, rbtn in enumerate(list_rbtn):
            if rbtn.isChecked():
                print(i)


class AppGiveHint(QWidget): #힌트주기 창
    def __init__(self, playerDecks):
        QWidget.__init__(self)
        self.playerDecks = playerDecks
        self.playerNum = 0
        self.layout2 = QHBoxLayout()
        self.deck0 = QLabel(str(self.playerDecks[self.playerNum].getCardOrNone(0)))
        self.deck1 = QLabel(str(self.playerDecks[self.playerNum].getCardOrNone(1)))
        self.deck2 = QLabel(str(self.playerDecks[self.playerNum].getCardOrNone(2)))
        self.deck3 = QLabel(str(self.playerDecks[self.playerNum].getCardOrNone(3)))

    def paintEvent(self, e):
        self.setWindowTitle('힌트 주기')
        cob = QComboBox(self)
        # 아이디를 서버에서 받아야겠다
        player1 = "1번의 아이디"
        player2 = "2번의 아이디"
        player3 = "3번의 아이디"
        cob.addItem(player1)
        cob.addItem(player2)
        cob.addItem(player3)
        cob.activated[str].connect(self.onActivated)
        # print(self.playerDecks[self.playerNum].getCardorNone(0).getColor())
        layout2 = QHBoxLayout()
        self.deck0 = QLabel(str(self.playerDecks[self.playerNum].getCardOrNone(0)))
        self.deck1 = QLabel(str(self.playerDecks[self.playerNum].getCardOrNone(1)))
        self.deck2 = QLabel(str(self.playerDecks[self.playerNum].getCardOrNone(2)))
        self.deck3 = QLabel(str(self.playerDecks[self.playerNum].getCardOrNone(3)))
        layout2.addWidget(self.deck0)
        layout2.addWidget(self.deck1)
        layout2.addWidget(self.deck2)
        layout2.addWidget(self.deck3)
        self.deck0.setMinimumHeight(160)
        self.deck1.setMinimumHeight(160)
        self.deck2.setMinimumHeight(160)
        self.deck3.setMinimumHeight(160)
        self.deck0.setMaximumWidth(140)
        self.deck1.setMaximumWidth(140)
        self.deck2.setMaximumWidth(140)
        self.deck3.setMaximumWidth(140)
        self.deck0.setAlignment(Qt.AlignCenter)
        self.deck1.setAlignment(Qt.AlignCenter)
        self.deck2.setAlignment(Qt.AlignCenter)
        self.deck3.setAlignment(Qt.AlignCenter)

        SetCardDesign(self.playerDecks[self.playerNum].getCardOrNone(0).getColor(), self.deck0)
        SetCardDesign(self.playerDecks[self.playerNum].getCardOrNone(1).getColor(), self.deck1)
        SetCardDesign(self.playerDecks[self.playerNum].getCardOrNone(2).getColor(), self.deck2)
        SetCardDesign(self.playerDecks[self.playerNum].getCardOrNone(3).getColor(), self.deck3)
        btnNumber1 = QPushButton("1")
        btnNumber2 = QPushButton("2")
        btnNumber3 = QPushButton("3")
        btnNumber4 = QPushButton("4")
        btnNumber5 = QPushButton("5")
        layout3 = QHBoxLayout()
        layout3.addWidget(btnNumber1)
        layout3.addWidget(btnNumber2)
        layout3.addWidget(btnNumber3)
        layout3.addWidget(btnNumber4)
        layout3.addWidget(btnNumber5)

        btnColorR = QPushButton("R")
        btnColorG = QPushButton("G")
        btnColorB = QPushButton("B")
        btnColorY = QPushButton("Y")
        btnColorW = QPushButton("W")
        layout4 = QHBoxLayout()
        layout4.addWidget(btnColorR)
        layout4.addWidget(btnColorG)
        layout4.addWidget(btnColorB)
        layout4.addWidget(btnColorY)
        layout4.addWidget(btnColorW)

        layout5 = QVBoxLayout()
        layout5.addWidget(cob)
        layout5.addLayout(layout2)
        layout5.addLayout(layout3)
        layout5.addLayout(layout4)
        cob.setMaximumSize(300, 30)
        cob.setMinimumSize(300, 30)
        self.setLayout(layout5)

    def onActivated(self, text):
        self.playerNum = int(text[0])
        self.deck0.setText(str(self.playerDecks[self.playerNum].getCardOrNone(0)))
        self.deck1.setText(str(self.playerDecks[self.playerNum].getCardOrNone(1)))
        self.deck2.setText(str(self.playerDecks[self.playerNum].getCardOrNone(2)))
        self.deck3.setText(str(self.playerDecks[self.playerNum].getCardOrNone(3)))
        SetCardDesign(self.playerDecks[self.playerNum].getCardOrNone(0).getColor(), self.deck0)
        SetCardDesign(self.playerDecks[self.playerNum].getCardOrNone(1).getColor(), self.deck1)
        SetCardDesign(self.playerDecks[self.playerNum].getCardOrNone(2).getColor(), self.deck2)
        SetCardDesign(self.playerDecks[self.playerNum].getCardOrNone(3).getColor(), self.deck3)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = HanabiGui()
    myWindow.show()
    app.exec_()