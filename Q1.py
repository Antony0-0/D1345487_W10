def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
if __name__=="__main__":
    print(is_leap_year(2020))
    print(is_leap_year(1900))
    print(is_leap_year(2000))