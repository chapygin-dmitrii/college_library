from college_library.service import calculate_late_fee


def test_late_fee_zero_days():
    assert calculate_late_fee(0) == 0


def test_late_fee_three_days():
    assert calculate_late_fee(3) == 30
