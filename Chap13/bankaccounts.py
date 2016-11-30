class BankAccount:
    """  Models a bank account  """
    def __init__(self, number, name, balance):
        """  Initialize the instance variables of a bank account object.
             Disallows a negative initial balance.  """
        if balance < 0:
            raise ValueError('Negative initial balance')
        self.__account_number = number  # Account number
        self.__name = name              # Customer name
        self.__balance = balance        # Funds available in the account

    def id(self):
        """ Returns the account number of this bank account object.  """
        return self.__account_number

    def deposit(self, amount):
        """ Add funds to the account.  There is no limit
            to the size of the deposit.  """
        self.__balance += amount

    def withdraw(self, amount):
        """ Remove funds from the account, if possible.
            Only completes the withdrawal successfully if
            there are enough funds in the account to 
            fulfill the withdrawal.
            Return true if successful, false otherwise """
        result = False   # Unsuccessful by default
        if self.__balance - amount >= 0:
            self.__balance -= amount
            result = True   # Success
        return result

    def __str__(self):
        """  Returns the string representation for this object """
        return '[{:>5} {:<10} {:>7} ]'.format(self.__account_number,
                                               self.__name, self.__balance)


# -----------------------------------------------------------------
# Global functions that use BankAccount objects

def open_database(filename, db):
    """ Read account information from a given file and store it
        in the given list.  """
    with open(filename) as lines:     # Open file to read
        for line in lines:
            line.strip()
            number, name, balance = line.split(",")
            db.append(BankAccount(int(number), name, int(balance)))


def print_database(db):
    """ Display the contents of the database """
    for acct in db:
        print(acct)  # Calls the __str__ method of acct
        
def get_account(db, account_number):
    """ Retrieve an account object with a given account number. """
    for acct in db:
        if acct.id() == account_number:
            return acct


def main():
    # Simple bank account "database"
    database = []

    try:
        # Open the database of accounts
        open_database('accountdata.text', database)
        print_database(database)
        print("--------------------")
        customer = get_account(database, 129)
        if customer:
            print("Account 129 before deposit of $100: ", end="")
            print(customer)
            customer.deposit(100)
            print("Account 129 after  deposit of $100: ", end="")
            print(customer)
            print("--------------------")
            print("Account 129 before withdraw of $500: ", end="")
            print(customer)
            customer.withdraw(500)
            print("Account 129 after  withdraw of $500: ", end="")
            print(customer)
            print("--------------------")
            print("Account 129 before withdraw of $80000: ", end="")
            print(customer)
            customer.withdraw(80000)
            print("Account 129 after  withdraw of $80000: ", end="")
            print(customer)

    except Exception:
        print('Error in account database')
        raise


main()
