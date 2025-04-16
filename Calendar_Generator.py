# Monthly Calendars Generator 2022.1 | Eslam Abdullah
print('Monthly Calendars Generator 2022.1 | Eslam Abdullah\n')
month_name = (None, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
              'October', 'November', 'December')
w_0 = ('Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su')
gregorian_legend = (0, 5, 3, 1)


def file_write(calendar, month, year):
    file_name = month_name[month] + '_' + str(year) + '.txt'
    f = open(file_name, 'w')
    f.write('')
    f.close()
    calendar_text = month_name[month] + ' ' + str(year) + '\n'
    f = open(file_name, 'a')
    for w in calendar:
        for d in w:
            d = '' if d == 0 else d
            calendar_text += str(d) + '\t'
        calendar_text += '\n'
    f.write(calendar_text)
    f.close()
    f = open(file_name, "r")
    print(f.read())


def calendar_fill(first_day, month_max):
    w_1 = [0, 0, 0, 0, 0, 0, 0]
    w_2 = [0, 0, 0, 0, 0, 0, 0]
    w_3 = [0, 0, 0, 0, 0, 0, 0]
    w_4 = [0, 0, 0, 0, 0, 0, 0]
    w_5 = [0, 0, 0, 0, 0, 0, 0]
    w_6 = [0, 0, 0, 0, 0, 0, 0]
    calendar = [w_0, w_1, w_2, w_3, w_4, w_5, w_6]
    week_no = 1
    day_no = first_day
    for d in range(1, month_max+1):
        calendar[week_no][day_no] = d
        day_no += 1
        if day_no > 6:
            day_no = day_no % 7
            week_no += 1
    return calendar


def dayofweek(month_code, year_code, century_code):
    dayofweek_code = (1 + month_code + year_code + (year_code // 4) + century_code) % 7
    return dayofweek_code


def is_leap(year):
    leap = True if year % 4 == 0 else False
    if leap and year % 100 == 0 and year % 400 != 0:
        leap = False
    return leap


def calendar_input():
    month_legend = [None, 6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    month_max = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = month = 0
    while year < 1583:
        year_temp = input('Year > ')
        year = int(year_temp) if year_temp.isnumeric() else 0
    while month < 1 or month > 12:
        month_temp = input('Month > ')
        month = int(month_temp) if month_temp.isnumeric() else 0
    if is_leap(year):
        month_legend[1], month_legend[2], month_max[2] = 5, 1, 29
    century_code = gregorian_legend[int(year / 100) % 4]
    year_code = int(year % 100)
    first_day = (dayofweek(month_legend[month], year_code, century_code) - 1) % 7
    file_write(calendar_fill(first_day, month_max[month]), month, year)
    input('> ')


calendar_input()
