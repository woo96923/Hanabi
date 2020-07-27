import sys
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


        #표시된 카드 교체 (버리고 새카드/ 내고 새카드)
        deck = ["R2", "B4", "W1", "B1"]#player 2가 가지고 있는 deck 샘플?
        newDeck = "R1"#새로 가져올 카드 샘플
        #만약 0번쨰 리스트를 버린다면
        changePlayer2Deck0=1
        if changePlayer2Deck0:
            self.player2Deck0.setText(newDeck)
            deck[0] = newDeck
            print(deck)



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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = HanabiGui()
    myWindow.show()
    app.exec_()