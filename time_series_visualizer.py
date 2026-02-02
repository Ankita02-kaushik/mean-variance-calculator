import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1 Import data
df = pd.read_csv(
    "fcc-forum-pageviews.csv",
    parse_dates=['date'],
    index_col='date'
)

# 2 Clean data (remove top & bottom 2.5%)
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]


def draw_line_plot():
    # 3 Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'], color='red')
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Prepare data
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    df_bar = (
        df_bar
        .groupby(['year', 'month'])['value']
        .mean()
        .unstack()
    )

    # Order months correctly
    months_order = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    df_bar = df_bar[months_order]

    # 4 Draw bar plot
    fig = df_bar.plot(kind='bar', figsize=(10, 8)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")

    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.strftime('%b')
    df_box['month_num'] = df_box.index.month

    df_box = df_box.sort_values('month_num')

    # 5 Draw box plots
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    sns.boxplot(
        data=df_box,
        x='year',
        y='value',
        ax=axes[0]
    )
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page_
