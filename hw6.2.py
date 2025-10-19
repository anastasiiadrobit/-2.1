seconds = int(input("Enter the number of seconds: "))

days, rem = divmod(seconds, 86400)
hours, rem = divmod(rem, 3600)
minutes, seconds = divmod(rem, 60)

if days == 1:
    day_word = "day"
elif 2 <= days <= 4:
    day_word = "days"
else:
    day_word = "days"

print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
