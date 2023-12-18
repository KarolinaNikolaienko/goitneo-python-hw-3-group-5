from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    birthdays_on_week = defaultdict(list)
    today = datetime.now().date()
    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # враховуючи поточний день today, знайдемо перший день наступного тижня,
    # тиждень у даному випадку буде починатися З СУБОТИ і закінчуватісь П'ЯТНИЦЕЮ
    # тоді ми зможемо дізнатись дні народження, які припадають на ці вихідні та на наступний робочий тиждень
    # і власне перенести ті дні народження, які припали на вихідні, на наступний понеділок
    
    if today.weekday() < 5: # якщо поточний день понеділок - п'ятниця
        first_day_of_week = today + timedelta(days = 5 - today.weekday())
    elif today.weekday() == 6: # якщо сьогодні неділя
        first_day_of_week = today - timedelta(days = 1)
    
    for user in users:
        name = user['name']
        birthday = user['birthday']
        birthday_this_year = birthday.replace(year = today.year)

        if birthday_this_year < first_day_of_week:
            birthday_this_year = birthday_this_year.replace(year = birthday_this_year.year + 1)
        delta_days = (birthday_this_year - first_day_of_week).days
        if delta_days < 7:
            day = birthday_this_year.strftime('%A')
            if day in ['Saturday', 'Sunday']:
                birthdays_on_week['Monday'].append(name)
            else:
                birthdays_on_week[day].append(name)
    
    birthdays_on_week = dict(sorted(birthdays_on_week.items(), key = lambda d: day_order.index(d[0])))
    
    return birthdays_on_week