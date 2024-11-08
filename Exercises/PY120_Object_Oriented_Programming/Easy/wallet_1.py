class Wallet:
    def __init__(self, cash):
        self.amount = cash

    def __add__(self, other):
        if isinstance(other, Wallet) :
            return Wallet(self.amount + other.amount)
        elif isinstance(other, int):
            return Wallet(self.amount + other)
        else:
            return NotImplemented





wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet.amount == 80)       # True