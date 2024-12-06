# -*- coding: utf-8 -*-
"""[nayve bayes] Sentimental analysis

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/111K2Ml_CVvKpnkMXaJfhzjhWxGXIizqm
"""

pip install flask-ngrok

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
from nltk.corpus import stopwords
import nltk
from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok

df_1 = pd.read_csv('/content/drive/MyDrive/train_nb.csv', sep=';', encoding = 'iso-8859-1')
df_2 = pd.read_csv('/content/drive/MyDrive/test_nb.csv', sep=';', encoding = 'iso-8859-1')

tamanho = len(df_2)

# Baixar stopwords do NLTK
nltk.download('stopwords')

# Carregar as stopwords em português
stop_words = stopwords.words('portuguese')

# Separar os dados em texto e rótulo
X = df_1['Comentário']
y = df_1['Sentimento']

# Remover ou substituir valores NaN
X = X.fillna('')  # Substituir NaN por uma string vazia

# Dividir os dados em treino e teste (90% treino, 10% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=50)

# Converter o texto para uma representação numérica usando o CountVectorizer
vectorizer = CountVectorizer(stop_words=stop_words)  # Usando stopwords do NLTK
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Criar e treinar o modelo Naive Bayes
model = MultinomialNB(alpha=0.6)
model.fit(X_train_vec, y_train)

# Fazer previsões nos dados de teste
y_pred = model.predict(X_test_vec)

# Avaliar o desempenho do modelo
print("Acurácia:", accuracy_score(y_test, y_pred))
print("Relatório de Classificação:\n", classification_report(y_test, y_pred))

# Função para testar novas frases
def prever_sentimento(texto):
    # Transformar o texto de entrada de acordo com o vetor de treino
    texto_vec = vectorizer.transform([texto])

    # Fazer a previsão
    previsao = model.predict(texto_vec)

    return previsao[0]  # Retorna o resultado da previsão

# Listas para armazenar os dados
comentarios = []
sentimentos = []

# Iterar sobre os exemplos e salvar os resultados
for i in range(tamanho):  # Ajuste o número de iterações conforme necessário
    exemplo = df_2['Comentário'][i]
    sentimento = prever_sentimento(exemplo)

    # Adicionar comentário e sentimento nas listas
    comentarios.append(exemplo)
    sentimentos.append(sentimento)

# Criar um novo DataFrame com as duas colunas
df_resultado = pd.DataFrame({
    'Comentário': comentarios,
    'Sentimento': sentimentos
})

# Exibir o DataFrame resultante
print(df_resultado)


"""exemplo = df_2['Comentário'][0]
sentimento = prever_sentimento(exemplo)
print(f"O sentimento do texto '{exemplo}' é: {sentimento}")"""

#df_resultado.to_csv('resultados_sentimentos.csv', index=False, encoding='iso-8859-1')

"""## Visualizando

"""
