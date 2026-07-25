"""Write a program to display two messages:
Press 1 to convert seconds into hours, minutes, and seconds.
Press 2 to convert days into years, months, weeks, and days."""

choice = int(input("Enter 1 or 2: "))

if choice == 1:
    seconds = int(input("Enter seconds: "))
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    sec = seconds % 60
    print("Hours:", hours)
    print("Minutes:", minutes)
    print("Seconds:", sec)
elif choice == 2:
    days = int(input("Enter days: "))
    years = days // 365
    remaining_days = days % 365
    months = remaining_days // 30
    weeks = (remaining_days % 30) // 7
    days_left = (remaining_days % 30) % 7
    print("Years:", years)
    print("Months:", months)
    print("Weeks:", weeks)
    print("Days:", days_left)
else:
    print("Invalid choice")