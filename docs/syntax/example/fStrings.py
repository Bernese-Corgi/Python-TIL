print(f"3 + 4 = {3 + 4}") # 3 + 4 = 7

name = "프레드"

print(f"그의 이름은 {name}입니다.") # 그의 이름은 프레드입니다.
print(f"그의 이름은 {name!r}입니다.") # 그의 이름은 '프레드'입니다.
print(f"그의 이름은 {repr(name)}입니다.") # 그의 이름은 '프레드'입니다.

import decimal
width = 10
precision = 4
value = decimal.Decimal("12.34567")

print(f"결과: {value:{width}.{precision}}") # 결과:      12.35

from datetime import datetime

today = datetime(year=2017, month=1, day=27)

print(f"{today:%B %d, %Y}") # January 27, 2017

number = 1024

print(f"{number:#0x}") # 0x400

