class Hint:
    pass


class Action:

    def __init__(self, actionType: int, playerIndex: int, cardIndex: int):
        """
        액션 타입 1,2에 대응하는 생성자
        :param actionType: Action의 타입을 의미 1-내려놓기 / 2-버리기 / 3-힌트주기
        :param playerIndex: Action을 수행하는 플레이어의 색인
        :param cardIndex: 내고자 하는 카드의 색인
        """

        self.__actionType = actionType
        self.__playerIndex = playerIndex
        self.__hint = cardIndex

    def __init__(self, actionType: int, playerIndex: int, hint: Hint):
        """
        액션 타입 3에 대응하는 생성자
        :param actionType: Action의 타입을 의미 1-내려놓기 / 2-버리기 / 3-힌트주기
        :param playerIndex: 힌트를 받을 플레이어의 색인
        :param hint: 힌트 객체
        """
        self.__actionType = actionType
        self.__playerIndex = playerIndex
        self.__hint = hint

    def getActionType(self):
        return self.__actionType

    def getPlayerIndex(self):
        return self.__playerIndex

    def getHint(self):
        return self.__hint

    def getCardIndex(self):
        return self.getCardIndex()
