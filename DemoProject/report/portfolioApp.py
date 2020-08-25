# @date 2020-08-25
# @author Yu Tongxin(Front)
# I think I should define special exception in __init__ for special input type or value
# but remote is shutting down, so I may think over it later


class Currency:
    def __init__(self, iso, name):
        self.iso = iso
        self.name = name

    def __str__(self):
        return "iso:" + self.iso + ", name:" + self.name

    def __repr__(self):
        return "iso:" + self.iso + ", name:" + self.name


class Address:
    def __init__(self, line1, line2, city, tel):
        self.line1 = line1
        self.line2 = line2
        self.city = city
        self.tel = tel

    def __str__(self):
        return self.line1 + ", " + self.line2 \
               + ", " + self.city + ", " + self.tel

    def __repr__(self):
        return self.line1 + ", " + self.line2 \
               + ", " + self.city + ", " + self.tel


class Exchange:
    def __init__(self, name, currency, address):
        self.name = name
        self.currency = currency
        self.address = address

    def __str__(self):
        return f"name: {self.name} currency: {self.currency}  {self.address}"

    def __repr__(self):
        return f"name: {self.name} currency: {self.currency}  {self.address}"


class Security:
    def __init__(self, ticker, name, exchange):
        self.ticker = ticker
        self.name = name
        self.exchange = exchange

    def __str__(self):
        return f"ticker:{self.ticker} name:{self.name} {self.exchange}"

    def __repr__(self):
        return f"ticker:{self.ticker} name:{self.name} {self.exchange}"


class Price:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Price(self.value + other.value)

    def __mul__(self, other):
        return Price(self.value * other.value)

    def __sub__(self, other):
        return Price(self.value - other.value)

    def __truediv__(self, other):
        return Price(self.value / other.value)

    def __str__(self):
        return "value:" + str(self.value)

    def __repr__(self):
        return "value:" + str(self.value)


class Position:
    def __init__(self, sec, price, qyt):
        self.sec = sec
        self.price = price
        self.qyt = qyt

    def __str__(self):
        return f"{self.sec}\t{self.price}\tqty:{self.qyt}"

    def __repr__(self):
        return f"{self.sec}\t{self.price}\tqty:{self.qyt}"


class LegalEntity:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"name:{self.name}\t {self.address}"

    def __repr__(self):
        return f"name:{self.name}\t {self.address}"


class Equity(Security):
    def __init__(self, ticker, name, exchange):
        super().__init__(ticker, name, exchange)

    def __str__(self):
        return f"ticker:{self.ticker}\tname:{self.name}\t{self.exchange}"

    def __repr__(self):
        return f"ticker:{self.ticker}\tname:{self.name}\t{self.exchange}"


class Bond(Security):
    def __init__(self, ticker, name, exchange, isin, coupon, maturity, issuer):
        super().__init__(ticker, name, exchange)
        self.isin = isin
        self.coupon = coupon
        self.maturity = maturity
        self.issuer = issuer
        self.exchange = exchange

    def __str__(self):
        return f"{super().__str__()}\tisin:{self.isin}\tcoupon:{self.coupon}\t" \
               f"maturity:{self.maturity}\tissuer:{self.issuer}"

    def __repr__(self):
        return f"{super().__str__()}\tisin:{self.isin}\tcoupon:{self.coupon}\t" \
               f"maturity:{self.maturity}\tissuer:{self.issuer}"


def main_run():
    #Assignment 1
    currency = Currency("GBP", "Pounds Sterling")
    print("currency:", currency)

    address = Address("Huixian Rd.", "Gaoxin District", "Dalian", "3977")
    print("address:", address)

    exchange = Exchange("NYSE", currency, address)
    print("exchange:", exchange)

    security = Security("FB", "Facebook", exchange)
    print("security:", security)

    a1 = Price(6.0)
    a2 = Price(3.0)
    print("a1 + a2\t", a1 + a2)
    print("a1 - a2\t", a1 - a2)
    print("a1 * a2\t", a1 * a2)
    print("a1 / a2\t", a1 / a2)

    price = Price(12.0)
    print("price:", price)

    #Assigment2
    qyt = 100
    position = Position(security, price, qyt)
    print("position: ", position)

    legalEntity = LegalEntity("CompanyRepre", address)
    print("legalEntity:", legalEntity)

    equity = Equity("FB", "Facebook", exchange)
    print("equity:", equity)

    bond = Bond("FB", "Facebook", exchange, "0411", 0.5, "Dec 2030", "Issuer")
    print("bond:", bond)


main_run()
