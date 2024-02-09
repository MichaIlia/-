class chair:
    def __init__(self, legs, material, height, size):
        self.legs = legs
        self.height = height
        self.material = material
        self.size = size

    def __str__(self):
        return f'Стул - (Количество ножек у стула: {my_chair.legs}, Высота стула: {my_chair.height}, Материал из которого изготовлен стул: {my_chair.material}, Размер сидалища: {my_chair.size})'
    
    def __eq__(self, other):
            if not isinstance(other, chair):
                return self.size == other.size
            return False
    def __ne__(self, other):
            if not isinstance(other, chair):
                return self.size != other.size
            return False
    def __gt__(self, other):
            if not isinstance(other, chair):
                return self.size > other.size
            return False
    def __lt__(self, other):
            if not isinstance(other, chair):
                return self.size < other.size
            return False
    def __ge__(self, other):
            if not isinstance(other, chair):
                return self.size >= other.size
            return False
    def __le__(self, other):
            if not isinstance(other, chair):
                return self.size <= other.size
            return False
    
    def __repr__(self):
            return f'Стул - (Количество ножек у стула: {my_chair.legs}, Высота стула: {my_chair.height}, Материал из которого изготовлен стул: {my_chair.material}, Размер сидалища: {my_chair.size})'

my_chair = chair(4, 'Дуб', 57, 30)
my_chair2 = chair(3, 'Дуб', 68, 40)


print(my_chair < my_chair2)