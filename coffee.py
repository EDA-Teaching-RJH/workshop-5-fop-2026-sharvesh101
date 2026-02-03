check = [50,20,10,5]
def get_coin():
    coin = int(input("Insert cash [50p/20p/10p/5p]: ").replace("p",""))
    if coin in check:
        return coin
    else:
        print("please insert only [50p/20p/10p/5p]: ")
        return get_coin()
    
def update_total(current, coin):
    current = current - coin
    print(str(current)+"p","remaing")
    return current

def dispense_product(total_inserted):
    if total_inserted == 0:
        print("thank you here is your Coffee")
    else:
        calculate_change(total_inserted)

def calculate_change(amount):
    if amount < 0:
        print("Thank you here is you Coffee")
        print(f"And here is your {str(amount).replace("-","")+"p"} change back")

def main():
    amount_due = 75
    while amount_due > 0:
        coin = get_coin()
        amount_due = update_total(amount_due, coin)
    dispense_product(amount_due)

main()