import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon
from PyQt5.QtCore import Qt, QRect
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
        #배경 사진 넣기
        background = QImage("background.jpeg")
        palette = QPalette()
        palette.setBrush(10, QBrush(background))
        self.setPalette(palette)
        self.btnGiveHint.clicked.connect(self.clickedGiveHint)
        self.deckList = [[self.player0Deck0, self.player0Deck1, self.player0Deck2, self.player0Deck3],
                         [self.player1Deck0, self.player1Deck1, self.player1Deck2, self.player1Deck3],
                         [self.player2Deck0, self.player2Deck1, self.player2Deck2, self.player2Deck3],
                         [self.player3Deck0, self.player3Deck1, self.player3Deck2, self.player3Deck3]]

        self.btnThrow.clicked.connect(self.ShowThrowDeck)
        self.btnDrop.clicked.connect(self.ShowDropDeck)
        self.btnGiveHint.clicked.connect(self.ShowGiveHint)

        #버린 카드 개수표
        throwDeck = 1
        deckInfo = "B2"
        throwB2 = 0#버려진 B2개수, game에서 정한 리스트 있을 것 같아서 그거 갖구오려고 대충 지었어요
        if throwDeck:
            if deckInfo =="B2":
                throwB2 = throwB2 + 1
                printthrowB2 = "%d" %throwB2
                self.throwB2.setText(printthrowB2)

        #카드 가져오기. 낸경우+버린경우
        getDeck =1#가져와야하는경우1
        remainDeck = 10#남은 카드수
        if getDeck:
            remainDeck = remainDeck -1
            printRemainDeck = "남은카드\n%d" %remainDeck
            self.remainDeck.setText(printRemainDeck)
            getDeck=0

        number = 1
        color = "WHITE"
        hintCategory =1#숫자 힌트면 0 색 힌트면 1
        if hintCategory == 0:
            hint = "카드 번호가 %d" % number
        if hintCategory == 1:
            hint = " 카드 색이 %s" % color
        presentPlayer = 3
        pickedPlayer = 2
        giveHint = "player%d 가 player%d에게 힌트를 주었습니다.\n;%s" % (presentPlayer, pickedPlayer, hint)
        self.notice.setText(giveHint)





        #힌트 삭제, 생성
        life =3#남은 생명
        loseLife=1#life 잃은 경우 1 외엔 0
        hint = 8#남은 힌트
        giveHint = 1#힌트 주면 1 나머지경우 0
        throwDeck = 1#카드버림
        if loseLife:
            if life ==3:
                self.lifeToken2.setText("X")
            elif life == 2 :
                self.hintToken1.setText("X")
            elif life ==1:
                self.lifeToken0.setText("X")
                print("GAMEOVER")
            loseLife=0
            life = life - 1

        if throwDeck &(hint<8):
            if hint ==7:
                self.hintToken7.setText("O")
            elif hint ==6:
                self.hintToken6.setText("O")
            elif hint == 5 :
                self.hintToken5.setText("O")
            elif hint ==4:
                self.hintToken4.setText("O")
            elif hint ==3:
                self.hintToken3.setText("O")
            elif hint == 2 :
                self.hintToken2.setText("O")
            elif hint ==1:
                self.hintToken1.setText("O")
            elif hint ==0:
                self.hintToken0.setText("O")
            throwDeck=0
            hint = hint + 1

        if giveHint & (hint >0):
            if hint == 8:
                self.hintToken7.setText("X")
            elif hint ==7:
                self.hintToken6.setText("X")
            elif hint ==6:
                self.hintToken5.setText("X")
            elif hint == 5 :
                self.hintToken4.setText("X")
            elif hint ==4:
                self.hintToken3.setText("X")
            elif hint ==3:
                self.hintToken2.setText("X")
            elif hint == 2 :
                self.hintToken1.setText("X")
            elif hint ==1:
                self.hintToken0.setText("X")
            hint = hint-1
            giveHint=0





        #mainboard에 카드 내려놓기 과정
        getScore = 1 #점수 얻으면 1
        #테스트용 반복문
        for i in range(5):
            if i ==0:
                dropDeck="G1"#낸 카드 ? 이름 못짓겠어요ㅠㅠ
            elif i==1:
                dropDeck="G2"
            elif i==2:
                dropDeck="G3"
            elif i==3:
                dropDeck="G4"
            else:
                dropDeck="G5"
            #다음 분류는 Deck 정보 저장된 형식에 따라 바뀔 수 있어요! (실행 내용은 바뀌지 않음
            if getScore:
                if dropDeck =="R1":
                    self.mainR2.setStyleSheet("background-color : rgb(255, 79, 79);"
                                              "border-width: 2px;"
                                              "border-style : solid;"
                                              "border-radius: 20px;"
                                              "border-color : rgb(0, 0, 0)"
                                              )
                    self.mainR2.setText(dropDeck)
                elif dropDeck =="R2":
                    self.mainR2.setStyleSheet("background-color : rgb(255, 79, 79);"
                                              "border-width: 2px;"
                                              "border-style : solid;"
                                              "border-radius: 20px;"
                                              "border-color : rgb(0, 0, 0)"
                                              )
                    self.mainR2.setText(dropDeck)
                elif dropDeck =="R3":
                    self.mainR3.setStyleSheet("background-color : rgb(255, 79, 79);"
                                              "border-width: 2px;"
                                              "border-style : solid;"
                                              "border-radius: 20px;"
                                              "border-color : rgb(0, 0, 0)"
                                              )
                    self.mainR3.setText(dropDeck)
                elif dropDeck =="R4":
                    self.mainR4.setStyleSheet("background-color : rgb(255, 79, 79);"
                                              "border-width: 2px;"
                                              "border-style : solid;"
                                              "border-radius: 20px;"
                                              "border-color : rgb(0, 0, 0)"
                                              )
                    self.mainR4.setText(dropDeck)
                elif dropDeck =="R5":
                    self.mainR5.setStyleSheet("background-color : rgb(255, 79, 79);"
                                              "border-width: 2px;"
                                              "border-style : solid;"
                                              "border-radius: 20px;"
                                              "border-color : rgb(0, 0, 0)"
                                              )
                    self.mainR5.setText(dropDeck)
                elif dropDeck =="G1":
                    self.mainG1.setStyleSheet("background-color : rgb(11, 222, 0);"
                                              "border-width: 2px;"
                                              "border-style : solid;"
                                              "border-radius: 20px;"
                                              "border-color : rgb(0, 0, 0)")
                    self.mainG1.setText(dropDeck)
                elif dropDeck =="G2":
                    self.mainG2.setStyleSheet("background-color : rgb(11, 222, 0);"
                                              "border-width: 2px;"
                                              "border-style : solid;"
                                              "border-radius: 20px;"
                                              "border-color : rgb(0, 0, 0)")
                    self.mainG2.setText(dropDeck)
                elif dropDeck =="G3":
                    self.mainG3.setStyleSheet("background-color : rgb(11, 222, 0);"
                                              "border-width: 2px;"
                                              "border-style : solid;"
                                              "border-radius: 20px;"
                                              "border-color : rgb(0, 0, 0)")
                    self.mainG3.setText(dropDeck)
                elif dropDeck =="G4":
                    self.mainG4.setStyleSheet("background-color : rgb(11, 222, 0);"
                                              "border-width: 2px;"
                                              "border-style : solid;"
                                              "border-radius: 20px;"
                                              "border-color : rgb(0, 0, 0)")
                    self.mainG4.setText(dropDeck)
                elif dropDeck =="G5":
                    self.mainG5.setStyleSheet("background-color : rgb(11, 222, 0);"
                                              "border-width: 2px;"
                                              "border-style : solid;"
                                              "border-radius: 20px;"
                                              "border-color : rgb(0, 0, 0)")
                    self.mainG5.setText(dropDeck)



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
        self.w = AppGiveHint()
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
    def __init__(self):
        QWidget.__init__(self)
    def paintEvent(self, e):
        self.setWindowTitle('힌트 주기')
        cob = QComboBox(self)
        player1 = "일번의 아이디"
        player2 = "이번의 아이디"
        player3 = "삼번의 아이디"
        cob.addItem(player1)
        cob.addItem(player2)
        cob.addItem(player3)

        deck0 = QLabel(playerDeck[0])
        deck1 = QLabel(playerDeck[1])
        deck2 = QLabel(playerDeck[2])
        deck3 = QLabel(playerDeck[3])
        layout2 = QHBoxLayout()
        layout2.addWidget(deck0)
        layout2.addWidget(deck1)
        layout2.addWidget(deck2)
        layout2.addWidget(deck3)
        deck0.setMinimumHeight(160)
        deck1.setMinimumHeight(160)
        deck2.setMinimumHeight(160)
        deck3.setMinimumHeight(160)
        deck0.setMaximumWidth(140)
        deck1.setMaximumWidth(140)
        deck2.setMaximumWidth(140)
        deck3.setMaximumWidth(140)
        deck0.setAlignment(Qt.AlignCenter)
        deck1.setAlignment(Qt.AlignCenter)
        deck2.setAlignment(Qt.AlignCenter)
        deck3.setAlignment(Qt.AlignCenter)

        SetCardDesign(playerDeck[0][0], deck0)
        SetCardDesign(playerDeck[1][0], deck1)
        SetCardDesign(playerDeck[2][0], deck2)
        SetCardDesign(playerDeck[3][0], deck3)

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