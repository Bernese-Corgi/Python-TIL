from datetime import date, timedelta
from model import Batch, OrderLine, allocate

# 테스트는 배송보다 현재 재고 배치를 선호합니다.
def test_prefers_current_stock_batches_to_shipments():
    in_stock_batch = Batch(
        ref="in-stock-batch", 
        sku="RETRO-CLOCK",
        qty=100,
        eta=None
    )
    shipment_batch = Batch(
        ref="shipment-batch", 
        sku="RETRO-CLOCK",
        qty=100,
        eta=date.today() + timedelta(days=1)
    )
    line = OrderLine(
        orderid="oref",
        sku="RETRO-CLOCK",
        qty=10
    )
    
    allocate(line, [in_stock_batch, shipment_batch])
    
    assert in_stock_batch.available_quantity == 90
    assert shipment_batch.available_quantity == 100

# 테스트는 이전 배치를 선호합니다.
def test_prefers_earlier_batches():
    earliest = Batch(
        ref="speedy-batch",
        sku="MINIMALIST-SPOON",
        qty=100,
        eta=date.today()
    )
    medium = Batch(
        ref="normal-batch",
        sku="MINIMALIST-SPOON",
        qty=100,
        eta=date.today() + timedelta(days=1)
    )
    latest = Batch(
        ref="slow-batch",
        sku="MINIMALIST-SPOON",
        qty=100,
        eta=date.today() + timedelta(weeks=1)
    )
    line = OrderLine(
        orderid="order1",
        sku="MINIMALIST-SPOON",
        qty=10
    )
    
    allocate(line, [medium, earliest, latest])
    
    assert earliest.available_quantity == 90
    assert medium.available_quantity == 100
    assert latest.available_quantity == 100

# 테스트는 할당된 배치 참조를 반환합니다.
def test_returns_allocated_batch_ref():
    in_stock_batch = Batch(
        ref="in-stock-batch-ref",
        sku="HIGHBROW-POSTER",
        qty=100,
        eta=None
    )
    shipment_batch = Batch(
        ref="shipment-batch-ref",
        sku="HIGHBROW-POSTER",
        qty=100,
        eta=date.today() + timedelta(days=1)
    )
    line = OrderLine(
        orderid="oref",
        sku="HIGHBROW-POSTER",
        qty=10
    )
    
    allocation = allocate(line, [in_stock_batch, shipment_batch])
    
    assert allocation == in_stock_batch.reference