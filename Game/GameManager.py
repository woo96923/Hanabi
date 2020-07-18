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
        self.lastPlayerIndex = -1

        self.__hintToken = 10
        self.__lifeToken = 3

        self.cards = cards

        self.__redPlayedCards = []
        self.__greenPlayedCards = []
        self.__bluePlayedCards = []
        self.__whitePlayedCards = []
        self.__yellowPlayedCards = []

        # self.discardedCards = []
        self.__redDiscardedCards = []
        self.__greenDiscardedCards = []
        self.__blueDiscardedCards = []
        self.__whiteDiscardedCards = []
        self.__yellowDiscardedCards = []

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

    def distributeCards(self):
        for i in range(4):
            for j in range(4):
                self.giveOneCard(j)

    def decreaseHintToken(self):
        assert self.__hintToken != 0, "can't decrease hint token"
        self.__hintToken -= 1

    def increaseHintToken(self):
        if self.__hintToken < 8:
            self.__hintToken += 1

    def decreaseLifeToken(self):
        assert self.__lifeToken > 0, "life can't be negative value"
        self.__lifeToken -= 1

    def nextTurn(self):
        self.currentPlayerIndex = (self.currentPlayerIndex + 1) % 4
        if self.lastPlayerIndex == self.currentPlayerIndex:
            self.onGameEnd()

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

    def getDiscardedCards(self, color: str):
        assert color == "R" or color == "G" or color == "B" or color == "W" or color == "Y", "invalid card color"

        if color == "R":
            return self.__redDiscardedCards
        elif color == "G":
            return self.__greenDiscardedCards
        elif color == "B":
            return self.__blueDiscardedCards
        elif color == "W":
            return self.__whiteDiscardedCards
        return self.__yellowDiscardedCards

    def doAction(self, action: Action):
        """
        Action을 수행하는 함수
        :param action: 수행할 동작
        """

        if action.getActionType() == 1:         # 카드내기 (Play)
            playerDeck = self.playerDecks[self.currentPlayerIndex]
            cardIndex = action.getCardIndex()

            card = playerDeck.getCardOrNone(cardIndex)
            playedCards = self.getPlayedCards(card.getColor())

            if card.getNumber() - 1 == len(playedCards):        # 해당색의 카드를 카드를 줄지어 낼 수 있는 경우
                playedCards.add(card)
            else:
                discardedCards = self.getDiscardedCards(card.getColor())
                discardedCards.addCard(card)
                self.decreaseLifeToken()

            playerDeck.useCard(cardIndex)

            if not self.isCardsEmpty():
                playerDeck.giveOneCard(self.currentPlayerIndex)
            else:
                if self.lastPlayerIndex < 0:
                    self.lastPlayerIndex = self.currentPlayerIndex

        elif action.getActionType() == 2:         # 버리기   (Discard)
            playerDeck = self.playerDecks[self.currentPlayerIndex]
            cardIndex = action.getCardIndex()

            card = playerDeck.getCardOrNone(cardIndex)
            discardedCards = self.getDiscardedCards(card.getColor())

            discardedCards.addCard(card)
            self.increaseHintToken()

            playerDeck.useCard(cardIndex)
            if not self.isCardsEmpty():
                playerDeck.giveOneCard(self.currentPlayerIndex)
            else:
                if self.lastPlayerIndex < 0:
                    self.lastPlayerIndex = self.currentPlayerIndex

        elif action.getActionType() == 3:         # 힌트주기
            targetIndex = action.getTargetIndex()
            correspondedIndexes = []

            for i in range(4):
                card = self.playerDecks[targetIndex].getCardOrNone(i)
                if card is not None:
                    if card.isCorrespondedHint(action.getHint):
                        correspondedIndexes.append(i)

            self.decreaseHintToken()
            self.deliverHintToUI(correspondedIndexes)

    def deliverHintToUI(self, cardIndexes: list):
        # 힌트를 받은 내용을 UI에게 넘겨주는 함수
        # 내용은 아직 미정
        self
        pass

    def calculateScore(self):
        pass

    def onGameEnd(self):
        # 실제론 이 함수에서 UI랑 서버쪽에 게임이 끝났다 알려야 할듯?
        print("게임 종료! 최종점수: %d점" % self.calculateScore())


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


gm = GameManager(initCards(), 0, 0)
gm.distributeCards()
