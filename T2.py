transactions = [
    "P 300",
    "P 300",
    "O 200",
    "P 100"
]

def GetBalance():
    balance = 0
    for tr in transactions:
        transactionAmount = int(tr.split(' ')[1])
        if tr.startswith('P'):
            balance += transactionAmount
        elif tr.startswith('O'):
            balance -= transactionAmount
    return balance

print(f'Your balance is: {GetBalance()}')
