def retireyear_calculator():
    age = raw_input("Enter your current age")
    retire_age = raw_input("Enter the age u wanna retire")
    time_left = int(retire_age)-int(age)
    import datetime
    year = datetime.date.today().year
    retire_year = year + time_left
    print "Current year is %d" %year
    print "your desired retirement year is %d" %retire_year

retireyear_calculator()
