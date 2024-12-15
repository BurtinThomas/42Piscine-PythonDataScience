from load_csv import load
import matplotlib.pyplot as plt


def preprocess_population(pop_str):
    """
    Convertit une chaîne de caractères représentant une
    population en un nombre flottant.
    Args:
        pop_str (str): Une chaîne représentant une
        population, avec ou sans suffixe ('M' ou 'k').
    Returns:
        float: La population convertie en nombre flottant.
    """
    if pop_str.endswith("M"):
        return float(pop_str[:-1]) * 1e6
    elif pop_str.endswith("k"):
        return float(pop_str[:-1]) * 1e3
    else:
        return float(pop_str)


def main():
    """
    Exécute le processus principal pour tracer les projections
    de population de la France et de la Belgique.
    Étapes :
        1. Charge les données de population à partir d'un fichier CSV.
        2. Filtre les données pour la France et la Belgique,
        et extrait les années et les populations correspondantes.
        3. Convertit les valeurs de population en nombres
        flottants (gérant les suffixes 'M' et 'k').
        4. Trace les courbes de population pour la France et la Belgique
        avec des axes personnalisés :
           - Axe X : Années (1800 à 2050, avec un pas de 40).
           - Axe Y : Population, affichée en millions (M).
    """
    try:
        df = load("population_total.csv")
        df_France = df.loc[df['country'] == 'France'].iloc[:, 1:]
        df_Belgium = df.loc[df['country'] == 'Belgium'].iloc[:, 1:]
        #df_France = df.loc[df['country'] == 'France', df.columns[1:]]

        popFrance = df_France.values[0]
        popBelgium = df_Belgium.values[0]
        years = df.columns[1:].astype(int)

        popFrance = [preprocess_population(data) for data in popFrance]
        popBelgium = [preprocess_population(data) for data in popBelgium]

        plt.plot(years, popFrance, label="France", color="green")
        plt.plot(years, popBelgium, label="Belgium", color="blue")
        plt.title('Population projections')
        plt.xlabel('Year')
        plt.xticks(range(1800, 2051, 40))
        plt.ylabel("Population")
        plt.legend(loc="lower right")
        max_pop = max(max(popBelgium), max(popFrance))
        y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1) if (i % 2 == 0 and i > 0)]
        plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])
        plt.show()
    except Exception as error:
        print(f"{Exception.__name__} : {error}")
    except KeyboardInterrupt:
        print("\nInput interrupted. Exiting...")


if __name__ == "__main__":
    main()
