# Follow the assignment instructions to code an app that
# will tell a user their birthstone.

user_input = input("Enter the number of the month you were born (1-12) >>")
month = int(user_input)
print("You have entered:", month)

if month == 1:
    print("Your birthstone is garnet.")
elif month == 2:
    print("Your birthstone is amethyst.")
elif month == 3:
    print("Your birthstone is aquamarine.")
elif month == 4:
    print("Your birthstone is diamond.")
elif month == 5:
    print("Your birthstone is emerald.")
elif month == 6:
    print("Your birthstone is alexandrite.")
elif month == 7:
    print("Your birthstone is ruby.")
elif month == 8:
    print("Your birthstone is periot.")
elif month == 9:
    print("Your birthstone is sapphire.")
elif month == 10:
    print("Your birthstone is pink tourmaline.")
elif month == 11:
    print("Your birthstone is topaz.")
else:
    print("Your birthstone is blue topaz.")
