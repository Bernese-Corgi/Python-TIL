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
        self.available_quantity = qty
    
    def allocate(self, line: OrderLine):
        self.available_quantity -= line.qty
    
    def can_allocate(self, line: OrderLine):
        return self.sku == line.sku and self.available_quantity >= line.qty