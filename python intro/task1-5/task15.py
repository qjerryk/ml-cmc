from typing import List
import itertools

def hello(name:str=None) -> str:
    res = ""
    if name is not None and name:
        res = f"Hello, {name}!"
    else:
        res = "Hello!"
    return res

def int_to_roman(num: int) -> str:
    ans = ""
    dict = {1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'}

    while num:
        for digit in list(dict.keys()):
            if num - digit >= 0:
                ans += dict[digit]
                num -= digit
                break

    return ans



def longest_common_prefix(strs_input: List[str]) -> str:
    if not strs_input:
        return ""

    pos = 0
    offset = [0] * len(strs_input)
    for j in range(len(strs_input)):
        k = 0
        while k < len(strs_input[j]) and strs_input[j][k] in [' ', '\n', '\t']:
            k += 1
        offset[j] = k

    flag = False
    for i in range(min(list(map(len, strs_input)))):
       pos = i
       flag = False
       for j in range(len(strs_input)):
           if offset[j] + i >= len(strs_input[j]) or strs_input[j][offset[j] + i] != strs_input[0][offset[0] + i]:
               flag = True
               break
       if flag:
           break
    if not flag:
        pos+=1
    return strs_input[0][offset[0]:offset[0]+pos]

def primes(N:int=50) -> int:
    last = 0
    while True:
        primeNums = [1]*N
        primeNums[0] = 0
        primeNums[1] = 0
        for i in range(2, N):
            if primeNums[i]:
                j = 2
                while j * i < N:
                    primeNums[j * i] = 0
                    j += 1
                if i > last:
                    yield i
                last = max(last, i)
        N *= 2


class BankCard:
    def __init__(self, total_sum: int, balance_limit: int=float('inf')):
        self.total_sum = total_sum
        self.balance_limit = balance_limit
        #self.balance()

    def __call__(self, sum_spent):
        """
        sum_spent - сумма, которую студент хочет потратить; при таком
        обращении sum_spent вычитается из текущей total_sum; если
        такой суммы на карте нет, требуется бросить исключение
        ValueError и напечатать "Not enough money to spend sum_spent dollars.".
        Если попытка снятия денег была успешной, следует написать: You spent sum_spent dollars.
        """
        if self.total_sum - sum_spent < 0:
            raise ValueError(f"Not enough money to spend {sum_spent} dollars.")
        self.total_sum -= sum_spent
        print(f'You spent {sum_spent} dollars.')

    def __str__(self):
        """
        при вызове функции print от объекта класса должно выводиться
        следующее сообщение "To learn the balance call balance."
        a.balance # при таком вызове количество вызовов баланса карты
        должно увеличиваться на 1, а возвращаться должна total_sum; если
        лимит операций по количеству просмотров баланса превышен,
        требуется бросить исключение ValueError и напечатать "Balance check limits exceeded."
        """
        return "To learn the balance call balance."

    @property
    def balance(self):
        self.balance_limit-=1
        if self.balance_limit < 0:
            raise ValueError("Balance check limits exceeded.")
        return self.total_sum

    def put(self, sum_put):
        self.total_sum += sum_put
        print(f'"You put {sum_put} dollars."')

    def __add__(self, other):
        return BankCard(self.total_sum + other.total_sum, max(self.balance_limit, other.balance_limit))

#print(  longest_common_prefix([[" ML;", "\t\t\tML", "\n \tML"], "ML"]))
a.balance