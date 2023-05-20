from collections import namedtuple
from dataclasses import dataclass
from typing import NamedTuple


# dataclass
@dataclass(frozen=True)
class Name:
    first_name: str
    surname: str

# NamedTuple
class Money(NamedTuple):
    currency: str
    value: int

# namedtuple
Line = namedtuple('Line', ['sku', 'qty'])

def test_equality():
    # 값들이 같으면 값객체도 같다고 간주
    print(Money('gdp', 10) == Money('gdp', 10)) # True
    print(Name('Harry', 'Percival') == Name('Bob', 'Gregory')) # False
    print(Line('RED-CHAIR', 5) == Line('RED-CHAIR', 5)) # True

test_equality()

# ---------------------------------- 값객체의 연산 --------------------------------- #
fiver = Money('gdp', 5)
tenner = Money('gdp', 10)

def can_add_money_values_for_the_same_currency():
    # currency가 같으면 value 값을 더할 수 있다.
    print(fiver + fiver == tenner)

def can_subtract_money_values():
    # currency가 같으면 value 값을 뺄 수 있다.
    print(tenner - fiver == fiver)