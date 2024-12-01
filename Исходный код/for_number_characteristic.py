import math
import numpy


def nice_view(s: list):
    m = {}
    for element in s:
        if m.get(element) is None:
            m[element] = 1
        else:
            m[element] += 1
    result = []
    for number, degree in m.items():
        result += [str(number) + '^' + str(degree)]
    return ' * '.join(result)


class NotNaturalNumberError(Exception):
    pass


class ToBigNumber(Exception):
    pass


class Number:
    def __init__(self, string_number):
        self.number = int(string_number)
        if self.number <= 0:
            raise NotNaturalNumberError
        if self.number > 10 ** 7:
            raise ToBigNumber

    def count_of_numbers(self):
        return str(len(str(self.number)))

    def amount_of_numbers(self):
        return str(sum(list(map(int, str(self.number)))))

    def product_of_number(self):
        product = 1
        for num in list(map(int, str(self.number))):
            if num != 0:
                product *= num
        if self.number == 0:
            return 0
        return str(product)

    def dividers(self):
        num = self.number
        primal_dividers = []
        dividers = []
        result = []
        if num == 1:
            return ['1', '1', '1',  'Нет', 'Нет']

        div = 2
        while num != 1:
            while num % div == 0:
                primal_dividers += [div]
                num //= div
            div += 1

        result.append(primal_dividers)
        primal_dividers.append(1)

        for div in range(1, self.number // 2 + 1):
            if self.number % div == 0:
                dividers += [div]
        dividers += [self.number]

        result.append(dividers)
        result.append(len(dividers))
        if len(dividers) == 2:
            result.append('Да')
        else:
            result.append('Нет')

        if len(dividers) == 4:
            result.append('Да')
        else:
            result.append('Нет')
        primal_dividers.sort()
        primal_dividers.remove(1)
        dividers.sort()
        primal_dividers = nice_view(primal_dividers)
        dividers = list(map(str, dividers))

        answer = [primal_dividers, ' '.join(dividers), str(len(dividers)), result[3], result[4]]
        return answer

    def is_square(self):
        if int(math.sqrt(self.number)) == float(math.sqrt(self.number)):
            return f'Да, {int(math.sqrt(self.number))}'
        return 'Нет'

    def is_cube(self):
        if int(numpy.cbrt(self.number)) == float(numpy.cbrt(self.number)):
            return f'Да, {int(numpy.cbrt(self.number))}'
        return 'Нет'

    def square_root(self):
        return str(math.sqrt(self.number))

    def cubic_root(self):
        return str(numpy.cbrt(self.number))

    def is_fibonacci(self):
        x = (5 * self.number ** 2 + 4)
        y = (5 * self.number ** 2 - 4)
        if int(math.sqrt(x)) == float(math.sqrt(x)):
            return 'Да'
        if int(math.sqrt(y)) == float(math.sqrt(y)):
            return 'Да'
        return 'Нет'

    def is_katalan(self):
        katalan_number = 1
        index = 0
        while katalan_number < self.number:
            katalan_number = math.factorial(2 * index) / (math.factorial(index) * math.factorial(index + 1))
            index += 1
        if self.number == katalan_number:
            return 'Да'
        else:
            return 'Нет'

    def is_mersen(self):
        mersen_number = 0
        index = 1
        while mersen_number < self.number:
            mersen_number = 2 ** index - 1
            index += 1
        if self.number == mersen_number:
            return 'Да'
        else:
            return 'Нет'

    def sin(self):
        return str(math.sin(math.radians(self.number)))


    def cos(self):
        return str(math.cos(math.radians(self.number)))

    def tan(self):
        return str(math.tan(math.radians(self.number)))


    def ctg(self):
        return str(1 / math.tan(math.radians(self.number)))

    def decimal_logarithm(self):
        return str(math.log10(self.number))

    def natural_logarithm(self):
        return str(math.log(self.number, math.e))


    def bin_view(self):
        return str(bin(self.number))[2:]

    def oct_view(self):
        return str(oct(self.number))[2:]

    def hex_view(self):
        return str(hex(self.number))[2:]

    def max_number(self):
        return str(max(list(str(self.number))))

    def min_number(self):
        return str(min(list(str(self.number))))
