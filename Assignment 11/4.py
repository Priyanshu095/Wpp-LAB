# Whenever your friends John and Judy visit you together, y’all have a party. Given a
# DataFrame with 10 rows representing the next 10 days of your schedule and whether John
# and Judy are scheduled to make an appearance, insert a new column
# called days_til_party that indicates how many days until the next party.
# days_til_party should be 0 on days when a party occurs, 1 on days when a party doesn’t
# occur but will occur the next day, etc.
import pandas as pd


data = {
    'Day': range(1, 11),
    'John': [1, 0, 1, 1, 0, 0, 1, 0, 0, 1], 
    'Judy': [1, 0, 1, 0, 0, 1, 1, 0, 0, 1], 
}

df = pd.DataFrame(data)


df['Party'] = (df['John'] & df['Judy']).astype(int)

days_until_party = []
next_party_day = -1

for index in range(len(df) - 1, -1, -1):
    if df.loc[index, 'Party'] == 1:
        next_party_day = 0
    days_until_party.insert(0, next_party_day)
    if next_party_day >= 0:
        next_party_day += 1

df['days_til_party'] = days_until_party
df = df.drop(columns=['Party'])
print(df)