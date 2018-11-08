#1. Circular Sector Class
class Sector:
    def __init__(self):
        self.fr = 0
        self.to = 0
        self.rad = 0

    def rotate(self, angle):
        self.fr += angle
        self.to += angle

    def intersect(self, other):
        intersect = Sector()
        if self.fr >= other.fr:
            intersect.fr = self.fr
        else:
            intersect.fr = other.fr
        if self.to <= other.to:
            intersect.to = self.to
        else:
            intersect.to = other.to
        if self.rad <= other.rad:
            intersect.rad = self.rad
        else:
            intersect.rad = other.rad
        return intersect

    def is_empty(self):
        if self.fr == self.to or self.rad == 0:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.fr == other.fr and self.to == other.to and self.rad == other.rad:
            return True
        else:
            return False

    def __str__(self):
        return str(self.fr) + " " + str(self.to) + " " + str(self.rad)


# NO modications below this line
s1 = Sector()
s1.fr = 0
s1.to = 20
s1.rad = 40
print(s1)
s1.rotate(50)
print(s1)
s2 = Sector()
s2.fr = 50
s2.to = 80
s2.rad = 40
print(s1 == s2)
s2.fr = 60
s2.to = 100
s2.rad = 30
s3 = s1.intersect(s2)
print(s3)

#2. Advanced Counter Class
class Counter:
    def __init__(self, id):
        self._items = dict()
        self._id = id

    def add(self, item_name, amount, price_of_unit):
        if item_name in self._items.keys():
            self._items[item_name][0] += amount
        else:
            self._items[item_name] = [amount, price_of_unit]

    def remove(self, item_name, amount):
        if item_name not in self._items.keys():
            return 0
        elif item_name in self._items.keys():
            amount_in_stock = self._items[item_name][0]
            if amount <= amount_in_stock:
                self._items[item_name][0] -= amount

    def reset(self):
        self._items = dict()

    def get_total(self):
        summ = 0.0
        for val in self._items.values():
            summ += val[0] * val[1]
        return round(summ, 2)

    def status_print(self):
        total_amount_items = 0
        for val in self._items.values():
            total_amount_items += val[0]
        print(self._id, total_amount_items, self.get_total())


#NO modifications modify below this line
c = Counter("C001")
c.add("Spaghetti", 5, 1.8)
c.status_print()
c.add("Ice Cream", 2, 3.4)
c.status_print()
print(c.get_total())
c.add("Spaghetti", 3, 1.8)
c.status_print()
c.remove("Ice Cream", 1)
c.status_print()
c.reset()
c.add("Coke", 5, 1.45)
c.status_print()
