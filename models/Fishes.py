class Fish:
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


class Nessie(Fish):
    def __init__(self):
        name = "Nessie"
        hash = "sauropod"
        value = 1500
        probability = 0.05
        super().__init__(name, hash, value, probability)


class Ballena(Fish):
    def __init__(self):
        name = "Ballena"
        hash = "whale"
        value = 1200
        probability = 0.14
        super().__init__(name, hash, value, probability)


class Tiburon(Fish):
    def __init__(self):
        name = "Tiburón"
        hash = "shark"
        value = 1000
        probability = 0.23
        super().__init__(name, hash, value, probability)


class Calamar(Fish):
    def __init__(self):
        name = "Calamar"
        hash = "squid"
        value = 800
        probability = 0.32
        super().__init__(name, hash, value, probability)


class Delfin(Fish):
    def __init__(self):
        name = "Delfín"
        hash = "dolphin"
        value = 500
        probability = 0.41
        super().__init__(name, hash, value, probability)


class Pulpo(Fish):
    def __init__(self):
        name = "Pulpo"
        hash = "octopus"
        value = 400
        probability = 1.39
        super().__init__(name, hash, value, probability)


class Foca(Fish):
    def __init__(self):
        name = "Foca"
        hash = "seal"
        value = 300
        probability = 2.37
        super().__init__(name, hash, value, probability)


class Nutria(Fish):
    def __init__(self):
        name = "Nutria"
        hash = "otter"
        value = 200
        probability = 3.35
        super().__init__(name, hash, value, probability)


class Tortuga(Fish):
    def __init__(self):
        name = "Tortuga"
        hash = "turtle"
        value = 150
        probability = 4.33
        super().__init__(name, hash, value, probability)


class Langosta(Fish):
    def __init__(self):
        name = "Langosta"
        hash = "lobster"
        value = 100
        probability = 5.31
        super().__init__(name, hash, value, probability)


class Globo(Fish):
    def __init__(self):
        name = "Pez Globo"
        hash = "blowfish"
        value = 80
        probability = 8.2
        super().__init__(name, hash, value, probability)


class Cangrejo(Fish):
    def __init__(self):
        name = "Cangrejo"
        hash = "crab"
        value = 60
        probability = 11.09
        super().__init__(name, hash, value, probability)


class Charal(Fish):
    def __init__(self):
        name = "Charal"
        hash = "fish"
        value = 40
        probability = 13.98
        super().__init__(name, hash, value, probability)


class Camaron(Fish):
    def __init__(self):
        name = "Camarón"
        hash = "shrimp"
        value = 30
        probability = 16.87
        super().__init__(name, hash, value, probability)


class Concha(Fish):
    def __init__(self):
        name = "Concha"
        hash = "shell"
        value = 10
        probability = 31.96
        super().__init__(name, hash, value, probability)
