from dataclasses import dataclass
from datetime import date
from typing import List, Optional


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
    
    # 동등성 비교
    def __eq__(self, other) -> bool:
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference
    
    def __hash__(self) -> int:
        return hash(self.reference)
    
    def __gt__(self, other):
        if self.eta is None: return False
        if other.eta is None: return True
        return self.eta > other.eta
    
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

# 도메인 서비스 함수 : 주어진 배치 집합에 대해 주문 라인을 할당하는 함수
def allocate(line: OrderLine, batches: List[Batch]) -> str:
    batch = next(b for b in sorted(batches) if b.can_allocate(line))
    batch.allocate(line)
    return batch.reference