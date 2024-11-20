def get_start_day(year, month):
    if month == 1 or month == 2:
        month += 12
        year -= 1
    k = year % 100 
    j = year // 100 
    day = (1 + (13 * (month + 1)) // 5 + k + (k // 4) + (j // 4) - (2 * j)) % 7
    return (day + 5) % 7

if __name__=="__main__":
    print(get_start_day(2023, 11)) 
    print(get_start_day(2024, 2)) 