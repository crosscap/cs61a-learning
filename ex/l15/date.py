def date_demos():
    from datetime import date
    today = date(2020, 2, 24)
    freedom = date(2020, 5, 12)
    str(freedom - today)
    today.year
    today.strftime('%A, %B %d')
    type(today)

