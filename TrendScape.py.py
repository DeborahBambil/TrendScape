# Read the file and parse data
years = []
counts = []

with open('publications.txt', 'r') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) != 2:
            continue
        year, count = parts
        try:
            years.append(int(year))
            counts.append(int(count))
        except ValueError:
            continue

# Basic analysis
if counts:
    total_publications = sum(counts)
    average_publications = total_publications / float(len(counts))
    max_publications = max(counts)
    min_publications = min(counts)
else:
    total_publications = 0
    average_publications = 0.0
    max_publications = 0
    min_publications = 0

# Print results
print("Total publications: {}".format(total_publications))
print("Average per year: {:.2f}".format(average_publications))
print("Maximum in a year: {}".format(max_publications))
print("Minimum in a year: {}".format(min_publications))

# Plot e regressão linear
if counts and len(years) > 1:  # Requer pelo menos 2 pontos para regressão
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LinearRegression
    import numpy as np

    # Prepara dados para regressão
    X = np.array(years).reshape(-1, 1)  # Anos como variável independente
    y = np.array(counts)                # Publicações como variável dependente

    # Cria e treina o modelo
    model = LinearRegression()
    model.fit(X, y)

    # Calcula a linha de tendência
    trend_line = model.predict(X)
    slope = model.coef_[0]
    intercept = model.intercept_

    # Configura o gráfico
    plt.figure(figsize=(12, 6))
    plt.plot(years, counts, marker='o', linestyle='-', color='b', markersize=8, linewidth=2, label='Real Data')
    plt.plot(years, trend_line, linestyle='--', color='red', linewidth=2, label='Linear Trend')

    # Adiciona equação da regressão
    equation = f'y = {slope:.2f}x + {intercept:.2f}'
    plt.text(0.05, 0.95, equation, transform=plt.gca().transAxes, 
             fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))

    # Rótulos e estilo
    plt.title("Publications by Year with Linear Trend", fontsize=16, fontweight='bold', pad=20)
    plt.xlabel("Year", fontsize=14, labelpad=10)
    plt.ylabel("Number of Publications", fontsize=14, labelpad=10)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=12)

    plt.tight_layout()
    plt.savefig('publications_plot_with_trend.png', dpi=300, bbox_inches='tight')
    print("Gráfico salvo como 'publications_plot_with_trend.png'!")
    plt.close()

elif counts:
    print("Regressão linear requer pelo menos 2 anos de dados.")