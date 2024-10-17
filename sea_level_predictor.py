import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Step 1: Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Step 2: Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Step 3: Create first line of best fit
    line1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series([i for i in range(1880, 2051)])
    plt.plot(years_extended, line1.intercept + line1.slope * years_extended, 'r', label='Best fit line 1880-2050')

    # Step 4: Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    line2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series([i for i in range(2000, 2051)])
    plt.plot(years_recent, line2.intercept + line2.slope * years_recent, 'green', label='Best fit line 2000-2050')

    # Step 5: Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Step 6: Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
