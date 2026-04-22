import pandas as pd
import matplotlib.pyplot as plt

flights = pd.read_csv('flights.csv')
flights = flights.convert_dtypes()
pd.options.mode.chained_assignment = None
passengers = pd.read_csv('us-daily-passengers.csv')

# Extract scheduled and actual columns:
departures = flights[['scheduled', 'actual']]

# Convert strings to datetime:
departures['scheduled'] = pd.to_datetime(departures['scheduled'])
departures['actual'] = pd.to_datetime(departures['actual'])
# Calculate the delays:
departures['delay'] = departures.eval('actual - scheduled')
# New column to flag flights as late:
departures['is_late'] = departures['delay'].dt.total_seconds() > 900
# Get the day of the week:
departures['day_name'] = departures['actual'].dt.strftime('%a')
# Percentage of flights delayed by day of week:
proportion_delayed = departures.groupby('day_name')['is_late'].mean()
percent_delayed = proportion_delayed * 100
print(departures.head(10))
print("\nPercentage of delayed flights:\n", percent_delayed)
# Plotting the data:
new_index_order = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
percent_delayed = percent_delayed.reindex(new_index_order)
plt.figure(figsize=(6,3))
plt.bar(percent_delayed.index, percent_delayed)
plt.ylabel('Percent Delayed')
plt.show()

# Passengers Data:
passengers['date'] = pd.to_datetime(passengers['date'])
passengers['day_name'] = passengers['date'].dt.strftime('%a')
print(passengers.head(10))

# Creating a graph that shows the average number of passengers flying per day of the week
passengers_per_day = passengers.groupby('day_name')['num_passengers'].mean()
print("\nPassengers Flying per Day:\n", passengers_per_day)

# Plotting the data:
passengers_flying = passengers_per_day.reindex(new_index_order)
plt.figure(figsize=(6,3))
plt.bar(passengers_flying.index, passengers_flying)
plt.ylabel('Passengers Flying per Day')
plt.show()
