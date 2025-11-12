import calendar

month, day, year = map(int,input().split())

if year > 2000:
    print(calendar.day_name[calendar.weekday(year, month, day)].upper())