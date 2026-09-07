from bank import BankAccount

shared_account = BankAccount(100)

def test_deposit_independent():
    account = BankAccount(100)
    account.deposit(50)
    assert account.balance == 150

def test_withdraw_indenpendent():
    account = BankAccount(100)
    account.withdraw(30)
    assert account.balance == 70


