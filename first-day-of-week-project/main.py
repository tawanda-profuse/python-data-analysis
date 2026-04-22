import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('first-day-of-week.csv')
pop = pd.read_csv('population.csv')
regions = pd.read_csv('four-regions.csv')

# How many territories show Friday, Saturday, Sunday, and Monday as the first_day of the week?
friday_territories = (df['first_day'] == 'fri').sum()
saturday_territories = (df['first_day'] == 'sat').sum()
sunday_territories = (df['first_day'] == 'sun').sum()
monday_territories = (df['first_day'] == 'mon').sum()

print("\nTerritory totals for the first day of the week:")
print({
    'Friday': int(friday_territories), 
    'Saturday': int(saturday_territories),
    'Sunday': int(sunday_territories),
    'Monday': int(monday_territories)
    })


# How many people start the week on Friday, Saturday, Sunday, and Monday?
days = ['fri','sat','sun','mon']
df_pop = df.merge(pop, on='alpha3', how='left')
population_counts = (
    df_pop[df_pop['first_day'].isin(days)]
    .groupby('first_day')['population']
    .sum()
)
print("\nPopulation by first day of week:")
print(population_counts)

# Which of the four_regions predominantly start the week on Sunday? On Monday? Are there any regions that are more divided between Sunday and Monday?
df_full = df.merge(regions, on='alpha3', how='left')

region_day_counts = (
    df_full[df_full['first_day'].isin(['sun', 'mon'])]
    .groupby(['four_regions', 'first_day'])
    .size()
    .unstack(fill_value=0)
)

print("\nRegion vs first day counts:")
print(region_day_counts)

# Visualizing the data
data = region_day_counts[['sun', 'mon']].plot(kind='bar')
plt.xlabel("Region")
plt.ylabel("Number of Territories")
plt.title("First Day of Week by Region")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()