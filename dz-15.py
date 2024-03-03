date_num = 7948799

day_string = ""

days, hours_sec = divmod(date_num, (24 * 60 * 60))
hours, minutes_sec = divmod(hours_sec, (60*60))
minutes, seconds = divmod(minutes_sec, 60)

if days % 10 == 1 and days > 20 or days == 1:
    day_string = "день"
elif 2 <= days % 10 < 5 and 10 <= days < 20:
    day_string = "днів"
elif 2 <= days % 10 < 5:
    day_string = "дні"
else:
    day_string = "днів"

print(f"{days} {day_string}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
