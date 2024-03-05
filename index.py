import pandas as pd
import matplotlib.pyplot as plt
#por defecto el número de bins en un histogram es 10
def load_data(filename):
    return pd.read_csv(filename, index_col=0)

def filter_sport(df, sex, sport):
    return df[(df["Sex"] == sex) & (df["Sport"] == sport)]

def display_data(df):
    print("Original DF:")
    print(df.head(10))

def display_filtered_data(filtered_data):
    print("Filtered DF:")
    print(filtered_data.head(10))
    binsDef=[150, 160, 170, 180, 190, 200, 210]
def plot_height_differences(menRowing, menGymnastics, menBasketball, menTaek):
    fig, ax = plt.subplots()
    ax.hist(menRowing["Height"], label="Rowling", color="lightblue", ec="darkblue", lw=1, bins=5)
    ax.hist(menGymnastics["Height"], label="Gymnastics", color="lightgreen", ec="darkgreen", lw=1, bins=5)
    ax.hist(menBasketball["Height"], label="Basketball", color="lightpink", ec="darkred", lw=1, bins=5)
    #ax.hist(menTaek["Height"], label="Taek", color= "orange", ec="black", bins=5,  histtype="step")
    ax.hist(menTaek["Height"], label="Taek", color= "orange", ec="black", bins=5)
    ax.set_xlabel("Height (cm)")
    ax.set_ylabel("Number of observations")
    ax.set_title("Differences between height and male sport categories")
    ax.legend()
    plt.show()

def boxplot_height(menRowing, menGymnastics, menBasketball, menTaek):
    fig, ax = plt.subplots()
    ax.boxplot([ menRowing["Height"], menGymnastics["Height"], menBasketball["Height"],menTaek["Height"]])
    ax.set_xticklabels(["Rowing", "Gymnastics", "Basket", "Taekwondo"])
    # Add a y-axis label
    ax.set_ylabel("Height (cm)")
    plt.show()
#error var charts
def barcharts_error_varchats(menRowing, menGymnastics, menBasketball, menTaek):
    fig, ax = plt.subplots()
# Add a bar for the rowing "Height" column mean/std
    ax.bar("Rowing", menRowing["Height"].mean(), yerr=menRowing["Height"].std(), color="lightblue", ec="darkblue")
# Add a bar for the gymnastics "Height" column mean/std
    ax.bar("Gymnastics", menGymnastics["Height"].mean(), yerr=menGymnastics["Height"].std(), color="lightgreen", ec="darkgreen")
 # Other
    ax.bar("Basketball", menBasketball["Height"].mean(), yerr=menBasketball["Height"].std(),color="lightpink", ec="darkred")   
 # Other
    ax.bar("Taekwondo", menTaek["Height"].mean(), yerr=menTaek["Height"].std(), label="Taek", color= "orange", ec="black")      
# Label the y-axis
    #ax.grid(True)
    ax.set_title("Barcharts mean & deviation ")
    ax.set_ylabel("Height (cm)")
    plt.ylim(150, 210)
    plt.show()

def weightfull():
    # Suponiendo que `load_data` es una función que importa datos de un archivo CSV
    summer_2016_medals = load_data("summer2016.csv")
    # Extraer la columna "Sport"
    sports_column = summer_2016_medals["Sport"]
    # Encontrar los valores únicos de la columna "Sport"
    sports = sports_column.unique()
    # Imprimir los valores únicos de los deportes
    print(sports)
    fig, ax = plt.subplots()
    # Iterar sobre las diferentes ramas de deportes
    for sport in sports:
        # Extraer las filas solo para este deporte
        sport_df = summer_2016_medals[summer_2016_medals["Sport"] == sport]
        # Agregar una barra para la media de "Weight" con barra de error y std
        ax.bar(sport, sport_df["Weight"].mean(), yerr=sport_df["Weight"].std())
    ax.set_ylabel("Weight")
    ax.set_title("Weight of sports 2016")
    ax.set_xticklabels(sports, rotation=90)
    # Guardar la figura en un archivo
    fig.savefig("sports_weights2.png")
    plt.ylim(30, 120)
    plt.show()

def heightfull():
    # Suponiendo que `load_data` es una función que importa datos de un archivo CSV
    summer_2016_medals = load_data("summer2016.csv")
    # Extraer la columna "Sport"
    sports_column = summer_2016_medals["Sport"]
    # Encontrar los valores únicos de la columna "Sport"
    sports = sports_column.unique()
    # Imprimir los valores únicos de los deportes
    print(sports)
    fig, ax = plt.subplots()
    # Iterar sobre las diferentes ramas de deportes
    for sport in sports:
        # Extraer las filas solo para este deporte
        sport_df = summer_2016_medals[summer_2016_medals["Sport"] == sport]
        # Agregar una barra para la media de "Weight" con barra de error y std
        ax.bar(sport, sport_df["Height"].mean(), yerr=sport_df["Height"].std())
    ax.set_ylabel("Height")
    ax.set_title("Height of sports 2016")
    ax.set_xticklabels(sports, rotation=90)
    # Guardar la figura en un archivo
    fig.savefig("sports_heights2.png")
    plt.ylim(150, 210)
    plt.show()

# Load data por defecto
df = load_data("summer2016.csv")
# Filtrar datos
menRowing = filter_sport(df, "M", "Rowing")
menGymnastics = filter_sport(df, "M", "Gymnastics")
menBasketball = filter_sport(df, "M", "Basketball")
menTaek = filter_sport(df, "M", "Taekwondo")

# Mostrar datos originales y filtrados
display_data(df)
display_filtered_data(menRowing)
# Call to func
boxplot_height(menRowing, menGymnastics, menBasketball, menTaek)
weightfull()
heightfull()