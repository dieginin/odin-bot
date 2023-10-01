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
        probability = 0.05
        super().__init__(name, hash, value, probability)


class Leon(Animal):
    def __init__(self):
        name = "León"
        hash = "lion"
        value = 1200
        probability = 0.14
        super().__init__(name, hash, value, probability)


class Tigre(Animal):
    def __init__(self):
        name = "Tigre"
        hash = "tiger"
        value = 1000
        probability = 0.23
        super().__init__(name, hash, value, probability)


class Elefante(Animal):
    def __init__(self):
        name = "Elefante"
        hash = "elephant"
        value = 800
        probability = 0.32
        super().__init__(name, hash, value, probability)


class Oso(Animal):
    def __init__(self):
        name = "Oso"
        hash = "bear"
        value = 500
        probability = 0.41
        super().__init__(name, hash, value, probability)


class Caballo(Animal):
    def __init__(self):
        name = "Caballo"
        hash = "horse"
        value = 400
        probability = 1.39
        super().__init__(name, hash, value, probability)


class Lobo(Animal):
    def __init__(self):
        name = "Lobo"
        hash = "wolf"
        value = 300
        probability = 2.37
        super().__init__(name, hash, value, probability)


class Zorro(Animal):
    def __init__(self):
        name = "Zorro"
        hash = "fox"
        value = 200
        probability = 3.35
        super().__init__(name, hash, value, probability)


class Mono(Animal):
    def __init__(self):
        name = "Mono"
        hash = "monkey"
        value = 150
        probability = 4.33
        super().__init__(name, hash, value, probability)


class Conejo(Animal):
    def __init__(self):
        name = "Conejo"
        hash = "rabbit"
        value = 100
        probability = 5.31
        super().__init__(name, hash, value, probability)


class Pajaro(Animal):
    def __init__(self):
        name = "Pájaro"
        hash = "bird"
        value = 80
        probability = 8.2
        super().__init__(name, hash, value, probability)


class Gato(Animal):
    def __init__(self):
        name = "Gato"
        hash = "cat"
        value = 60
        probability = 11.09
        super().__init__(name, hash, value, probability)


class Perro(Animal):
    def __init__(self):
        name = "Perro"
        hash = "dog"
        value = 40
        probability = 13.98
        super().__init__(name, hash, value, probability)


class Hamster(Animal):
    def __init__(self):
        name = "Hamster"
        hash = "hamster"
        value = 30
        probability = 16.87
        super().__init__(name, hash, value, probability)


class Pollo(Animal):
    def __init__(self):
        name = "Pollo"
        hash = "chicken"
        value = 10
        probability = 31.96
        super().__init__(name, hash, value, probability)
