class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if isinstance(amount, int):
            self._transactions.append(amount)
        else:
            raise ValueError("please use int for amount")

    @property
    def balance(self):
        return sum(self._transactions) + self.amount

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if sum(account._transactions) + account.amount - amount_to_add < 0:
            account._transactions.pop()
            raise ValueError("sorry cannot go in debt!")
        else:
            account.add_transaction(amount_to_add)
            return f"New balance: {account.balance}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __iter__(self):
        return (x for x in self._transactions)

    def __getitem__(self, name):
        return self._transactions[name]

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        acc = Account(owner=f'{self.owner}&{other.owner}', amount=self.amount + other.amount)
        acc._transactions = self._transactions + other._transactions
        return acc


acc = Account('bob', 10)
acc2 = Account('john')
print(acc.balance)
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
