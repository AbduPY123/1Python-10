'''1. Р РµР°Р»РёР·РѕРІР°С‚СЊ РєР»Р°СЃСЃ Matrix (РјР°С‚СЂРёС†Р°). РћР±РµСЃРїРµС‡РёС‚СЊ РїРµСЂРµРіСЂСѓР·РєСѓ РєРѕРЅСЃС‚СЂСѓРєС‚РѕСЂР° РєР»Р°СЃСЃР°
(РјРµС‚РѕРґ init()), РєРѕС‚РѕСЂС‹Р№ РґРѕР»Р¶РµРЅ РїСЂРёРЅРёРјР°С‚СЊ РґР°РЅРЅС‹Рµ (СЃРїРёСЃРѕРє СЃРїРёСЃРєРѕРІ) РґР»СЏ С„РѕСЂРјРёСЂРѕРІР°РЅРёСЏ
РјР°С‚СЂРёС†С‹.
РџРѕРґСЃРєР°Р·РєР°: РјР°С‚СЂРёС†Р° вЂ” СЃРёСЃС‚РµРјР° РЅРµРєРѕС‚РѕСЂС‹С… РјР°С‚РµРјР°С‚РёС‡РµСЃРєРёС… РІРµР»РёС‡РёРЅ, СЂР°СЃРїРѕР»РѕР¶РµРЅРЅС‹С…
РІ РІРёРґРµ РїСЂСЏРјРѕСѓРіРѕР»СЊРЅРѕР№ СЃС…РµРјС‹.
РџСЂРёРјРµСЂС‹ РјР°С‚СЂРёС† РІС‹ РЅР°Р№РґРµС‚Рµ РІ РјРµС‚РѕРґРёС‡РєРµ.
РЎР»РµРґСѓСЋС‰РёР№ С€Р°Рі вЂ” СЂРµР°Р»РёР·РѕРІР°С‚СЊ РїРµСЂРµРіСЂСѓР·РєСѓ РјРµС‚РѕРґР° str() РґР»СЏ РІС‹РІРѕРґР° РјР°С‚СЂРёС†С‹ РІ РїСЂРёРІС‹С‡РЅРѕРј РІРёРґРµ.
Р”Р°Р»РµРµ СЂРµР°Р»РёР·РѕРІР°С‚СЊ РїРµСЂРµРіСЂСѓР·РєСѓ РјРµС‚РѕРґР° add() РґР»СЏ СЂРµР°Р»РёР·Р°С†РёРё РѕРїРµСЂР°С†РёРё СЃР»РѕР¶РµРЅРёСЏ РґРІСѓС… РѕР±СЉРµРєС‚РѕРІ
РєР»Р°СЃСЃР° Matrix (РґРІСѓС… РјР°С‚СЂРёС†). Р РµР·СѓР»СЊС‚Р°С‚РѕРј СЃР»РѕР¶РµРЅРёСЏ РґРѕР»Р¶РЅР° Р±С‹С‚СЊ РЅРѕРІР°СЏ РјР°С‚СЂРёС†Р°.
РџРѕРґСЃРєР°Р·РєР°: СЃР»РѕР¶РµРЅРёРµ СЌР»РµРјРµРЅС‚РѕРІ РјР°С‚СЂРёС† РІС‹РїРѕР»РЅСЏС‚СЊ РїРѕСЌР»РµРјРµРЅС‚РЅРѕ вЂ” РїРµСЂРІС‹Р№ СЌР»РµРјРµРЅС‚ РїРµСЂРІРѕР№
СЃС‚СЂРѕРєРё РїРµСЂРІРѕР№ РјР°С‚СЂРёС†С‹ СЃРєР»Р°РґС‹РІР°РµРј СЃ РїРµСЂРІС‹Рј СЌР»РµРјРµРЅС‚РѕРј РїРµСЂРІРѕР№ СЃС‚СЂРѕРєРё РІС‚РѕСЂРѕР№ РјР°С‚СЂРёС†С‹ Рё С‚.Рґ.'''


class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Problems with shape'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join(map(str, summed_line)) + '\n'
        else:
            return 'Problems with shape'
        return answer


# matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
# matrix_2 = Matrix([[2, 3], [4, 5], [6, 7], [10, 20]])
# print(matrix_1)
# print()
# print(matrix_1 + matrix_2)  # matrix_1.__add__(matrix_2)

'''2. Р РµР°Р»РёР·РѕРІР°С‚СЊ РїСЂРѕРµРєС‚ СЂР°СЃС‡РµС‚Р° СЃСѓРјРјР°СЂРЅРѕРіРѕ СЂР°СЃС…РѕРґР° С‚РєР°РЅРё РЅР° РїСЂРѕРёР·РІРѕРґСЃС‚РІРѕ
РѕРґРµР¶РґС‹. РћСЃРЅРѕРІРЅР°СЏ СЃСѓС‰РЅРѕСЃС‚СЊ (РєР»Р°СЃСЃ) СЌС‚РѕРіРѕ РїСЂРѕРµРєС‚Р° вЂ” РѕРґРµР¶РґР°, РєРѕС‚РѕСЂР°СЏ РјРѕР¶РµС‚ РёРјРµС‚СЊ
РѕРїСЂРµРґРµР»РµРЅРЅРѕРµ РЅР°Р·РІР°РЅРёРµ. Рљ С‚РёРїР°Рј РѕРґРµР¶РґС‹ РІ СЌС‚РѕРј РїСЂРѕРµРєС‚Рµ РѕС‚РЅРѕСЃСЏС‚СЃСЏ РїР°Р»СЊС‚Рѕ Рё РєРѕСЃС‚СЋРј.
РЈ СЌС‚РёС… С‚РёРїРѕРІ РѕРґРµР¶РґС‹ СЃСѓС‰РµСЃС‚РІСѓСЋС‚ РїР°СЂР°РјРµС‚СЂС‹: СЂР°Р·РјРµСЂ (РґР»СЏ РїР°Р»СЊС‚Рѕ) Рё СЂРѕСЃС‚ (РґР»СЏ РєРѕСЃС‚СЋРјР°).
Р­С‚Рѕ РјРѕРіСѓС‚ Р±С‹С‚СЊ РѕР±С‹С‡РЅС‹Рµ С‡РёСЃР»Р°: V Рё H, СЃРѕРѕС‚РІРµС‚СЃС‚РІРµРЅРЅРѕ.
Р”Р»СЏ РѕРїСЂРµРґРµР»РµРЅРёСЏ СЂР°СЃС…РѕРґР° С‚РєР°РЅРё РїРѕ РєР°Р¶РґРѕРјСѓ С‚РёРїСѓ РѕРґРµР¶РґС‹ РёСЃРїРѕР»СЊР·РѕРІР°С‚СЊ С„РѕСЂРјСѓР»С‹:
РґР»СЏ РїР°Р»СЊС‚Рѕ (V/6.5 + 0.5), РґР»СЏ РєРѕСЃС‚СЋРјР° (2 * H + 0.3). РџСЂРѕРІРµСЂРёС‚СЊ СЂР°Р±РѕС‚Сѓ СЌС‚РёС… 
РјРµС‚РѕРґРѕРІ РЅР° СЂРµР°Р»СЊРЅС‹С… РґР°РЅРЅС‹С….
Р РµР°Р»РёР·РѕРІР°С‚СЊ РѕР±С‰РёР№ РїРѕРґСЃС‡РµС‚ СЂР°СЃС…РѕРґР° С‚РєР°РЅРё. РџСЂРѕРІРµСЂРёС‚СЊ РЅР° РїСЂР°РєС‚РёРєРµ РїРѕР»СѓС‡РµРЅРЅС‹Рµ 
РЅР° СЌС‚РѕРј СѓСЂРѕРєРµ Р·РЅР°РЅРёСЏ: СЂРµР°Р»РёР·РѕРІР°С‚СЊ Р°Р±СЃС‚СЂР°РєС‚РЅС‹Рµ РєР»Р°СЃСЃС‹ РґР»СЏ РѕСЃРЅРѕРІРЅС‹С… РєР»Р°СЃСЃРѕРІ 
РїСЂРѕРµРєС‚Р°, РїСЂРѕРІРµСЂРёС‚СЊ РЅР° РїСЂР°РєС‚РёРєРµ СЂР°Р±РѕС‚Сѓ РґРµРєРѕСЂР°С‚РѕСЂР° @property.'''

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    @property
    def calculate(self):
        return round((self.param / 6.5) + 0.5)


class Suit(Clothes):

    @property
    def calculate(self):
        return round((2 * self.param) + 0.3)


# coat = Coat(45)
# suit = Suit(170)
# print(coat.calculate)
# print(suit.calculate)

'''3. Р РµР°Р»РёР·РѕРІР°С‚СЊ РїСЂРѕРіСЂР°РјРјСѓ СЂР°Р±РѕС‚С‹ СЃ РєР»РµС‚РєР°РјРё. РќРµРѕР±С…РѕРґРёРјРѕ СЃРѕР·РґР°С‚СЊ РєР»Р°СЃСЃ РљР»РµС‚РєР°.
Р’ РµРіРѕ РєРѕРЅСЃС‚СЂСѓРєС‚РѕСЂРµ РёРЅРёС†РёР°Р»РёР·РёСЂРѕРІР°С‚СЊ РїР°СЂР°РјРµС‚СЂ, СЃРѕРѕС‚РІРµС‚СЃС‚РІСѓСЋС‰РёР№ РєРѕР»РёС‡РµСЃС‚РІСѓ 
РєР»РµС‚РѕРє (С†РµР»РѕРµ С‡РёСЃР»Рѕ). Р’ РєР»Р°СЃСЃРµ РґРѕР»Р¶РЅС‹ Р±С‹С‚СЊ СЂРµР°Р»РёР·РѕРІР°РЅС‹ РјРµС‚РѕРґС‹ РїРµСЂРµРіСЂСѓР·РєРё
Р°СЂРёС„РјРµС‚РёС‡РµСЃРєРёС… РѕРїРµСЂР°С‚РѕСЂРѕРІ: 
СЃР»РѕР¶РµРЅРёРµ (add()), 
РІС‹С‡РёС‚Р°РЅРёРµ (sub()), 
СѓРјРЅРѕР¶РµРЅРёРµ (mul()),
РґРµР»РµРЅРёРµ (truediv()).
Р”Р°РЅРЅС‹Рµ РјРµС‚РѕРґС‹ РґРѕР»Р¶РЅС‹ РІС‹РїРѕР»РЅСЏС‚СЊ СѓРІРµР»РёС‡РµРЅРёРµ,СѓРјРµРЅСЊС€РµРЅРёРµ, СѓРјРЅРѕР¶РµРЅРёРµ Рё 
РѕР±С‹С‡РЅРѕРµ (РЅРµ С†РµР»РѕС‡РёСЃР»РµРЅРЅРѕРµ) РґРµР»РµРЅРёРµ РєР»РµС‚РѕРє, СЃРѕРѕС‚РІРµС‚СЃС‚РІРµРЅРЅРѕ.
Р’ РјРµС‚РѕРґРµ РґРµР»РµРЅРёСЏ РґРѕР»Р¶РЅРѕ РѕСЃСѓС‰РµСЃС‚РІР»СЏС‚СЊСЃСЏ РѕРєСЂСѓРіР»РµРЅРёРµ Р·РЅР°С‡РµРЅРёСЏ РґРѕ С†РµР»РѕРіРѕ С‡РёСЃР»Р°.
Р’ РєР»Р°СЃСЃРµ РЅРµРѕР±С…РѕРґРёРјРѕ СЂРµР°Р»РёР·РѕРІР°С‚СЊ РјРµС‚РѕРґ make_cell(), РїСЂРёРЅРёРјР°СЋС‰РёР№ СЌРєР·РµРјРїР»СЏСЂ РєР»Р°СЃСЃР° 
Рё РєРѕР»РёС‡РµСЃС‚РІРѕ РєР»РµС‚РѕРє РІ СЂСЏРґСѓ. РњРµС‚РѕРґ РґРѕР»Р¶РµРЅ РІРѕР·РІСЂР°С‰Р°С‚СЊ СЃС‚СЂРѕРєСѓ РІРёРґСѓ **\n\n**..., 
РіРґРµ РєРѕР»РёС‡РµСЃС‚РІРѕ РєР»РµС‚РѕРє РјРµР¶РґСѓ \n СЂР°РІРЅРѕ РїРµСЂРµРґР°РЅРЅРѕРјСѓ Р°СЂРіСѓРјРµРЅС‚Сѓ, Р° РєРѕР»РёС‡РµСЃС‚РІРѕ СЂСЏРґРѕРІ
РѕРїСЂРµРґРµР»СЏРµС‚СЃСЏ, РёСЃС…РѕРґСЏ РёР· РѕР±С‰РµРіРѕ РєРѕР»РёС‡РµСЃС‚РІР° РєР»РµС‚РѕРє.
РџСЂРё СЃРѕР·РґР°РЅРёРё СЌРєР·РµРјРїР»СЏСЂР° РєР»РµС‚РєРё РґРѕР»Р¶РЅР° РїСЂРѕРёСЃС…РѕРґРёС‚СЊ РїРµСЂРµР·Р°РїРёСЃСЊ РїР°СЂР°РјРµС‚СЂР°, 
РєРѕС‚РѕСЂС‹Р№ С…СЂР°РЅРёС‚ РєРѕР»РёС‡РµСЃС‚РІРѕ РєР»РµС‚РѕРє.'''

class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) \
               + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return 'Sum of cell is ' + str(self.nums + other.nums)
        # return Cell(self.nums + other.nums)

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else 'РЇС‡РµРµРє РІ РїРµСЂРІРѕР№ РєР»РµС‚РєРµ РјРµРЅСЊС€Рµ РёР»Рё СЂР°РІРЅРѕ РІС‚РѕСЂРѕР№, РІС‹С‡РёС‚Р°РЅРёРµ РЅРµРІРѕР·РјРѕР¶РЅРѕ'

    def __mul__(self, other):
        return 'Multiply of cells is ' + str(self.nums * other.nums)

    def __truediv__(self, other):
        return 'Truediv of cells is ' + str(round(self.nums / other.nums))


# cell_1 = Cell(10)
# cell_2 = Cell(34)
# print(cell_1)
# print(cell_1 + cell_2)
# print(cell_2.make_order(10))
