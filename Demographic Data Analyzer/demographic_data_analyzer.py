import pandas as pd

def analyze_demographic_data():
    df = pd.read_csv(r'D:\Coding\FreeCodeCamp\Demographic Data Analyzer\adult.data.csv')  # Update the path to your CSV file

    # 1. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'].value_counts(normalize=True)['Bachelors']) * 100

    # 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_advanced_education_over_50k = (advanced_education['salary'] == '>50K').mean() * 100

    # 5. What percentage of people without advanced education make more than 50K?
    no_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_no_advanced_education_over_50k = (no_advanced_education['salary'] == '>50K').mean() * 100

    # 6. What is the minimum number of hours a person works per week?
    min_hours_per_week = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    percentage_min_hours_over_50k = (df[df['hours-per-week'] == min_hours_per_week]['salary'] == '>50K').mean() * 100

    # 8. What country has the highest percentage of people that earn >50K and what is that percentage?
    country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack().fillna(0)
    country_high_salary = country_salary['>50K'].idxmax()
    percentage_high_salary_country = country_salary['>50K'].max() * 100

    # 9. Identify the most popular occupation for those who earn >50K in India.
    popular_occupation_india = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': round(percentage_bachelors, 1),
        'percentage_advanced_education_over_50k': round(percentage_advanced_education_over_50k, 1),
        'percentage_no_advanced_education_over_50k': round(percentage_no_advanced_education_over_50k, 1),
        'min_hours_per_week': min_hours_per_week,
        'percentage_min_hours_over_50k': round(percentage_min_hours_over_50k, 1),
        'country_high_salary': country_high_salary,
        'percentage_high_salary_country': round(percentage_high_salary_country, 1),
        'popular_occupation_india': popular_occupation_india,
    }

if __name__ == '__main__':
    results = analyze_demographic_data()
    print(results)
