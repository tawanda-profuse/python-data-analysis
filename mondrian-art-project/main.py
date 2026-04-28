import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

pd.options.display.max_rows = 10

features = pd.read_csv('mondrian-painting-features.csv')
painting_info = pd.read_csv('mondrian-painting-info.csv') # Loading the painting info data
fp26_features = pd.read_csv('fp26-features.csv')

# Find all the features for painting b104
print(features.query('painting_id == "b104"')) 

def draw_mondrian(painting_id):
    """
    The function below draws Mondrian paintings from data. Internally, this function uses Matplotlib to draw each feature as a rectangular patch of color.
    """
    rects = features.query('painting_id == @painting_id')
    total_width = rects.eval("x + width").max()
    total_height = rects.eval("y + height").max()

    fig, ax = plt.subplots(figsize=(3, 3))

    for (idx, row) in rects.iterrows():
        x, y, w, h, rgb = row[['x', 'y', 'width', 'height', 'rgb']]
        patch = mpatches.Rectangle((x, y), w, h, facecolor=rgb)
        ax.add_patch(patch)

    ax.axis([0, total_width, 0, total_height])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.text(0.5, 0.01, painting_id, ha="center", fontsize=14)
    plt.show()

# Draw painting b104
draw_mondrian('b104')

# Grouping features by painting_id
sizes = features.groupby('painting_id').size()
complexity_df = sizes.reset_index(name='complexity')
print(complexity_df)

# Merging dataframes:
painting_info = painting_info.merge(complexity_df, on='painting_id', how='left')
print(painting_info)

# Plotting Complexity over Time. The complexity of Mondrian's paintings increases after 1935, indicating a shit in his artistic style
plt.figure(figsize=(6, 4))
plt.scatter(painting_info['year'], painting_info['complexity'])
# The 1926 painting is an outlier with much higher complexity than other paintings from that period, suggesting it might be fake:
plt.scatter(x=1926, y=54, color='red', marker='s')
plt.xlabel('Year')
plt.ylabel('Complexity')
plt.show()

# Compute the total area of each painting using data from painting_info
painting_info['area'] = painting_info['width'] * painting_info['height']
print("\nTotal area per painting:")
print(painting_info[['painting_id', 'title', 'area']])

# Identify features in the dataset where the color is 'blue'
blue_features = features[features['color'] == 'blue']
print("\nBlue features (main dataset):")
print(blue_features[['painting_id', 'x', 'y', 'width', 'height']])

# Calculate the area of the blue areas
features['feature_area'] = features['width'] * features['height']
fp26_features['feature_area'] = fp26_features['width'] * fp26_features['height']
blue_area_per_painting = (
    features[features['color'] == 'blue']
    .groupby('painting_id')['feature_area']
    .sum()
)

print("\nTotal blue area per painting:")
print(blue_area_per_painting)
