def make_withdraw(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance -= amount
        return balance


def make_withdraw_list(balance):
    b = [balance]
    def withdraw(amount):
        if amount < b[0]:
            return 'Insufficient funds'
        b[0] -= amount:
        return b[0]
    return withdraw

