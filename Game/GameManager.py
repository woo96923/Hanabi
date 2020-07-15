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
        self.discardedCards = []

        self.__hintToken = 10
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
        pass


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
