import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the data
df = pd.read_csv(r'D:\Coding\FreeCodeCamp\Sea Level Predictor\epa-sea-level.csv')

def draw_plot():
    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Create first line of best fit for all data
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_level_prediction = slope * years_extended + intercept
    plt.plot(years_extended, sea_level_prediction, color='red', label='Best Fit Line (1880 - 2050)')

    # Create second line of best fit for data from year 2000 onwards
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_2000_extended = pd.Series(range(2000, 2051))
    sea_level_prediction_2000 = slope_2000 * years_2000_extended + intercept_2000
    plt.plot(years_2000_extended, sea_level_prediction_2000, color='green', label='Best Fit Line (2000 - 2050)')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    plt.grid()

    # Save the plot
    plt.savefig('sea_level_plot.png')
    plt.show()

# Call the function to draw the plot
draw_plot()
