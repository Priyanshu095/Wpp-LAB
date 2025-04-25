# Given a dataset of concerts, count the number of concerts per (artist, venue), per year
# month. Make the resulting table be a wide table - one row per year month with a column
# for each unique (artist, venue) pair. Use the cross product of the artists and venues Series
# to determine which (artist, venue) pairs to include in the result.
import pandas as pd
import itertools


data = {
    'artist': ['Arijit', 'Ed Sheeran', 'Arijit', 'Weeknd', 'Ed Sheeran', 'Arijit', 'Weeknd'],
    'venue': ['Ahmedabad', 'Mumbai', 'Bengaluru', 'Mumbai', 'Ahmedabad', 'Bengaluru', 'Bengaluru'],
    'date': ['2025-01-15', '2025-01-20', '2025-02-10', '2025-02-15', '2025-02-20', '2025-03-05', '2025-03-10']
}

concerts_df = pd.DataFrame(data)
concerts_df['date'] = pd.to_datetime(concerts_df['date'])


concerts_df['year_month'] = concerts_df['date'].dt.to_period('M')


artists = concerts_df['artist'].unique()
venues = concerts_df['venue'].unique()

artist_venue_pairs = pd.DataFrame(itertools.product(artists, venues), columns=['artist', 'venue'])

grouped = concerts_df.groupby(['year_month', 'artist', 'venue']).size().reset_index(name='count')


merged_df = pd.merge(
    artist_venue_pairs.assign(key=1),
    grouped.assign(key=1),
    on=['artist', 'venue', 'key'],
    how='outer'
).drop('key', axis=1)


merged_df['count'] = merged_df['count'].fillna(0).astype(int)


wide_table = merged_df.pivot_table(
    index='year_month',
    columns=['artist', 'venue'],
    values='count',
    fill_value=0
)


wide_table = wide_table.reset_index()


print(wide_table)