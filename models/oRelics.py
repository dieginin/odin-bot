class Relic:
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


class Cometa(Relic):
    def __init__(self):
        name = "Cometa"
        hash = "comet"
        value = 1500
        probability = 0.05
        super().__init__(name, hash, value, probability)


class Diamante(Relic):
    def __init__(self):
        name = "Diamante"
        hash = "gem"
        value = 1200
        probability = 0.14
        super().__init__(name, hash, value, probability)


class Turquesa(Relic):
    def __init__(self):
        name = "Turquesa"
        hash = "diamond_shape_with_a_dot_inside"
        value = 1000
        probability = 0.23
        super().__init__(name, hash, value, probability)


class Granito(Relic):
    def __init__(self):
        name = "Granito"
        hash = "bricks"
        value = 800
        probability = 0.32
        super().__init__(name, hash, value, probability)


class Piedra(Relic):
    def __init__(self):
        name = "Piedra"
        hash = "rock"
        value = 500
        probability = 0.41
        super().__init__(name, hash, value, probability)


class Trofeo(Relic):
    def __init__(self):
        name = "Trofeo"
        hash = "trophy"
        value = 400
        probability = 1.39
        super().__init__(name, hash, value, probability)


class Violin(Relic):
    def __init__(self):
        name = "Violín"
        hash = "violin"
        value = 300
        probability = 2.37
        super().__init__(name, hash, value, probability)


class Reloj(Relic):
    def __init__(self):
        name = "Reloj"
        hash = "clock"
        value = 200
        probability = 3.35
        super().__init__(name, hash, value, probability)


class Lacrosse(Relic):
    def __init__(self):
        name = "Lacrosse"
        hash = "lacrosse"
        value = 150
        probability = 4.33
        super().__init__(name, hash, value, probability)


class Campana(Relic):
    def __init__(self):
        name = "Campana"
        hash = "bell"
        value = 100
        probability = 5.31
        super().__init__(name, hash, value, probability)


class Varita(Relic):
    def __init__(self):
        name = "Varita"
        hash = "magic_wand"
        value = 80
        probability = 8.2
        super().__init__(name, hash, value, probability)


class Dardos(Relic):
    def __init__(self):
        name = "Dardos"
        hash = "dart"
        value = 60
        probability = 11.09
        super().__init__(name, hash, value, probability)


class Balon(Relic):
    def __init__(self):
        name = "Balón"
        hash = "soccer"
        value = 40
        probability = 13.98
        super().__init__(name, hash, value, probability)


class Dado(Relic):
    def __init__(self):
        name = "Dado"
        hash = "game_die"
        value = 30
        probability = 16.87
        super().__init__(name, hash, value, probability)


class Jeringa(Relic):
    def __init__(self):
        name = "Jeringa"
        hash = "syringe"
        value = 10
        probability = 31.96
        super().__init__(name, hash, value, probability)
