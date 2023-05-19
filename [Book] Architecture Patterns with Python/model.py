from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class OrderLine:
    orderid: str # 주문 참조 번호
    sku: str # 제품 식별자
    qty: int # 수량

class Batch:
    def __init__(
        self,
        ref: str,
        sku: str,
        qty: int,
        eta: Optional[date]
    ):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty
        self._allocations = set() # type Set[OrderLine]
    
    def allocate(self, line: OrderLine):
        if self.can_allocate(line): # 가용 수량이 충분하면
            self._allocations.add(line) # 이를 set에 추가하기만 한다.
    
    def deallocate(self, line: OrderLine):
        if line in self._allocations: # 라인이 존재하면
            self._allocations.remove(line) # 할당을 해제한다.

    @property
    def allocated_quantity(self) -> int:
        # 할당수량 = 할당된 집합에 있는 qty 수량 합계
        return sum(line.qty for line in self._allocations)
    
    @property
    def available_quantity(self) -> int:
        # 가용수량 = 구매수량 - 할당수량
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty