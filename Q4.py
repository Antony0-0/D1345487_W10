from Q2 import get_days_in_month
from Q3 import get_start_day

def display_calendar(year, month):
    days_in_month = get_days_in_month(year, month)
    start_day = get_start_day(year, month)

    if isinstance(days_in_month, str):
        print(days_in_month)
        return
    print(f" {year}年 {month}月")
    print("Mo Tu We Th Fr Sa Su")
    calendar = ["   "] * start_day
    for day in range(1, days_in_month + 1):
        calendar.append(f"{day:2} ")
    for i in range(0, len(calendar), 7):
        print("".join(calendar[i:i + 7]))
        
if __name__=="__main__":
    display_calendar(2023, 11)