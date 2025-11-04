# 📈 Previsor de Salário (Regressão Linear com Streamlit)

Este é um projeto de portfólio que demonstra um fluxo simples de Machine Learning, desde a análise dos dados até a implantação de um aplicativo web interativo.

O aplicativo prevê o salário de um profissional com base em seus anos de experiência, utilizando um modelo de Regressão Linear Simples treinado em um conjunto de dados.

![Screenshot do App](img/app-screenshot.png)

---

## 💻 Tecnologias Utilizadas

Este projeto foi construído com as seguintes tecnologias:

* **Python:** Linguagem principal do projeto.
* **Pandas:** Para carregamento e manipulação dos dados.
* **Scikit-learn:** Para criar e treinar o modelo de Regressão Linear.
* **Joblib:** Para salvar o modelo treinado e carregá-lo no aplicativo.
* **Streamlit:** Para construir e servir o aplicativo web interativo.

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para executar o aplicativo em sua máquina local.

**Pré-requisitos:**
* Ter o [Python 3.x](https://www.python.org/) instalado.
* Ter o [Poetry](https://python-poetry.org/docs/#installation) instalado.
* Ter o [Git](https://git-scm.com/) instalado.

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU_NOME/NOME_DO_REPOSITORIO.git](https://github.com/SEU_NOME/NOME_DO_REPOSITORIO.git)
    cd NOME_DO_REPOSITORIO
    ```

2.  **Instale as dependências (O Poetry cuida do ambiente virtual):**
    ```bash
    poetry install
    ```

3.  **Execute o aplicativo Streamlit:**
    * (O Poetry também pode rodar o comando dentro do ambiente virtual)
    ```bash
    poetry run streamlit run app.py
    ```

4.  Abra seu navegador e acesse o endereço `http://localhost:8501`.

---

## 📂 Estrutura dos Arquivos

* `app.py`: O código-fonte do aplicativo web Streamlit.
* `testes.ipynb`: Jupyter Notebook com a análise exploratória e o processo de treinamento do modelo.
* `modelo.pkl`: O arquivo do modelo de Regressão Linear salvo (serializado).
* `Salary_Data.csv`: O conjunto de dados usado para treinar o modelo.
* `README.md`: Este arquivo.

---

## 🙏 Créditos

Este projeto foi desenvolvido como exercício de aprendizado, seguindo o tutorial do canal Daxus | Empowerdata Python. Você pode encontrar o vídeo original aqui: https://www.youtube.com/watch?v=bGwdwF1vlvQ.