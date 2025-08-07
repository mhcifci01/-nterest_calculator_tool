def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time) - principal

def main():
    print("Welcome to the Interest Calculator Tool!")
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate (in %): "))
    time = float(input("Enter the time (in years): "))

    si = simple_interest(principal, rate, time)
    ci = compound_interest(principal, rate, time)

    print(f"Simple Interest: {si:.2f}")
    print(f"Compound Interest: {ci:.2f}")

if __name__ == "__main__":
    main()