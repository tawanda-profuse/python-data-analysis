# Python Data Analysis

This repository contains multiple data analysis projects that make use of essential data cleaning techniques, including splitting columns, converting data types, handling NaN values, and organizing datasets effectively.

All of the projects in this repository use Python, the modules used in this project are Pandas for data cleaning and Matplotlib for visualization.

## Installing Python Modules

- `python -m pip install pandas matplotlib`

## Projects

- [Coffee Survey Results](/coffee-survey-project/main.py) - In this project, a survey dataset of approximately 1000 coffee enthusiasts is analyzed to identify the most popular dairy choices. These findings will help to recommend which dairy alternatives should be stocked by a new specialty coffee shop.
- [Emoji Sentiment](/emoji-sentiment-project/main.py) - This project uses a CSV dataset and aims to discover if popular emojis are generally associated with positive or negative sentiments. Researchers examined 1.6 million tweets. Each tweet was labeled by annotators as positive, negative, or neutral. About 4% of these tweets included emojis. This project uses Python to add new columns and answer questions such as, "what percentage of emojis in the dataset have a positive sentiment?"
- [First Day of the Week](/first-day-of-week-project/main.py) - In this project, we aim to answer whether more countries start the week on Sunday or Monday. What about people? What about by continent? The file [first-day-of-week.csv](/first-day-of-week-project/first-day-of-week.csv) shows the first day of the week for each territory. The file [population.csv](/first-day-of-week-project/population.csv) shows the population in the year 2020 for each territory in millions, and the file [four-regions.csv](/first-day-of-week-project/four-regions.csv) specifies whether each territory is in asia, europe, africa, or the americas.
- [Flight Delays project](/flight-delays-project/main.py) - In this project, we work with airport flight data and explore how the day of week affects the likelihood of a delayed departure.
- [Jean Pockets Project](/jean-pockets-project/main.py) - In this project, we analyze a dataset for the jean sizes of men and women. The file [jean-pocket-measurements.csv](/jean-pockets-project/jean-pocket-measurements.csv) shows pocket measurements for 20 popular brands. Four pairs of jeans from each brand were measured: men's and women's skinny and straight styles. All jeans were designated a 32-inch waistband.
- [Largest Islands Project](/largest-islands-project/main.py) - In this project, we use a dataset named [largest-islands.csv](/largest-islands-project/largest-islands.csv) which contains information about the 100 largest islands in the world. The unit for the **area** column is km2. We then use this dataset to answer some questions and create a line graph that compares area and rank.
- [Mondrian Art Project](/mondrian-art-project/main.py) - Piet Mondrian was a Dutch artist best known for his abstract, grid-like designs during the 1920s and 30s. In this project, we will explore Mondrian's quest for artistic simplicity and try our hands at detecting fake paintings falsely attributed to Mondrian. By representing art as data, we open up artistic analysis to a broad range of data science techniques.

## License

This project is available for use under a MIT License.
