class InsufficientCoins(Exception):
    def __init__(
        self,
        coins: int,
        pocket: int,
    ):
        self.coins = coins
        self.pocket = pocket


class InsufficientResources(Exception):
    def __init__(
        self,
        resource,
    ):
        self.resource = resource


class InsufficientBalance(Exception):
    def __init__(
        self,
        coins: int,
        bank: int,
    ):
        self.coins = coins
        self.bank = bank


class SecureCoins(Exception):
    def __init__(
        self,
        coins: int,
        pocket: int,
        secure: int,
    ):
        self.coins = coins
        self.pocket = pocket
        self.secure = secure


class MinimunAmount(Exception):
    def __init__(
        self,
        coins: int,
    ):
        self.coins = coins
