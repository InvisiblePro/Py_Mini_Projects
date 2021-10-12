year = int(input("\nEnter year here : "))
if year % 4 == 0:
    print("\nHurray! its leap year")
if year % 4 == 3:
    print(f"\nNext year is leap year -- {year+1}")
if year % 4 == 2:
    print(f"\nAfter 2 years is leap year -- {year+2}")
if year%4==1:
    print(f"\nOps!!, Pervious year was leap year -- {year-1}")