from college_library import calculate_late_fee


def main():
    days = 3
    fee = calculate_late_fee(days)
    print(f"Дней просрочки: {days}")
    print(f"Штраф за просрочку: {fee} руб.")


if __name__ == "__main__":
    main()
