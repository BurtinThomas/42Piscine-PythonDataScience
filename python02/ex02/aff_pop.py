from load_csv import load
import matplotlib.pyplot as plt

def preprocess_population(pop_str):
    if pop_str.endswith("M"):
        return float(pop_str[:-1]) * 1e6
    elif pop_str.endswith("k"):
        return float(pop_str[:-1]) * 1e3
    else:
        return float(pop_str)

def main():
    dataset = load("population_total.csv")
    if dataset is None:
        return
    dataFrance = dataset[dataset['country'] == "France"].iloc[:, 1:]
    dataItalie = dataset[dataset['country'] == "Italy"].iloc[:, 1:]
    popFrance = dataFrance.values[0]
    popItalie = dataItalie.values[0]
    years = dataFrance.columns.astype(int)

    popFrance = [preprocess_population(pop) for pop in popFrance]
    popItalie = [preprocess_population(pop) for pop in popItalie]

    plt.plot(years, popFrance, label="France")
    plt.plot(years, popItalie, label="Belgium")
    plt.title('Population projection')
    plt.xlabel('Year')
    plt.xticks(range(1800, 2051, 40))
    plt.ylabel("Population")
    plt.legend()
    max_pop = max(max(popItalie), max(popFrance))
    print(int(max_pop / 1e7) + 1)
    y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1) if(i % 2 == 0 and i > 0)]
    plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])
    plt.show()


main()