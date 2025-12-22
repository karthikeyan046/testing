# Simulate account operations

def view_balance():
    print("Your balance is $1000")

def transfer_funds(amount):
    print(f"Transferred ${amount} successfully!")

def pay_bill(amount):
    print(f"Bill of ${amount} paid successfully!")

if __name__ == "__main__":
    view_balance()
    transfer_funds(1000)
    pay_bill(200)
