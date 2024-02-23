import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load dataset
df = pd.read_csv('epa-sea-level.csv')

# Datos dispersión
data = {
    'Year': df['Year'],
    'CSIRO Adjusted Sea Level': df['CSIRO Adjusted Sea Level']
}

def draw_plot(df):
    
    df = pd.DataFrame(data)

    # Filtrar los datos desde el año 2000 hasta el año más reciente
    df_filtered = df[df['Year'] >= 2000]

    # Realizar la regresión lineal para todos los datos
    slope, intercept, r_value, p_value, std_err = stats.linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Calcular la línea de mejor ajuste para todos los datos
    line_all = slope * df['Year'] + intercept

    # Realizar la regresión lineal para los datos filtrados
    slope_filtered, intercept_filtered, r_value_filtered, p_value_filtered, std_err_filtered = stats.linregress(df_filtered['Year'], df_filtered['CSIRO Adjusted Sea Level'])

    # Calcular la línea de mejor ajuste para los datos filtrados
    line_filtered = slope_filtered * df_filtered['Year'] + intercept_filtered

    # Traza la línea de mejor ajuste sobre el diagrama de dispersión para todos los datos
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], line_all, color='red', label='All data')

    # Traza la línea de mejor ajuste sobre el diagrama de dispersión para los datos filtrados
    plt.scatter(df_filtered['Year'], df_filtered['CSIRO Adjusted Sea Level'])
    plt.plot(df_filtered['Year'], line_filtered, color='blue', label='Since 2000')

    # Establecer el límite del eje x para incluir el año 2050
    plt.xlim(min(df['Year']), 2050)

    # Etiquetas de los ejes
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Agregar una leyenda
    plt.legend()

    # Predecir el aumento del nivel del mar en 2050 para todos los datos
    aumento_2050_all = slope * 2050 + intercept
    print("Sea level rise prediction in 2050 for all data:", aumento_2050_all)

    # Predecir el aumento del nivel del mar en 2050 para los datos filtrados
    aumento_2050_filtered = slope_filtered * 2050 + intercept_filtered
    print("Sea level rise prediction in 2050 for filtered data:", aumento_2050_filtered)
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
