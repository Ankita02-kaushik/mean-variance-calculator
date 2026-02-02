import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load dataset
    df = pd.read_csv("adult.data.csv")

    # 1. How many people of each race are represented
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # 4. Advanced education
    advanced_education = df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate']
    )

    higher_education_rich = round(
        (df[advanced_education]['salary'] == '>50K').mean() * 100, 1
    )

    lower_education_rich = round(
        (df[~advanced_education]['salary'] == '>50K').mean() * 100, 1
    )

    # 5. Minimum work hours
    min_work_hours = df['hours-per-week'].min()

    # 6. Rich among minimum workers
    rich_percentage = round(
        (df[
            (df['hours-per-week'] == min_work_hours) &
            (df['salary'] == '>50K')
        ].shape[0] /
        df[df['hours-per-week'] == min_work_hours].shape[0]) * 100, 1
    )

    # 7. Country with highest percentage earning >50K
    country_stats = (
        df[df['salary'] == '>50K']['native-country']
        .value_counts() / df['native-country'].value_counts()
    ) * 100

    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(country_stats.max(), 1)

    # 8. Top occupation in India for >50K
    top_IN_occupation = (
        df[
            (df['native-country'] == 'India') &
            (df['salary'] == '>50K')
        ]['occupation']
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Higher education rich:", higher_education_rich)
        print("Lower education rich:", lower_education_rich)
        print("Min work hours:", min_work_hours)
        print("Rich percentage:", rich_percentage)
        print("Highest earning country:", highest_earning_country)
        print("Highest earning country percentage:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
