from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Exécute le processus principal pour charger les données
    de l'espérance de vie et tracer les projections pour la France.
    Étapes :
        1. Charge un fichier CSV contenant les données
        d'espérance de vie par pays et années.
        2. Filtre les données pour la France et extrait les
        colonnes correspondant aux années et aux valeurs d'espérance de vie.
        3. Trace un graphique de l'espérance de vie
        en fonction des années pour la France.
    """
    try:
        df = load("life_expectancy_years.csv")
        df_France = df.loc[df['country'] == 'France'].iloc[:, 1:]
        years = df_France.columns.astype(int)
        life_expectancy = df_France.values[0]

        plt.plot(years, life_expectancy, color="blue")
        plt.title("France Life expectancy Projections")
        plt.xticks(range(min(years), max(years), 40))
        plt.xlabel("Year")
        plt.ylabel("life expectancy")
        plt.yticks(range(30, 95, 10))
        plt.show()
    except Exception as error:
        print(f"{Exception.__name__} : {error}")
    except KeyboardInterrupt:
        print("\nInput interrupted. Exiting...")


if __name__ == "__main__":
    main()
