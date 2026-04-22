import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('largest-islands.csv')

# What are the 10 largest islands in the tropics?
tropics = df[df['climate'] == 'tropics']
top10_tropics = tropics.sort_values(by='area', ascending=False).head(10)
print("Top 10 Largest Islands in the tropics:")
print(top10_tropics[['island', 'area', 'region']])

# What are the largest islands in each region?
largest_islands_per_region = df.loc[df.groupby('region')['area'].idxmax()]

print("\nLargest island in each region:")
print(largest_islands_per_region[['region','island','area']])

# Create a line graph with area on the y-axis and rank on the x-axis. The data should be ordered by rank, from largest to smallest
df_sorted = df.sort_values(by='rank')

plt.plot(df_sorted['rank'], df_sorted['area'], marker='o')
plt.xlabel('Rank (1 = largest)')
plt.ylabel('Area')
plt.title('Island Area vs Rank')
plt.tight_layout()
plt.show()

# What islands are composed of multiple countries?
multi_country = df[df['countries'].str.contains(',', na=False)]

print('\nIslands with multiple countries:')
print(multi_country[['island', 'countries', 'region']])