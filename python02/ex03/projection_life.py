from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Exécute le processus principal pour visualiser la relation entre
    le PIB par habitant et l'espérance de vie en 1900.
    Étapes :
        1. Charge deux fichiers CSV :
           - L'un contenant les données d'espérance de vie par pays et années.
           - L'autre contenant les données de revenu par
           personne ajustées pour l'inflation.
        2. Extrait les données pour l'année 1900 à partir des deux DataFrames.
        3. Trace un graphique en nuage de points (scatter plot) représentant
        la relation entre le PIB et l'espérance de vie en 1900.
        4. Configure l'échelle logarithmique pour l'axe des X et
        personnalise les ticks des axes.
    """
    try:
        dfExpectancy = load("life_expectancy_years.csv")
        dfIncome = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

        Expectancy1900 = dfExpectancy.loc[:, "1900"].values
        Income1900 = dfIncome.loc[:, "1900"].values

        plt.scatter(Income1900, Expectancy1900)
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.xscale("log")
        plt.yticks(range(20, 60, 5))
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
        plt.show()
    except Exception as error:
        print(f"{Exception.__name__} : {error}")
    except KeyboardInterrupt:
        print("\nInput interrupted. Exiting...")


if __name__ == "__main__":
    main()
