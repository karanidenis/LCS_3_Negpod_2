month = str(input("enter month to check days:"))
if month == 'February':
    print("The month of {} has 28 or 29 days". format(month))
elif month in ['April', 'June','September','November']:
    print("The month of {} has 30 days". format(month))
else:
    print("The month of {} has 31 days".format(month))