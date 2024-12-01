import math
import statistics
from for_number_characteristic import Number


class Pair:
    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2

    def lcm(self):
        try:
            return str(math.lcm(self.number1, self.number2))
        except ZeroDivisionError:
            return '—————'

    def gcd(self):
        try:
            return str(math.gcd(self.number2, self.number1))
        except ZeroDivisionError:
            return '—————'

    def common_dividers(self):
        try:
            num = Number(self.gcd())
            return str(num.dividers()[1])
        except ZeroDivisionError:
            return '—————'

    def amount(self):
        return str(self.number1 + self.number2)

    def product(self):
        return str(self.number1 * self.number2)

    def divide_1(self):
        try:
            return str(self.number1 / self.number2)
        except ZeroDivisionError:
            return '—————'

    def divide_2(self):
        try:
            return str(self.number2 / self.number1)
        except ZeroDivisionError:
            return '—————'

    def difference(self):
        return str(abs(self.number1 - self.number2))

    def arithmetic_mean(self):
        return str((self.number1 + self.number2) / 2)

    def geometric_mean(self):
        try:
            return str(statistics.geometric_mean([self.number2, self.number1]))
        except statistics.StatisticsError:
            return '—————'

    def harmonic_mean(self):
        try:
            return str(statistics.harmonic_mean([self.number2, self.number1]))
        except statistics.StatisticsError:
            return '—————'

    def common_numbers(self):
        a = set(list(str(self.number1)))
        b = set(list(str(self.number2)))
        c = list(a & b)
        c.sort()
        if c:
            return ' '.join(c)
        else:
            return '———'
