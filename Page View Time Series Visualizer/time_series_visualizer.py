import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv(r'D:\Coding\FreeCodeCamp\Page View Time Series Visualizer\fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean the data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['value'], color='blue', linewidth=2)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('line_plot.png')
    plt.show()

def draw_bar_plot():
    # Prepare data for bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    avg_page_views = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot
    plt.figure(figsize=(12, 6))
    avg_page_views.plot(kind='bar', legend=True)
    plt.title('Average Daily Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('bar_plot.png')
    plt.show()

def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month  # Get month as a number (1-12)

    # Draw box plots
    plt.figure(figsize=(12, 6))

    # Year-wise Box Plot
    plt.subplot(1, 2, 1)
    sns.boxplot(data=df_box, x='year', y='value')
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')

    # Month-wise Box Plot
    plt.subplot(1, 2, 2)
    sns.boxplot(data=df_box, x='month', y='value')
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')

    # Set x-ticks to be the month names for better readability
    plt.xticks(ticks=range(12), labels=['January', 'February', 'March', 'April', 'May', 
                                         'June', 'July', 'August', 'September', 'October', 
                                         'November', 'December'])

    plt.tight_layout()
    plt.savefig('box_plot.png')
    plt.show()
