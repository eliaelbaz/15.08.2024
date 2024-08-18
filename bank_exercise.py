import datetime;

bank_accounts = {
    1001: {
        "first_name": "Alice",
        "last_name": "Smith",
        "id_number": "123456789",
        "balance": 2500.50,
        "transactions_to_execute": [
            ("2024-08-17 14:00:00", 1001, 1002, 300),
            ("2024-08-17 15:00:00", 1001, 1003, 200)
        ],
        "transaction_history": [
            ("2024-08-15 09:00:00", 1001, 1002, 500, "2024-08-15 09:30:00")
        ]
    },
    1002: {
        "first_name": "Bob",
        "last_name": "Johnson",
        "id_number": "987654321",
        "balance": 3900.75,
        "transactions_to_execute": [],
        "transaction_history": []
    }
};

def add_transaction(source_account, target_account, amount):
    if not validate_accounts(source_account, target_account):
        return;

    transaction = create_transaction(source_account, target_account, amount);
    bank_accounts[source_account]["transactions_to_execute"].append(transaction);
    print(f"Transaction added: {transaction}");

def create_transaction(source_account, target_account, amount):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S");
    return (timestamp, source_account, target_account, amount);

def execute_transactions(account_number):
    if not validate_account(account_number):
        return;

    transactions = bank_accounts[account_number]["transactions_to_execute"];
    for transaction in transactions:
        if process_transaction(transaction):
            update_history(account_number, transaction);
    clear_transactions(account_number);

def process_transaction(transaction):
    timestamp, source_account, target_account, amount = transaction;
    if bank_accounts[source_account]["balance"] >= amount:
        bank_accounts[source_account]["balance"] -= amount;
        bank_accounts[target_account]["balance"] += amount;
        print(f"Executed transaction: {transaction}");
        return True
    else:
        print(f"Transaction failed due to insufficient funds: {transaction}");
        return False;

def update_history(account_number, transaction):
    execution_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S");
    bank_accounts[account_number]["transaction_history"].append((*transaction, execution_time));

def clear_transactions(account_number):
    bank_accounts[account_number]["transactions_to_execute"] = [];
    print(f"All pending transactions for account {account_number} have been executed.");

def print_reports():
    options = {
        "1": print_all_accounts,
        "2": lambda: print_specific_account(int(input("Enter the account number: "))),
        "3": lambda: print_accounts_by_id(input("Enter the ID number: ")),
        "4": lambda: print_accounts_by_first_name(input("Enter the first name: ").lower()),
        "5": print_accounts_sorted_by_balance,
        "6": print_all_transaction_history,
        "7": print_accounts_with_negative_balance,
        "8": print_total_balance,
        "9": lambda: None
    };

    while True:
        choice = input(reports_menu());
        if choice in options:
            options[choice]();
            if choice == "9":
                break
        else:
            print("Invalid choice. Please try again.");

def reports_menu():
    return (
        "Reports Menu:\n"
        "1. Print all bank accounts\n"
        "2. Find and print a specific account by account number\n"
        "3. Find and print accounts by ID number\n"
        "4. Find and print accounts by first name\n"
        "5. Print all accounts sorted by balance\n"
        "6. Print all transaction history\n"
        "7. Print accounts with negative balance\n"
        "8. Print the total balance of all accounts\n"
        "9. Back to main menu\n"
        "Enter your choice: "
    );

def print_all_accounts():
    for account_number, details in bank_accounts.items():
        print(f"Account Number: {account_number}, Details: {details}");

def print_specific_account(account_number):
    if validate_account(account_number):
        print(f"Account {account_number}: {bank_accounts[account_number]}");

def print_accounts_by_id(id_number):
    for details in bank_accounts.values():
        if details["id_number"] == id_number:
            print(details);

def print_accounts_by_first_name(first_name):
    for details in bank_accounts.values():
        if details["first_name"].lower().startswith(first_name):
            print(details);

def print_accounts_sorted_by_balance():
    sorted_accounts = sorted(bank_accounts.items(), key=lambda x: x[1]["balance"]);
    for account_number, details in sorted_accounts:
        print(f"Account Number: {account_number}, Balance: {details['balance']}");

def print_all_transaction_history():
    for account_number, details in bank_accounts.items():
        print(f"Transaction history for account {account_number}: {details['transaction_history']}");

def print_accounts_with_negative_balance():
    for account_number, details in bank_accounts.items():
        if details["balance"] < 0:
            print(f"Account {account_number} has a negative balance: {details['balance']}");

def print_total_balance():
    total_balance = sum(details["balance"] for details in bank_accounts.values());
    print(f"Total balance of all accounts: {total_balance}");

def validate_account(account_number):
    if account_number not in bank_accounts:
        print("Account not found. Please try again.");
        return False;
    return True;

def validate_accounts(source_account, target_account):
    return validate_account(source_account) and validate_account(target_account);

def open_new_account():
    account_number = int(input("Enter a new account number: "));
    if account_number in bank_accounts:
        print("Account number already exists. Please try again.");
        return

    first_name = input("Enter first name: ");
    last_name = input("Enter last name: ");
    id_number = input("Enter ID number: ");
    initial_balance = float(input("Enter initial balance: "));

    bank_accounts[account_number] = {
        "first_name": first_name,
        "last_name": last_name,
        "id_number": id_number,
        "balance": initial_balance,
        "transactions_to_execute": [],
        "transaction_history": []
    };
    print(f"Account {account_number} created successfully.");

def execute_future_transactions(account_number):
    if not validate_account(account_number):
        return;

    current_time = datetime.datetime.now();
    transactions = bank_accounts[account_number]["transactions_to_execute"];

    pending_transactions = [];
    for transaction in transactions:
        transaction_time = datetime.datetime.strptime(transaction[0], "%Y-%m-%d %H:%M:%S");
        if current_time >= transaction_time:
            if process_transaction(transaction):
                update_history(account_number, transaction);
        else:
            pending_transactions.append(transaction);

    bank_accounts[account_number]["transactions_to_execute"] = pending_transactions;

def main_menu():
    options = {
        "1": lambda: add_transaction(int(input("Enter source account number: ")),
                                     int(input("Enter target account number: ")),
                                     float(input("Enter the amount to transfer: "))),
        "2": lambda: execute_transactions(int(input("Enter the account number: "))),
        "3": print_reports,
        "4": open_new_account,
        "5": lambda: execute_future_transactions(int(input("Enter the account number: "))),
        "6": lambda: exit("Exiting the system.")
    };

    while True:
        choice = input(main_menu_text());
        if choice in options:
            options[choice]();
        else:
            print("Invalid choice. Please try again.");

def main_menu_text():
    return (
        "Main Menu:\n"
        "1. Add a new transaction\n"
        "2. Execute all pending transactions for an account\n"
        "3. Reports\n"
        "4. Open a new account (Bonus)\n"
        "5. Execute future transactions for an account (Bonus)\n"
        "6. Exit\n"
        "Enter your choice: "
    );

main_menu();
