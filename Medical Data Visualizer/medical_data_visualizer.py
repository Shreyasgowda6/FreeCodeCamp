import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def draw_cat_plot():
    # Import the data
    df = pd.read_csv(r'D:\Coding\FreeCodeCamp\Medical Data Visualizer\medical_examination.csv')

    # Create the overweight column
    df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

    # Normalize data
    df['cholesterol'] = df['cholesterol'].replace({1: 0, 2: 1, 3: 1})
    df['gluc'] = df['gluc'].replace({1: 0, 2: 1, 3: 1})

    # Create a DataFrame for the cat plot
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Draw the cat plot
    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar')
    
    # Get the figure for the output
    return fig

def draw_heat_map():
    # Import the data
    df = pd.read_csv(r'D:\Coding\FreeCodeCamp\Medical Data Visualizer\medical_examination.csv')

    # Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    plt.figure(figsize=(12, 8))

    # Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap='coolwarm', cbar=True, square=True)

    # Do not modify the next two lines
    plt.show()
