import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo
df = pd.read_csv("D:/TFG/codigo/datos/indicadores-filtrados-TODAS-LIGAS.csv")

# Configuración de gráficos
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# 📊 Estadísticas descriptivas de goles
print("📊 Estadísticas de goles locales y visitantes:")
print(df[["resultado_local", "resultado_visitante"]].describe())

# Histograma goles local
sns.histplot(df["resultado_local"], bins=range(0, df["resultado_local"].max() + 2), kde=False)
plt.title("Distribución de goles del equipo local")
plt.xlabel("Goles")
plt.ylabel("Frecuencia")
plt.show()

# Histograma goles visitante
sns.histplot(df["resultado_visitante"], bins=range(0, df["resultado_visitante"].max() + 2), kde=False)
plt.title("Distribución de goles del equipo visitante")
plt.xlabel("Goles")
plt.ylabel("Frecuencia")
plt.show()

# Boxplot comparativo
sns.boxplot(data=df[["resultado_local", "resultado_visitante"]])
plt.title("Boxplot goles local vs visitante")
plt.show()

# 📋 Distribución de resultado_partido
conteo = df["resultado_partido"].value_counts().sort_index()
proporcion = conteo / conteo.sum()

print("\n📋 Distribución de resultado_partido:")
print(pd.DataFrame({
    "Resultado": ["1", "X", "2"],
    "Frecuencia": conteo.values,
    "Proporción": proporcion.values
}))

# Gráfico de barras para resultado_partido
sns.countplot(x="resultado_partido", data=df, order=["1", "X", "2"], palette="Set2")
plt.title("Distribución de resultado del partido")
plt.xlabel("Resultado del partido")
plt.ylabel("Número de partidos")
plt.show()



