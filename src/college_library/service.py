def calculate_late_fee(days_overdue: int) -> int:
    if days_overdue <= 0:
        return 0
    return days_overdue * 10
