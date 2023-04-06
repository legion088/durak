from random import shuffle, choice


class Players:
    def __init__(self, name, cards) -> None:
        self.name = name
        self.cards = cards

    def throw_card(self, cards_table) -> object:
        """Подбрасываем карту"""
        cards_table = [
            player_card
            for player_card in self.cards
            for card_table in cards_table
            if player_card.value == card_table.value
        ]
        return None if not cards_table else choice(cards_table)

    def close_card(self, card1) -> object:
        """Отбиваемся"""
        for card2 in self.cards:
            if card1.equal_suit(card2) and card1.less(card2):
                return card2
            elif card1.value == card2.value and card1.less(card2):
                return card2

    def delete_card(self, card) -> None:
        """Удаляем карту"""
        self.cards.remove(card)

    def show_cards(self) -> str:
        """Показываем карты игрока"""
        return " ".join([card.to_str() for card in self.cards])


class Card:
    SUIT = ['♠', '♣', '♦', '♥']
    VALUE = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit
        self.amount = (
            self.VALUE.index(self.value),
            self.SUIT.index(self.suit)
        )

    def to_str(self) -> str:
        """Возвращает строковое представление карты в виде строки"""
        return f"{self.value}{self.suit}"

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
        if self.amount > card.amount:
            return True
        return False

    def less(self, card) -> bool:
        """Возвращает True если ли карта младше, чем карта в параметре"""
        if self.amount < card.amount:
            return True
        return False


class Deck:
    def __init__(self) -> None:
        self.cards = [
            Card(v, s) for v in Card.VALUE for s in Card.SUIT
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
        self.players = None
        self.deck = Deck()

    def info(self) -> None:
        """Выводим информацию о ходе игры"""
        for player in self.players:
            if len(player.cards) == 10:
                print(f"Карты {player.name} {player.show_cards()}")
            else:
                print(f"Осталось карт {player.name} {player.show_cards()}")
        print()

    def start_game(self, players=2) -> None:
        """Запускаем игру"""
        if players < 2 or players > 2:
            raise ValueError("Игра только для двух игроков!")

        self.deck.shuffle()
        self.players = [
            Players(f"Игрок {num}:", self.deck.draw(10))
            for num, pl in enumerate(range(players), start=1)
        ]
        player1, player2 = self.players
        self.deck.show()
        self.info()

        card1 = choice(player1.cards)
        step = 0
        while True:
            step += 1
            print(f"Ход {step}")
            print(player1.name, card1.to_str())
            card2 = player2.close_card(card1)

            if card2 is None:
                print(f"{player2.name} не смог покрыть\n{player1.name} выиграл")
                break
            print(player2.name, card2.to_str(), "(покрыл)")
            player1.delete_card(card1), player2.delete_card(card2)
            card1 = player1.throw_card([card1, card2])

            if not player1.cards or card1 is None:
                print(f"{player2.name} выиграл")
                break

            self.info()



if __name__ == '__main__':
    """Генерируем несколько случайных игр"""
    for n in range(1, 100):
        print(f"Случай {n}")
        print("=" * 50)
        Game().start_game(2)
        print()
