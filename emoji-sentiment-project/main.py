import pandas as pd

df = pd.read_csv('emoji-sentiment.csv')

# Adding new columns
df['sentiment'] = (df['Pos [0...1]'] - df['Neg [0...1]']) * 100
df['positive_flag'] = df['sentiment'] > 50

# Remove unnecessary columns
needed_columns = df[[
    "Char",
    "Occurrences [5...max]",
    "Position [0...1]",
    "Neg [0...1]",
    "Neut [0...1]",
    "Pos [0...1]",
    "Unicode name",
    "sentiment",
    "positive_flag"
]]

# Rename columns
name_map = {
    'Char': 'character',
    'Occurrences [5...max]': 'occurrences',
    'Position [0...1]': 'position',
    'Neg [0...1]': 'negative_sentiments',
    'Neut [0...1]': 'neutral_sentiments',
    'Pos [0...1]': 'positive_sentiments',
    'Unicode name': 'unicode_name'
}
emoji_sentiments = needed_columns.rename(columns=name_map)

print(emoji_sentiments)

# What percentage of emojis in the dataset have a positive sentiment?
positive_emojis = df[df['sentiment'] > 50]
percentage_positive = (len(positive_emojis) / len(df)) * 100
print(f"Percentage of emojis with positive sentiment: {percentage_positive:.2f}%")

# What percentage of the top 20 most popular emojis are positive?
top20 = df.sort_values(by='Occurrences [5...max]', ascending=False).head(20)
positive_top20 = top20[top20['sentiment'] > 50]
percentage_top20_positive = (len(positive_top20) / len(top20)) * 100
print(f"Percentage of top 20 emojis that are positive: {percentage_top20_positive:.2f}%")

# Which emoji (with more than 500 mentions) is the most positive?
popular = df[df['Occurrences [5...max]'] > 500]
most_positive = popular.loc[popular['sentiment'].idxmax()]
print("\nMost positive emoji (>500 mentions):")
print(most_positive)

# Which emoji (with more than 500 mentions) is the most negative?
most_negative = popular.loc[popular['sentiment'].idxmin()]
print("\nMost negative emoji (>500 mentions):")
print(most_negative)

# Where in the tweets are most emojis located (i.e. at the beginning or the end)?
average_position = df['Pos [0...1]'].mean()
print(f"\nAverage emoji position: {average_position:.2f}")

if average_position < 0.5:
    print("Emojis tend to appear at the beginning of tweets.")
else:
    print("Emojis tend to appear at the end of tweets.")

# Is there a difference in the placement of positive versus negative emojis within a tweet?
positive_positions = df[df['sentiment'] > 0]['Pos [0...1]'].mean() 
negative_positions = df[df['sentiment'] < 0]['Pos [0...1]'].mean() 

print(f"\nAverage position (positive emojis): {positive_positions:.2f}")
print(f"Average position (negative emojis): {negative_positions:.2f}")