import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon
from PyQt5.QtCore import Qt, QRect
from Game.GameManager import GameManager as GM
from Game.GameManagerTest import initCards


FONTSIZE = 10

# 파일명만 바꿔서
MainAlpha = uic.loadUiType("HanabiAlpha.ui")[0]
GiveHintAlpha = uic.loadUiType("testUI02.ui")[0]
# MainBoard
# giveHint
# etc..

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
        self.isTurn = 1
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
        # 다음 내용은 불변.
        # 창 아이콘
        self.setWindowIcon(QIcon('Hanabi.PNG'))
        # 창크기 조절, 출력
        self.setFixedSize(1910, 990)
        self.setWindowTitle('Hanabi')
        self.show()

    def ShowThrowDeck(self):
        # 내 차례라면 창을 연다.
        if self.isTurn:
            print("Opening a Throw window...")
            # 플레이어 덱 정보를 넘겨야 하므로 gm.playerDecks 를 매개변수로 넣는다.
            self.w = AppThrowDeck(self.clientIndex, self.gm)
            self.w.setGeometry(QRect(700, 400, 300, 200))
            self.w.show()

    def ShowDropDeck(self):
        # 내 차례라면 창을 연다.
        if self.isTurn:
            print("Opening a Drop window...")
            self.w = AppDropDeck(self.clientIndex, self.gm)
            self.w.setGeometry(QRect(700, 400, 300, 200))
            self.w.show()

    def ShowGiveHint(self):
        # 내 차례라면 창을 연다.
            if self.isTurn:
                print("Opening a GiveHint window...")
                # 플레이어 덱 정보를 넘겨야 하므로 gm.playerDecks 를 매개변수로 넣는다.
                self.w = AppGiveHint(self.clientIndex, self.gm)
                self.w.setGeometry(QRect(700, 400, 300, 200))
                self.w.show()

    def clickedGiveHint(self):
        # 내 차례라면 창을 연다.
        if self.isTurn:
            winGiveHint = GiveHint()
            winGiveHint.show()


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
    def __init__(self, clientIndex, gm):
        QWidget.__init__(self)
        self.gm = gm

        self.playerDeck = self.gm.playerDecks[clientIndex]
        self.buttonGroup = QButtonGroup()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('버리기')
        deck0 = QPushButton("??")
        deck1 = QPushButton("??")
        deck2 = QPushButton("??")
        deck3 = QPushButton("??")

        self.buttonGroup.buttonClicked[int].connect(self.discardCard)
        self.buttonGroup.addButton(deck0, 0)
        self.buttonGroup.addButton(deck1, 1)
        self.buttonGroup.addButton(deck2, 2)
        self.buttonGroup.addButton(deck3, 3)

        for button in self.buttonGroup.buttons():
            SetCardDesign("mine", button)
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

    def discardCard(self, id):
        '''
        :param id: 몇 번째 카드를 버릴 건지
        :return: 버릴 카드 정보 반환
        '''
        for button in self.buttonGroup.buttons():
            if button is self.buttonGroup.button(id):
                print("{}번 플레이어가 {}번째 카드를 버렸습니다.".format(self.gm.clientIndex, id + 1))
                self.gm.clientIndex += 1
        self.gm.nextTurn()


#카드 내기 창
class AppDropDeck(QWidget):
    def __init__(self, clientIndex, gm):
        QWidget.__init__(self)
        self.gm = gm
        self.playerNum = clientIndex
        self.deckGroup = QButtonGroup()
        self.buttonGroup = QButtonGroup()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("카드 내기")
        deck0 = QPushButton("??")
        deck1 = QPushButton("??")
        deck2 = QPushButton("??")
        deck3 = QPushButton("??")

        self.buttonGroup.buttonClicked[int].connect(self.playCard)
        self.buttonGroup.addButton(deck0, 0)
        self.buttonGroup.addButton(deck1, 1)
        self.buttonGroup.addButton(deck2, 2)
        self.buttonGroup.addButton(deck3, 3)

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

        SetCardDesign("mine", deck0)
        SetCardDesign("mine", deck1)
        SetCardDesign("mine", deck2)
        SetCardDesign("mine", deck3)

        self.setLayout(layout1)

    def playCard(self, id):
        '''
                :param id: 몇 번째 카드를 버릴 건지
                :return: 버릴 카드 정보 반환
                '''
        for button in self.buttonGroup.buttons():
            if button is self.buttonGroup.button(id):
                print("{}번 플레이어가 {}번째 카드를 냈습니다.".format(self.playerNum, id + 1))


# 힌트주기 창
class AppGiveHint(QWidget):
    def __init__(self, clientIndex, gm):
        QWidget.__init__(self)
        self.clientIndex = clientIndex
        self.gm = gm
        self.playerNum = 0
        self.buttonGroup = QButtonGroup()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('힌트 주기')
        cob = QComboBox(self)
        # 아이디를 서버에서 받아야겠다
        player1 = "0번의 아이디"
        player2 = "1번의 아이디"
        player3 = "2번의 아이디"
        player4 = "3번의 아이디"
        playerList = [player1, player2, player3, player4]
        for i, player in enumerate(playerList):
            if i == self.clientIndex:
                continue
            cob.addItem(player)
        self.buttonGroup.buttonClicked[int].connect(self.giveHint)
        cob.activated[str].connect(self.onActivated)
        layout2 = QHBoxLayout()
        self.deck0 = QLabel(str(self.gm.playerDecks[self.playerNum].getCardOrNone(0)))
        self.deck1 = QLabel(str(self.gm.playerDecks[self.playerNum].getCardOrNone(1)))
        self.deck2 = QLabel(str(self.gm.playerDecks[self.playerNum].getCardOrNone(2)))
        self.deck3 = QLabel(str(self.gm.playerDecks[self.playerNum].getCardOrNone(3)))

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

        SetCardDesign(self.gm.playerDecks[self.playerNum].getCardOrNone(0).getColor(), self.deck0)
        SetCardDesign(self.gm.playerDecks[self.playerNum].getCardOrNone(1).getColor(), self.deck1)
        SetCardDesign(self.gm.playerDecks[self.playerNum].getCardOrNone(2).getColor(), self.deck2)
        SetCardDesign(self.gm.playerDecks[self.playerNum].getCardOrNone(3).getColor(), self.deck3)

        btnNumber1 = QPushButton("1")
        btnNumber2 = QPushButton("2")
        btnNumber3 = QPushButton("3")
        btnNumber4 = QPushButton("4")
        btnNumber5 = QPushButton("5")

        self.buttonGroup.addButton(btnNumber1, 0)
        self.buttonGroup.addButton(btnNumber2, 1)
        self.buttonGroup.addButton(btnNumber3, 2)
        self.buttonGroup.addButton(btnNumber4, 3)
        self.buttonGroup.addButton(btnNumber5, 4)

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

        self.buttonGroup.addButton(btnColorR, 5)
        self.buttonGroup.addButton(btnColorG, 6)
        self.buttonGroup.addButton(btnColorB, 7)
        self.buttonGroup.addButton(btnColorY, 8)
        self.buttonGroup.addButton(btnColorW, 9)
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

    def giveHint(self, id):
        '''
        :return: 힌트에 대한 정보를 줄 것. 플레이어 번호 + 힌트를 str로 넘긴다.
        '''
        for button in self.buttonGroup.buttons():
            if button is self.buttonGroup.button(id):
                print("{}번째 플레이어에게 {}로 힌트를 주었습니다.".format(self.playerNum, button.text()))
                self.clientIndex = (self.clientIndex + 1) % 4
                self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = HanabiGui()
    myWindow.show()
    app.exec_()