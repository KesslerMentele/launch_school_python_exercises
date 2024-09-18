

def main():
    rate = 0.05
    years = 5
    balance = 1000 * (1 + rate)**years
    print(f"After 5 years, the balance is {balance}")

if __name__ == "__main__":
    main()