class Barber:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self._earnings = 0
        self.active = True

    def receive_payment(self, amount):
        self._earnings += amount
        print(f"{self.name} received GHS {amount}. Total earnings: GHS {self._earnings}")

    def correct_payment(self, amount, reason):
        if amount < 0:
            print(f"ERROR: Cannot correct with a negative amount")
            return
        old_earnings = self._earnings
        self._earnings = amount
        print(f"AUDIT: {self.name}'s earnings changed from GHS {old_earnings} to GHS {amount}. Reason: {reason}")

    def get_earnings(self):
        return self._earnings

    def __str__(self):
        return f"Barber: {self.name} | Earnings: GHS {self._earnings} | Active: {self.active}"

    def __repr__(self):
        return f"Barber(name='{self.name}', phone='{self.phone}', earnings={self._earnings})"


if __name__ == "__main__":
    kwame = Barber("Kwame", "0241234567")
    kwame.receive_payment(200)
    print(kwame)