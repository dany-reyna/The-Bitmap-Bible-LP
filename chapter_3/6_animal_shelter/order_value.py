from abc import ABC


class Animal(ABC):
    def __init__(self, name):
        self.name = name
        self._order = 0

    def is_older_than(self, animal):
        return self.order > animal.order

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        self._order = value


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class AnimalQueue:
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.order = 0

    def enqueue(self, animal):
        animal.order = self.order
        self.order += 1

        if isinstance(animal, Dog):
            self.dogs.append(animal)
        elif isinstance(animal, Cat):
            self.cats.append(animal)

    def dequeue_dog(self):
        return self.dogs.pop()

    def dequeue_cat(self):
        return self.cats.pop()

    def dequeue_any(self):
        if not self.dogs and not self.cats:
            return None

        if not self.dogs:
            return self.dequeue_cat()
        elif not self.cats:
            return self.dequeue_dog()

        if self.dogs[-1].is_older_than(self.cats[-1]):
            return self.dequeue_dog()
        else:
            return self.dequeue_cat()

    def __len__(self):
        return len(self.dogs) + len(self.cats)


if __name__ == '__main__':
    animals = AnimalQueue()

    print(animals.dequeue_any())

    animals.enqueue(Cat("Callie"))
    animals.enqueue(Cat("Kiki"))
    animals.enqueue(Dog("Fido"))
    animals.enqueue(Dog("Dora"))
    animals.enqueue(Cat("Kari"))
    animals.enqueue(Dog("Dexter"))
    animals.enqueue(Dog("Dobo"))
    animals.enqueue(Cat("Copa"))

    print(animals.dequeue_any().name)
    print(animals.dequeue_any().name)
    print(animals.dequeue_any().name)

    animals.enqueue(Dog("Kapa"))
    animals.enqueue(Cat("Kilo"))

    print(animals.dequeue_dog().name)
    print(animals.dequeue_cat().name)

    while animals:
        print(animals.dequeue_any().name)
