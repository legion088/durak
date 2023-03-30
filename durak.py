from random import shuffle


class Players:
    def __init__(self, name, cards) -> None:
        self.name = name
        self.cards = cards

    def delete_card(self, card) -> None:
        """Удаляем карту"""
        cards = self.cards.copy()
        cards.remove(card)
        self.cards = cards

    def show_cards(self) -> str:
        """Показываем карты игрока"""
        return " ".join([card.to_str() for card in self.cards])


class Card:
    SUIT = ['♠', '♣', '♦', '♥']
    VALUE = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit

    def to_str(self) -> str:
        """Возвращает строковое представление карты в виде строки"""
        return "{}{}".format(self.VALUE[self.value],
                             self.SUIT[self.suit])

    def equal_suit(self, card) -> bool:
        """Проверяет, одинаковые ли масти у карт"""
        if not self.suit == card.suit:
            return False
        return True

    def more(self, card) -> bool:
        """
        Возвращает True, если карта у которой вызван метод больше,
        чем карта которую передали в качестве параметра
        """
        if self.value > card.value:
            return True
        if self.value == card.value:
            if self.suit > card.suit:
                return True
        return False

    def less(self, card) -> bool:
        """Возвращает True если ли карта младше, чем карта в параметре"""
        if self.value < card.value:
            return True
        if self.value == card.value:
            if self.suit < card.suit:
                return True
        return False


class Deck:
    def __init__(self) -> None:
        self.cards = [
            Card(value, suit) for value in range(2, 15) for suit in range(4)
        ]

    def shuffle(self) -> None:
        """Перемешивает колоду, располагая карты в случайном порядке"""
        shuffle(self.cards)

    def draw(self, x) -> list:
        """
        Возвращает x первых карт из колоды в виде списка, эти карты убираются из колоды.
        Уточнение: первую карту в списке считаем верхней картой колоды
        """
        cards = self.cards[:x]
        self.cards = [c for c in self.cards if c not in cards]
        return cards

    def show(self) -> None:
        """Отображает все карты колоды в формате"""
        cards = ["{}".format(card.to_str()) for card in self.cards]
        print("deck[{}]: {}".format(len(cards), cards))


class Game:
    def __init__(self) -> None:
        self.deck = Deck()
        self.players = None

    def info(self) -> None:
        """Выводим информацию о ходе игры"""
        for player in self.players:
            if len(player.cards) == 6:
                print(f"Карты {player.name} {player.show_cards()}")
            else:
                print(f"Осталось карт {player.name} {player.show_cards()}")


    def start_game(self, players=2) -> None:
        """Запускаем игру"""
        if players < 2 or players > 2:
            raise ValueError("Игра только для двух игроков!")

        self.deck.shuffle()
        self.players = [
            Players(f"Игрок {num}:", self.deck.draw(6))
            for num, pl in enumerate(range(players), start=1)
        ]

        player1, player2 = self.players

        self.deck.show()
        self.info()
        print()

        for step, card1 in enumerate(player1.cards, start=1):
            player1.delete_card(card1)
            print(f"Ход {step}\n{player1.name} {card1.to_str()}")

            for card2 in player2.cards:
                if card1.equal_suit(card2) and card1.less(card2):
                    print(f"{player2.name} {card2.to_str()} (покрыл)")
                    player2.delete_card(card2)
                    self.info()
                    break
            else:
                print(f"{player2.name} не смог покрыть\n{player1.name} выиграл.")
                break
            print()


if __name__ == '__main__':
    """Генерируем несколько случайных игр"""
    for n in range(1, 10):
        print(f"Случай {n}")
        print("=" * 200)
        Game().start_game(players=2)
        print()
