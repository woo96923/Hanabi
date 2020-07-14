class Hint:

    def __init__(self, info):
        """
        :param info: 색과 숫자 힌트. 문자열 혹은 숫자를 받을 수 있도록 자료형을 명시하지 않았음
        """
        assert info == "R" or info == "G" or info == "B" or info == "W" or info == "Y" \
            or info == 1 or info == 2 or info == 3 or info == 4 or info == 5, "invalid card information"

        self.info = info

    def isNumber(self):
        return type(self.info) == int

    def isColor(self):
        return type(self.info) == str


class Card:

    def __init__(self, color: str, number: int):
        """
        :param color: 카드의 색
        :param number: 카드의 숫자
        """
        assert color == "R" or color == "G" or color == "B" or color == "W" or color == "Y", "invalid card color"
        assert 1 <= number <= 5, "invalid card number"
        self.__color = color
        self.__number = number

    def getColor(self):
        return self.__color

    def getNumber(self):
        return self.__number

    def isCorrespondedHint(self, hint: Hint):
        return self.__color == hint.info or self.__number == hint.info


class Action:

    def __init__(self, actionType: int, playerIndex: int, element):
        """
        :param actionType: Action의 타입을 의미 1-내려놓기 / 2-버리기 / 3-힌트주기
        :param playerIndex: Action을 수행하는 플레이어의 색인(1,2) / 힌트를 받을 플레이어의 색인(3)
        :param element: 내고자 하는 카드의 색인(1,2 cardIndex: int), 힌트 객체(3 hint: Hint)
        """
        assert 1 <= actionType <= 3, "invalid action type"

        self.__actionType = actionType
        self.__playerIndex = playerIndex
        if actionType == 3:
            assert type(element) == Hint, "invalid element. Element should be Hint class when actionType is 3"
            self.__hint = element
        else:
            assert type(element) == int, "invalid element.Element should be integer when actionType is 1or2"
            assert 0 <= element <= 3, "invalid card index."
            self.__cardIndex = element

    def getActionType(self):
        return self.__actionType

    def getPlayerIndex(self):
        return self.__playerIndex

    def getHint(self):
        # getActionType()을 통해 메소드를 호출 할 수 있는지 확인하고 호출 할 것
        assert self.__actionType == 3
        return self.__hint

    def getCardIndex(self):
        # getActionType()을 통해 메소드를 호출 할 수 있는지 확인하고 호출 할 것
        assert self.__actionType != 3
        return self.__cardIndex


#     기능 테스트      #
def test___():
    h = Hint("R")
    h = Hint("G")
    h = Hint("B")
    h = Hint("W")
    h = Hint("Y")
    assert not h.isNumber()
    assert h.isColor()
    h = Hint(1)
    h = Hint(2)
    h = Hint(3)
    h = Hint(4)
    h = Hint(5)
    assert h.isNumber()
    assert not h.isColor()
    # h = Hint("K")
    # h = Hint(6)
    # h = Hint(0)

    colors = ["R", "G", "B", "W", "Y"]

    for i in range(5):
        for color in colors:
            c = Card(color, i + 1)

    # c = Card("J", 1)
    # c = Card("R", 6)

    for i in range(1, 3):
        for j in range(5):
            for k in range(4):
                a = Action(i, j, k)
    assert a.getCardIndex() == 3
    # a.getHint()

    for j in range(5):
        a = Action(3, j, h)
    # a.getCardIndex()
    assert a.getHint().info == 5

    # a = Action(3, 3, 4)

    print("Test Over")
