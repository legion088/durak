# Колода карт


### Задание

1) Разработать класс для “колоды игральных карт” (см. описание ниже)

2) Использовать данный класс для моделирования одного шага игры в дурака между двумя игроками.
Игроки 1 и 2 получают по 10 карт из перетасованной колоды.
Игрок 1 кидает карту (карта выбирается случайным образом), игрок 2 пытается ее отбить более старшей картой (про старшинство карт читайте ниже).
Если игрок 2 отбился, то игрок 1 может подкинуть карту, значение которой такое же, как у одной из карт, лежащих на столе.
Игрок 2 отбивается повторно, игрок 1 подкидывает повторно и так до тех пор пока у игрока 1 не закончаться карты, которые можно подкинуть.
Если игрок 2 отбился, то он победил, иначе победил игрок 1.

3) В консоль вывести:
- какие карты получили игрок 1 и игрок 2
- ход игры (какие карты выбрасывались)
- результат игры

4) Задание выполнять на Python 3.7

### Колода

Колода состоит из 52 карт.

Значения карт: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A

Масти карт: ♥ ♦ ♣ ♠

Говоря “берем карту сверху колоды” подразумеваем получение карты с начала списка колоды.


#### Конструктор колоды

При создании новой колоды все карты должны находиться в отсортированном порядке - сначала идут все червы от 2-ки до туза, затем буби, крести и пики.


#### Методы колоды

*   метод **.shuffle**() - перемешивает колоду, располагая карты в случайном порядке.
*   метод .**draw**(x) - возвращает x первых карт из колоды в виде списка, эти карты **убираются** из колоды.
Уточнение: первую карту в списке считаем верхней картой колоды
*   метод .**show**() - отображает все карты колоды в формате: \
deck[12]: 3♥, 4♦, A♣, … \
где 12 - текущее кол-во карт в колоде.


### Карты

Карты в колоде тоже должны являться объектами - экземплярами класса Card


#### Конструктор карты

При создании конструктор карты принимает: значение карты и ее масть. \
**Примечание:**

Diamonds    Бубны

Hearts	    Червы

Spades	    Пики

Clubs       Трефы


#### Методы карты

*   .**to_str**() возвращает строковое представление карты в виде строки, формата:4♦
*   .**equal_suit**(card) - проверяет, одинаковые ли масти у карт \
Пример: \
card1.more(card2) → **True**, при card1(J♦) card2(10♦). 
*   .**more**(card) - возвращает True, если карта у которой вызван метод больше, чем карта которую передали в качестве параметра. \
**Пример**:  \
card1.more(card2) → **True**, при card1(J♦) card2(10♦). Валет больше(старше) 10-ки \
card1.more(card2) → **False**, при card1(4♦) card2(10♦). 4-ка не старше 10-ки
*   .**less**(card) - проверяет является ли карта младше, чем карта в параметре 


##### Нюансы сравнения карт

Если у карты больше(старше) значение, то она больше(старше). При равенстве значений, сравниваем масти. Старшинство мастей определяем следующее: ♥>♦>♣>♠


##### Вывод иконок карт в консоль

Пример вывода иконок в консоль:


```
print('\u2661', '\u2665')
print('\u2662', '\u2666')
print('\u2667', '\u2663')
print('\u2664', '\u2660')
```


\uxxxx - юникод символ. Полный список всех юникод символов можно взять [тут](https://unicode-table.com/ru/#basic-latin).

Юникод символы мастей игральных карт [тут](https://unicode-table.com/ru/search/?q=%D0%BC%D0%B0%D1%81%D1%82%D0%B8).


Пример вывода приложения:
Колода:
8♦, 7♠, К♠, 8♥, В♦, 5♠, 4♥, 6♦, В♥, 4♠, Т♠, 7♥, В♠, 9♦, 9♠, 2♠, 6♥, Т♥, 5♥, 7♦, К♦, Д♠, Т♣, 6♣, 8♣, 10♠, 2♦, Д♣, 10♣, Д♦, 6♠, К♥, 3♥, 4♣, В♣, Т♦, 7♣, 2♣, 3♣, 5♣, 9♣, 3♠, 3♦, 9♥, Д♥, К♣, 5♦, 8♠, 4♦, 2♥, 10♥, 10♦

Раздали первому игроку: 4♠ 4♥ 5♠ 6♦ 7♠ 8♦ 8♥ В♦ В♥ К♠
Раздали второму игроку: 2♠ 5♥ 6♥ 7♦ 7♥ 9♠ 9♦ В♠ Т♠ Т♥

Ход 1
Игрок 1: 4♠
Игрок 2: 9♠ (покрыл)

У первого игрока осталось: 4♥ 5♠ 6♦ 7♠ 8♦ 8♥ В♦ В♥ К♠
У второго игрока осталось: 2♠ 5♥ 6♥ 7♦ 7♥ 9♦ В♠ Т♠ Т♥

Ход 2
Игрок 1: 4♥
Игрок 2: 5♥ (покрыл)

У первого игрока осталось: 5♠ 6♦ 7♠ 8♦ 8♥ В♦ В♥ К♠
У второго игрока осталось: 2♠ 6♥ 7♦ 7♥ 9♦ В♠ Т♠ Т♥

Ход 3
Игрок 1: 5♠
Игрок 2: В♠ (покрыл)

У первого игрока осталось: 6♦ 7♠ 8♦ 8♥ В♦ В♥ К♠
У второго игрока осталось: 2♠ 6♥ 7♦ 7♥ 9♦ Т♠ Т♥

Ход 4
Игрок 1: В♦
Игрок 2: не смог покрыть

Игрок 1 выиграл.
