import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # 1 Read data
    df = pd.read_csv("epa-sea-level.csv")

    # 2 Scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # 3 Line of best fit (ALL data)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = np.arange(1880, 2051)
    y_pred = res.intercept + res.slope * x_pred
    plt.plot(x_pred, y_pred, color='red')

    # 4 Line of best fit (Year >= 2000)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(
        df_recent['Year'],
        df_recent['CSIRO Adjusted Sea Level']
    )
    x_pred_recent = np.arange(2000, 2051)
    y_pred_recent = res_recent.intercept + res_recent.slope * x_pred_recent
    plt.plot(x_pred_recent, y_pred_recent, color='green')

    # 5 Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save and return plot
    plt.savefig('sea_level_plot.png')
    return plt.gca()
