from load_csv import load
import matplotlib.pyplot as plt
import pandas

def main():
    datasetLife = load("life_expectancy_years.csv")
    datasetInflation = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life1900 = datasetLife["1900"].values
    inflation900 = datasetInflation["1900"].values

    
    plt.scatter(life1900, inflation900)
    plt.title("Life expectancy vs Gross domestic product (Year 1900)")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy (Years)")
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.show()
    
    

main()