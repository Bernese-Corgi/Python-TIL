from datetime import date
from model import Batch, OrderLine


# 1. 할당을 위한 테스트
# 배치에 할당하는 테스트는 사용 가능한 수량을 줄입니다.
def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch = Batch(
        ref="batch-001",
        sku="SMALL-TABLE",
        qty=20,
        eta=date.today()
    )
    
    line = OrderLine(
        orderid='orderer-ref',
        sku="SMALL-TABLE",
        qty=2
    )
    
    batch.allocate(line=line)
    
    assert batch.available_quantity == 18

# 2. 할당할 수 있는 대상을 보여주는 테스트
def make_batch_and_line(sku, batch_qty, line_qty):
    return (
        Batch("batch-001", sku, batch_qty, eta=date.today()),
        OrderLine("order-123", sku, line_qty)
    )

# 테스트는 사용 가능한 경우 필요한 것보다 더 많이 할당할 수 있습니다.
def test_can_allocate_if_available_greater_than_required():
    (large_batch, small_line) = make_batch_and_line(
        sku="ELEGANT-LAMP",
        batch_qty=20,
        line_qty=2
    )
    assert large_batch.can_allocate(small_line)

# 필요한 것보다 작은 사용 가능한 경우 테스트에서 할당할 수 없음
def test_cannot_allocate_if_available_smaller_than_required():
    (small_batch, large_line) = make_batch_and_line(
        sku="ELEGANT-LAMP",
        batch_qty=2,
        line_qty=20
    )
    assert small_batch.can_allocate(large_line) is False

# 테스트는 사용 가능한 경우 필수 항목과 동일하게 할당할 수 있습니다.
def test_can_allocate_if_available_equal_to_required():
    (batch, line) = make_batch_and_line(
        sku="ELEGANT-LAMP",
        batch_qty=2,
        line_qty=2
    )
    assert batch.can_allocate(line)

# sku가 일치하지 않으면 테스트에서 할당할 수 없습니다.
def test_cannot_allocate_if_skus_do_not_match():
    batch = Batch(
        ref="batch-001",
        sku="UNCONFORTABLE-CHAIR",
        qty=100,
        eta=None
    )
    differnt_sku_line = OrderLine(
        orderid="orer-123",
        sku="EXPENSIVE-TOASTER",
        qty=10
    )
    assert batch.can_allocate(differnt_sku_line) is False

# 테스트는 할당된 줄만 할당 해제할 수 있습니다.
def test_can_only_deallocate_allocated_lines():
    batch, unallocated_line = make_batch_and_line(
        sku="DECORATIVE-TRINKET",
        batch_qty=20,
        line_qty=2
    )

    batch.deallocate(unallocated_line)

    assert batch.available_quantity == 20

# 테스트 할당은 멱등적입니다.
def test_allocation_is_idempotent():
    batch, line = make_batch_and_line(
        sku="ANGULAR-DESK",
        batch_qty=20,
        line_qty=2
    )
    batch.allocate(line)
    batch.allocate(line)
    assert batch.available_quantity == 18
