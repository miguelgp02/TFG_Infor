import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo completo
df = pd.read_csv("D:/TFG/codigo/datos/indicadores-filtrados-TODAS-LIGAS.csv")

# Estilo de gráficos
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# =======================================
# 📊 1. Proporciones de cambios por partido (total de sustituciones)
# =======================================
cambios_cols = [
    "proporcion local cambios en sitio",
    "proporcion local cambios en general",
    "proporcion visitante cambios en sitio",
    "proporcion visitante cambios en general"
]

# Unificar en una sola serie para análisis global
cambios_totales = df[cambios_cols].values.flatten()

print("\n📊 Análisis unificado de proporciones de cambios por partido:")
print(pd.Series(cambios_totales).describe())

# Boxplot
sns.boxplot(x=cambios_totales)
plt.title("Boxplot unificado de proporciones de cambios dentro del partido")
plt.xlabel("Número medio de cambios dentro del partido")
plt.show()

# =======================================
# 📊 2. Cambios en alineación (defensas, medios, delanteros, sitio y general)
# =======================================

# Definir columnas por línea y tipo (sitio vs general)
cols_local_sitio = [
    "proporcion local cambios alineacion defensa sitio",
    "proporcion local cambios alineacion centrocampista sitio",
    "proporcion local cambios alineacion delantero sitio"
]
cols_visitante_sitio = [
    "proporcion visitante cambios alineacion defensa en sitio",
    "proporcion visitante cambios alineacion centrocampista en sitio",
    "proporcion visitante cambios alineacion delantero en sitio"
]
cols_local_general = [
    "proporcion local cambios alineacion defensa en general",
    "proporcion local cambios alineacion centrocampista en general",
    "proporcion local cambios alineacion delantero en general"
]
cols_visitante_general = [
    "proporcion visitante cambios alineacion defensa en general",
    "proporcion visitante cambios alineacion centrocampista en general",
    "proporcion visitante cambios alineacion delantero en general"
]


# Calcular proporciones totales por partido
df["cambios_local_sitio_total"] = df[cols_local_sitio].sum(axis=1)
df["cambios_local_general_total"] = df[cols_local_general].sum(axis=1)
df["cambios_visitante_sitio_total"] = df[cols_visitante_sitio].sum(axis=1)
df["cambios_visitante_general_total"] = df[cols_visitante_general].sum(axis=1)


# Combinar todas las columnas en una sola serie
valores_unificados = df[[
    "cambios_local_sitio_total",
    "cambios_local_general_total",
    "cambios_visitante_sitio_total",
    "cambios_visitante_general_total"
]].values.flatten()

# Crear una Serie de pandas para facilitar el uso de describe
serie_unificada = pd.Series(valores_unificados)

# Obtener estadísticos
estadisticas = serie_unificada.describe()
print("\n📊 Media global de cambios en alineación:")
print(estadisticas)

# Boxplot
sns.boxplot(x=valores_unificados)
plt.title("Boxplot unificado de proporciones de cambios en la alineación")
plt.xlabel("Número medio de cambios en la alineación")
plt.show()


# =======================================
# 📊 3. Minutos promedio de cambios
# =======================================
minutos_cols = [
    "media local cambios minutos sitio",
    "media local cambios minutos en general",
    "media visitante cambios minutos sitio",
    "media visitante cambios minutos en general"
]

# Unificar en una sola serie
minutos_total = df[minutos_cols].values.flatten()

print("\n📊 Análisis unificado del minuto promedio de cambios:")
print(pd.Series(minutos_total).describe())

# Boxplot
sns.boxplot(x=minutos_total)
plt.title("Boxplot del minuto promedio de cambios")
plt.xlabel("Minuto")
plt.show()
