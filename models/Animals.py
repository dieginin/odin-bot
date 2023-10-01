class Animal:
    def __init__(
        self,
        name: str,
        hash: str,
        value: int,
        probability: float,
    ):
        self.name = name
        self.hash = hash
        self.value = value
        self.probability = probability


class Alien(Animal):
    def __init__(self):
        name = "Alien"
        hash = "alien"
        value = 1500
        probability = 0.6
        super().__init__(name, hash, value, probability)


class Leon(Animal):
    def __init__(self):
        name = "León"
        hash = "lion"
        value = 1300
        probability = 1.6
        super().__init__(name, hash, value, probability)


class Tigre(Animal):
    def __init__(self):
        name = "Tigre"
        hash = "tiger"
        value = 1100
        probability = 2.6
        super().__init__(name, hash, value, probability)


class Elefante(Animal):
    def __init__(self):
        name = "Elefante"
        hash = "elephant"
        value = 900
        probability = 3.6
        super().__init__(name, hash, value, probability)


class Oso(Animal):
    def __init__(self):
        name = "Oso"
        hash = "bear"
        value = 800
        probability = 4.6
        super().__init__(name, hash, value, probability)


class Caballo(Animal):
    def __init__(self):
        name = "Caballo"
        hash = "horse"
        value = 700
        probability = 5.6
        super().__init__(name, hash, value, probability)


class Lobo(Animal):
    def __init__(self):
        name = "Lobo"
        hash = "wolf"
        value = 600
        probability = 6.6
        super().__init__(name, hash, value, probability)


class Zorro(Animal):
    def __init__(self):
        name = "Zorro"
        hash = "fox"
        value = 500
        probability = 7.6
        super().__init__(name, hash, value, probability)


class Mono(Animal):
    def __init__(self):
        name = "Mono"
        hash = "monkey"
        value = 400
        probability = 8.6
        super().__init__(name, hash, value, probability)


class Conejo(Animal):
    def __init__(self):
        name = "Conejo"
        hash = "rabbit"
        value = 300
        probability = 9.6
        super().__init__(name, hash, value, probability)


class Pajaro(Animal):
    def __init__(self):
        name = "Pájaro"
        hash = "bird"
        value = 200
        probability = 10.6
        super().__init__(name, hash, value, probability)


class Gato(Animal):
    def __init__(self):
        name = "Gato"
        hash = "cat"
        value = 150
        probability = 11.6
        super().__init__(name, hash, value, probability)


class Perro(Animal):
    def __init__(self):
        name = "Perro"
        hash = "dog"
        value = 120
        probability = 12.6
        super().__init__(name, hash, value, probability)


class Hamster(Animal):
    def __init__(self):
        name = "Hamster"
        hash = "hamster"
        value = 80
        probability = 13.6
        super().__init__(name, hash, value, probability)


class Pollo(Animal):
    def __init__(self):
        name = "Pollo"
        hash = "chicken"
        value = 10
        probability = 35
        super().__init__(name, hash, value, probability)
