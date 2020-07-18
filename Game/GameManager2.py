from Game.GameElements import Hint as Hint
from Game.GameElements import Card as Card
from Game.GameElements import Action as Action
from Game.GameElements import PlayerDeck as PlayerDeck
import random


# 시작버튼을 누르면 서버에서 게임 시작시 정보를 받아 게임매니저를 생성하고 게임이 시작된다.
class GameManager:

    def __init__(self, cards: list, clientIndex: int, beginnerIndex: int):
        self.playerDecks = [PlayerDeck(), PlayerDeck(), PlayerDeck(), PlayerDeck()]
        self.clientIndex = clientIndex
        self.currentPlayerIndex = beginnerIndex

        self.cards = cards
        self.redDiscardedCards = []
        self.blueDiscardedCards = []
        self.greenDiscardedCards = []
        self.whiteDiscardedCards = []
        self.yellowDiscardedCards = []

        self.__hintToken = 8
        self.__lifeToken = 3

        self.__redPlayedCards = []
        self.__greenPlayedCards = []
        self.__bluePlayedCards = []
        self.__whitePlayedCards = []
        self.__yellowPlayedCards = []

    def nextTurn(self):
        # 턴을 넘기는 동작을 임의로 표현한 임시 함수!
        self.currentPlayerIndex = (self.currentPlayerIndex + 1) % 4

    def canPlayCard(self, card: Card):
        """
        해당 카드를 낼 수 있는지 판단하는 함수
        :param card: play 하려는 카드
        :return: play 가능하면 True, 불가능하면 False
        """
        playedCards = self.getPlayedCards(card.getColor())
        if len(playedCards) == card.getNumber() - 1:
            return True
        return False

    def getPlayedCards(self, color: str):
        assert color == "R" or color == "G" or color == "B" or color == "W" or color == "Y", "invalid card color"

        if color == "R":
            return self.__redPlayedCards
        elif color == "G":
            return self.__greenPlayedCards
        elif color == "B":
            return self.__bluePlayedCards
        elif color == "W":
            return self.__whitePlayedCards
        return self.__yellowPlayedCards

    def doAction(self, action: Action):
        """
        Action을 수행하는 함수
        :param action: 수행할 동작
        """

        playerDeck = self.playerDecks[self.currentPlayerIndex]
        cardIndex = action.getCardIndex()
        color = playerDeck.getCardOrNone(cardIndex).getColor()

        if actiontype == 2:
            if color == "R":
                self.redDiscardedCards.addCard(playerDeck[cardIndex])
                playerDeck.useCard(cardIndex)
                playerDeck.giveOneCard(self.currentPlayerIndex)
            elif color == "G":
                self.greenDiscardedCards.addCard(playerDeck[cardIndex])
                playerDeck.useCard(cardIndex)
                playerDeck.giveOneCard(self.currentPlayerIndex)
            elif color == "B":
                self.blueDiscardedCards.addCard(playerDeck[cardIndex])
                playerDeck.useCard(cardIndex)
                playerDeck.giveOneCard(self.currentPlayerIndex)
            elif color == "W":
                self.whiteDiscardedCards.addCard(playerDeck[cardIndex])
                playerDeck.useCard(cardIndex)
                playerDeck.giveOneCard(self.currentPlayerIndex)
            self.yellowDiscardedCards.addCard(playerDeck[cardIndex])
            playerDeck.useCard(cardIndex)
            playerDeck.giveOneCard(self.currentPlayerIndex)
        else :
            return False

    def distributeCards(self):
        assert self.cards != 0 "can't distribute card"

        for i in range(4):
            for j in self.playerDecks[i]:
                self.giveOneCard(j)
    #여기서 올릴껀 없긴해 내가 시호한테 보냈어 안올려져서 그냥 그럼 저기 깃헙으ㅔ 있는 코드랑 이 코드랑 다르긴 한 거지?ㅇㅇㅇㅇㅇㅇ이ㄱ
    def isCardsEmpty(self):
        # 카드더미가 비었는지 확인하는 함수
        return len(self.cards) == 0

    def giveOneCard(self, playerIndex: int):
        """
        카드더미 맨 위에서 카드를 뽑아 플레이어에게 주는 함수. isCardEmpty로 카드를 줄 수 있는지 검증하고 호출할 것
        :param playerIndex: 카드르 받을 플레이어의 색인
        """
        assert not self.isCardEmpty(), "cannot give card when have no cards"
        card = self.cards[0]
        del self.cards[0]       # pop()을 쓰면 한줄로 줄일 수도 있다.
        self.playerDecks[playerIndex].addCard(card)

    def decreseHintToken(self):
        assert self.__hintToken != 0, "can't decrease hint"

        self.__hintToken += 1

    def increaseHintToken(self):
        assert self.__hintToken != 8, "can't increase hint"

        self.__hintToken -= 1

    def decreaseLifeToken(self):
        assert self.__lifeToken != 0, "you die"

        self.__lifeToken -= 1

# 카드더미를 초기화하는 임시 함수. 통신이 추가되면 그 섞인 카드 정보를 받아 카드를 초기화 하는 함수로 바뀔 예정
def initCards():
    colors = ["R", "G", "B", "W", "Y"]
    counts = [3, 2, 2, 2, 1]
    cards = []

    for color in colors:
        for i in range(5):
            for j in range(counts[i]):
                cards.append(Card(color, i + 1))

    random.shuffle(cards)

    return cards


#   기능 테스트   #


gm = GameManager(initCards())
