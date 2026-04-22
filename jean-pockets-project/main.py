import pandas as pd

df = pd.read_csv('jean-pocket-measurements.csv')

# What is the average difference in pocket height_front between women's and men's jeans?
df['is_woman'] = df['gender'] == 'women'
womens_height_front_avg = df['is_woman'].mean() * 100
mens_height_front_avg = (df['is_woman'] == False).mean() * 100
average_diff = womens_height_front_avg - mens_height_front_avg
print(f"Average difference between women's ({womens_height_front_avg}%) and men's({mens_height_front_avg}%) jeans is: {average_diff}%")

# Is there a significant difference in pocket height_front between skinny and straight styles within the same gender?
womens_straight_hf = df.query('style == "straight" and gender == "women"').sum()['height_front']
womens_skinny_hf = df.query('style == "skinny" and gender == "women"').sum()['height_front']
mens_straight_hf = df.query('style == "straight" and gender == "men"').sum()['height_front']
mens_skinny_hf = df.query('style == "skinny" and gender == "men"').sum()['height_front']

print("\nWomen's pocket height_front difference between skinny and straight: ", womens_straight_hf - womens_skinny_hf)
print("\nMen's pocket height_front difference between skinny and straight: ", mens_skinny_hf - mens_straight_hf)

# How do back pocket sizes compare between women's and men's jeans?
womens_height_back = df.query('gender == "women"').sum()['height_back']
womens_width_back = df.query('gender == "women"').sum()['width_back']
mens_height_back = df.query('gender == "men"').sum()['height_back']
mens_width_back = df.query('gender == "men"').sum()['width_back']

print("\nComparison of back pocket sizes:")
print("Women's height back:", womens_height_back)
print("Women's width back:", womens_width_back)
print("Men's height back:", mens_height_back)
print("Men's width back:", mens_width_back)

# Based on my phones height (162.2 mm or 16.22 cm), what percentage of women's and men's jeans can comfortably fit the phone in the their pockets.
womens_percentage_fit = (len(df.query('gender == "women"')[df['height_front'] > 16.22]) / len(df.query('gender == "women"'))) * 100
mens_percentage_fit = (len(df.query('gender == "men"')[df['height_front'] > 16.22]) / len(df.query('gender == "men"'))) * 100

print("\nPhone height = 162.2 mm or 16.22 cm")
print(f"Women's percentage fit: {womens_percentage_fit}%")
print(f"Men's percentage fit: {mens_percentage_fit}%")