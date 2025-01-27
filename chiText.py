from collections import Counter
from scipy.stats import chi2_contingency
import pandas as pd

def chi_squared_test_corpus(corpus1, corpus2):
    # Contar la frecuencia de las palabras en ambos corpus
    freq1 = Counter(" ".join(corpus1).split()) #cambiar
    freq2 = Counter(" ".join(corpus2).split()) #cambiar
    
    # Crear un conjunto único de todas las palabras de ambos corpus
    unique_words = set(freq1.keys()).union(set(freq2.keys()))
    
    # Crear la tabla de contingencia
    data = {
        word: [freq1.get(word, 0), freq2.get(word, 0)]
        for word in unique_words
    }
    contingency_table = pd.DataFrame(data, index=['Corpus1', 'Corpus2']).T
    
    # Aplicar el test de chi-cuadrado
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    
    # Resultado
    return {
        "chi2": chi2,
        "p_value": p,
        "degrees_of_freedom": dof,
        "expected_frequencies": expected,
        "contingency_table": contingency_table
    }
 # Ejemplo de uso
corpus1 = documentPos #texto Original
corpus2 = documentNeg #texto transcrito

resultados = chi_squared_test_corpus(corpus1, corpus2)

# Mostrar los resultados
print("Chi-cuadrado:", resultados["chi2"])
print("p-value:", resultados["p_value"]) 
print("Grados de libertad:", resultados["degrees_of_freedom"])
print("Tabla de contingencia:")
print(resultados["contingency_table"])
