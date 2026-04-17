import pandas as pd
import matplotlib.pyplot as plt

survey = pd.read_csv('coffee-survey-results.csv')
print("\nDataset Columns:\n")
print(survey.columns)

# Selecting the needed columns from the survey:
needed_columns = [
    "What kind of dairy? (Whole milk)",
    "What kind of dairy? (Skim milk)",
    "What kind of dairy? (Half and half)",
    "What kind of dairy? (Coffee creamer)",
    "What kind of dairy? (Flavored creamer)",
    "What kind of dairy? (Oat milk)",
    "What kind of dairy? (Almond milk)",
    "What kind of dairy? (Soy milk)"
]
dairy = survey[needed_columns]
print("\n8 Narrowed down columns of dairy preferences:\n")
print(dairy)

# Renaming the columns using name map, e.g. 'What kind of dairy? (Whole milk)' becomes 'Whole milk'
name_map = {
    'What kind of dairy? (Whole milk)': 'Whole milk',
    'What kind of dairy? (Skim milk)': 'Skim milk',
    'What kind of dairy? (Half and half)': 'Half and half',
    'What kind of dairy? (Coffee creamer)': 'Coffee creamer',
    'What kind of dairy? (Flavored creamer)': 'Flavored creamer',
    'What kind of dairy? (Oat milk)': 'Oat milk',
    'What kind of dairy? (Almond milk)': 'Almond milk',
    'What kind of dairy? (Soy milk)': 'Soy milk',
}
dairy = dairy.rename(columns=name_map)
print("\nRenamed columns:\n", dairy)
print(dairy.isna().sum())

# Calculate the percentage for each dairy
dairy_preferences = dairy.mean() * 100
print("\nDairy preferences:\n", dairy_preferences.sort_values())

# Visualizing the data using a horizontal bar chart:
plt.figure(figsize=(6,3))
plt.barh(dairy_preferences.index, dairy_preferences)
plt.xlabel("Percent")
plt.show()