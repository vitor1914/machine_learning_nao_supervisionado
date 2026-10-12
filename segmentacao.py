
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Carregar os dados
dados = pd.read_csv("clientes.csv")

# 2. Selecionar as características dos clientes
X = dados[["idade", "renda_mensal", "compras_mensais"]]

# 3. Padronizar as variáveis
escalador = StandardScaler()
X_padronizado = escalador.fit_transform(X)

# 4. Criar o modelo K-Means
modelo = KMeans(n_clusters=3, random_state=42, n_init=10)

# 5. Identificar os grupos
dados["grupo"] = modelo.fit_predict(X_padronizado)

# 6. Exibir os resultados
print("\nCLIENTES AGRUPADOS")
print(dados.sort_values("grupo").to_string(index=False))

# 7. Resumir os grupos
print("\nPERFIL DOS GRUPOS")
print(
    dados.groupby("grupo")[
        ["idade", "renda_mensal", "compras_mensais"]
    ].mean().round(2)
)

# 8. Criar gráfico
for grupo in sorted(dados["grupo"].unique()):
    clientes = dados[dados["grupo"] == grupo]
    plt.scatter(
        clientes["renda_mensal"],
        clientes["compras_mensais"],
        label=f"Grupo {grupo}"
    )

plt.xlabel("Renda mensal (R$)")
plt.ylabel("Compras mensais")
plt.title("Segmentação de clientes com K-Means")
plt.legend()
plt.tight_layout()
plt.savefig("segmentacao_clientes.png")
plt.show()

# 9. Salvar os resultados
dados.to_csv("clientes_segmentados.csv", index=False)

print("\nArquivos gerados:")
print("- clientes_segmentados.csv")
print("- segmentacao_clientes.png")
