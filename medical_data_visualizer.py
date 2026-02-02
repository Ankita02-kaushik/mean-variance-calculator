import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 Import the data
df = pd.read_csv("medical_examination.csv")

# 2 Add overweight column
df['overweight'] = (
    df['weight'] / ((df['height'] / 100) ** 2) > 25
).astype(int)

# 3 Normalize data (0 = good, 1 = bad)
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)


def draw_cat_plot():
    # 4 Create categorical DataFrame
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # 5 Group and count
    df_cat = (
        df_cat
        .groupby(['cardio', 'variable', 'value'])
        .size()
        .reset_index(name='total')
    )

    # 6 Draw the catplot
    fig = sns.catplot(
        data=df_cat,
        kind="bar",
        x="variable",
        y="total",
        hue="value",
        col="cardio"
    ).fig

    return fig


def draw_heat_map():
    # 11 Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12 Calculate correlation matrix
    corr = df_heat.corr()

    # 13 Generate mask
    mask = np.triu(corr)

    # 14 Set up figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15 Draw heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        square=True,
        center=0,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5}
    )

    return fig
