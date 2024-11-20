# Análise de Sentimentos com Naive Bayes

Este projeto utiliza **Machine Learning** e **Processamento de Linguagem Natural (NLP)** para realizar análise de sentimentos em comentários de texto. Ele emprega o modelo **Multinomial Naive Bayes** e integra uma API simples para testar a previsão de sentimentos.

## 📋 Funcionalidades

- Treinamento de um modelo de classificação Naive Bayes com dados de comentários rotulados.
- Previsão do sentimento de novos comentários.
- Geração de um DataFrame com resultados de previsões.
- Exportação dos resultados para um arquivo CSV.
- Integração de um servidor **Flask** (com **ngrok**) para transformar o modelo em uma API acessível.

---

## 🛠️ Tecnologias Utilizadas

- **Python** 
  - Pandas
  - Scikit-learn
  - NLTK
  - Flask
  - Flask-ngrok
- **Machine Learning**: Multinomial Naive Bayes
- **Processamento de Texto**: Stopwords e vetorização com CountVectorizer

---

## 🚀 Como Usar

### Pré-requisitos

1. **Python 3.8+** instalado
2. Dependências listadas no `requirements.txt`. Instale-as com:
   ```bash
   pip install -r requirements.txt

### Passo a Passo

1. **Prepare os Dados**
   - Certifique-se de que os arquivos `train_nb.csv` e `test_nb.csv` estão disponíveis nos caminhos corretos.
   - O arquivo de treino (`train_nb.csv`) deve conter colunas como:
     - `Comentário`: Texto do comentário.
     - `Sentimento`: Rótulo do sentimento (positivo/negativo).
   - O arquivo de teste (`test_nb.csv`) deve conter ao menos a coluna `Comentário`.

2. **Execute o Script**
   - Rode o script para treinar o modelo e prever os sentimentos:
     ```bash
     python nome_do_seu_script.py
     ```
   - O script exibirá a acurácia e o relatório de classificação no console, além de gerar um DataFrame com os resultados.

3. **API Flask**
   - Para usar a API com Flask e ngrok, habilite a integração e configure a rota para enviar textos e receber previsões.

4. **Salvar Resultados**
   - Ao final da execução, os resultados das previsões podem ser salvos em um arquivo CSV:
     ```bash
     df_resultado.to_csv('resultados_sentimentos.csv', index=False, encoding='iso-8859-1')
     ```

---

## 🔍 Estrutura dos Arquivos

- **`train_nb.csv`**: Dados de treino rotulados para treinar o modelo.
- **`test_nb.csv`**: Dados para testar o modelo e gerar previsões.
- **`resultados_sentimentos.csv`**: Resultado final com comentários e seus respectivos sentimentos previstos.
- **`script.py`**: Script principal contendo todo o código.

---

## ⚡ Exemplos de Uso

- Para prever o sentimento de um único comentário no console:
  ```python
  exemplo = "Adorei este produto! Recomendo."
  sentimento = prever_sentimento(exemplo)
  print(f"O sentimento é: {sentimento}")
- Para usar com um DataFrame maior, os resultados serão armazenados automaticamente.
  
