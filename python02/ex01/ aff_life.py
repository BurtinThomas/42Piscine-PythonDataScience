from load_csv import load
import matplotlib.pyplot as plt

def main():
    dataset = load("life_expectancy_years.csv")
    if dataset is None:
        return
    france = dataset[dataset['country'] == "France"].iloc[1:, 1:]
   
    years = france.columns.astype(int)
    life_expectancy = france.values[0]
    print(france)

    plt.plot(years, life_expectancy)
    plt.title('Life Expectancy in France Over the Years')
    plt.xlabel('Year')
    plt.xticks(range(min(years), max(years), 40))
    plt.ylabel('Life Expectancy')
    plt.yticks(range(30, 95, 10))
    plt.show()  

main()