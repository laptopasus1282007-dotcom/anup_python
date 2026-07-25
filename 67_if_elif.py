"""Write a program to display two messages:
Press 1 to convert an amount into 500, 50, 10, and 1 rupee notes.
Press 2 to convert an amount into 200, 100, 20, 5, and 2 rupee notes."""

choice = int(input("Enter 1 or 2: "))
amount = int(input("Enter amount: "))

if choice == 1:
    notes_500 = amount // 500
    remaining = amount % 500
    notes_50 = remaining // 50
    remaining %= 50
    notes_10 = remaining // 10
    remaining %= 10
    notes_1 = remaining // 1

    print("500 rupee notes:", notes_500)
    print("50 rupee notes:", notes_50)
    print("10 rupee notes:", notes_10)
    print("1 rupee notes:", notes_1)
elif choice == 2:
    notes_200 = amount // 200
    remaining = amount % 200
    notes_100 = remaining // 100
    remaining %= 100
    notes_20 = remaining // 20
    remaining %= 20
    notes_5 = remaining // 5
    remaining %= 5
    notes_2 = remaining // 2
    notes_1 = remaining % 2

    print("200 rupee notes:", notes_200)
    print("100 rupee notes:", notes_100)
    print("20 rupee notes:", notes_20)
    print("5 rupee notes:", notes_5)
    print("2 rupee notes:", notes_2)
    print("1 rupee notes:", notes_1)
else:
    print("Invalid choice")