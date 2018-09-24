from libs.currency_api.api import CurrencyRESTAPI


class AmountCurrency(object):
    BASE_CURRENCY = "USD"

    def __init__(self, amount, currency=BASE_CURRENCY, round_to=4):
        self.amount = amount
        self.currency = currency
        self.api = CurrencyRESTAPI()
        self.round_to = round_to

    def __repr__(self):
        return "%s %s" % (self.amount, self.currency)

    def __str__(self):
        return "%s %s" % (round(self.amount, self.round_to), self.currency)

    def get_rates(self, currencies):
        rates = self.api.get_rates(currencies)
        return rates

    def convert_to(self, new_currency):
        if self.currency == new_currency:
            amount = self.amount
        else:
            rates = self.get_rates([self.currency, new_currency])

            amount = self.amount
            if self.currency != self.BASE_CURRENCY:
                amount = amount / rates[self.BASE_CURRENCY + self.currency]

            if new_currency != self.BASE_CURRENCY:
                amount = amount * rates[self.BASE_CURRENCY + new_currency]

        return AmountCurrency(amount, new_currency)

    def __add__(self, other):
        if type(other) == AmountCurrency:
            if self.currency != other.currency:
                other_converted = other.convert_to(self.currency)

                return AmountCurrency(self.amount + other_converted.amount,
                                      self.currency)
            else:
                return AmountCurrency(self.amount + other.amount,
                                      self.currency)
        elif type(other) in (int, float):
            return AmountCurrency(self.amount + other, self.currency)
        else:
            raise NotImplementedError

    def __iadd__(self, other):
        if type(other) == AmountCurrency:
            other = other.convert_to(self.currency)
            self.amount += other.amount
            return self
        elif type(other) in (int, float):
            self.amount += other
            return self
        else:
            raise NotImplementedError

    def __radd__(self, other):
        if type(other) != AmountCurrency:
            return self + other

    def __mul__(self, other):
        if type(other) in (float, int):
            return AmountCurrency(self.amount * other)
        else:
            raise NotImplemented

    __rmul__ = __mul__
