
bank_dict = {
    "Priya": {"balance": 100, "pin": "4821"},
    "Carlos": {"balance": 300, "pin": "1092"},
    "Amira": {"balance": 0, "pin": "0000"},
    "Jordan": {"balance": 7788, "pin": "9999"},
}


def welcome_message():
    """
    Display a welcome message for Berklee Bank.

    Inputs:
        None

    Returns:
        None

    Side Effects:
        Prints a welcome message.
    """
    pass


def login():
    """
    Ask the user for their name and PIN.
    Check if the information matches the bank dictionary.

    Inputs:
        User's name (str) and PIN (str) from input().

    Returns:
        str: The username if login is successful.
        None: If login fails.

    Side Effects:
        None
    """
    pass


def show_menu():
    """
    Display the ATM menu and ask the user to choose an option.

    Inputs:
        User's menu choice (str) from input().

    Returns:
        str: The user's menu choice.

    Side Effects:
        Prints the menu and prompts for input.
    """
    pass


def check_balance(name):
    """
    Show the user's current account balance.

    Inputs:
        name (str): The user's account name.

    Returns:
        None

    Side Effects:
        Prints the current balance.
    """
    pass


def deposit_money(name):
    """
    Ask the user for a deposit amount.
    Add the amount to their account balance.

    Inputs:
        name (str): The user's account name.
        Deposit amount from input().

    Returns:
        None

    Side Effects:
        Updates the balance in bank_dict.
        Prints the updated balance.
    """
    pass


def withdraw_money(name):
    """
    Ask the user for a withdrawal amount.
    Check if the account has enough money.
    Subtract the amount if the balance is sufficient.

    Inputs:
        name (str): The user's account name.
        Withdrawal amount from input().

    Returns:
        None

    Side Effects:
        Updates the balance in bank_dict if sufficient.
        Prints a success or error message.
    """
    pass


def exit_atm():
    """
    Log out the current user.

    Inputs:
        None

    Returns:
        None

    Side Effects:
        Prints a logout message.
    """
    pass