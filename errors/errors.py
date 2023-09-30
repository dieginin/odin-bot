class InsufficientCoins(Exception):
    def __init__(
        self,
        coins: int,
        pocket: int,
    ):
        self.coins = coins
        self.pocket = pocket


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
