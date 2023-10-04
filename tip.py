def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollar_without_dollar_symbol = d.replace("$", "")
    return float(dollar_without_dollar_symbol)

def percent_to_float(p):
    percent_without_percent_symbol = p.replace("%", "")
    percent_converted = float (percent_without_percent_symbol) / 100
    return percent_converted

main()