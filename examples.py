from money.models import AmountCurrency


if __name__ == "__main__":
    # create instances
    x = AmountCurrency(19600, "BYN")
    y = AmountCurrency(11)
    z = AmountCurrency(12.34, "EUR")

    # result “EUR”
    print(z + 3.11 * x + y * 0.8)

    lst = [AmountCurrency(100000, "BYN"),
           AmountCurrency(11),
           AmountCurrency(12.01, "JPY")]
    s = sum(lst)

    # result in “BYN”
    print(s)

