

def main():
    balance = 1000
    rate = 0.05

    balance *= (1 + rate)
    balance *= (1 + rate)
    balance *= (1 + rate)
    balance *= (1 + rate)
    balance *= (1 + rate)
    print(f"After 5 years, the balance is {balance}")

if __name__ == "__main__":
    main()