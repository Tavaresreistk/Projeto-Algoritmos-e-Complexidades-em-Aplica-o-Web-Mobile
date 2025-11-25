# 📦 Warehouse Manager

Sistema Web de **Cadastro e Busca de Itens em Armazém** desenvolvido em **Python (Flask)** e **SQLite**.

---

## ⚙️ Tecnologias Utilizadas
- Python 3.x
- Flask
- SQLite3
- HTML / Bootstrap

---

## 🚀 Funcionalidades
- Cadastrar novos itens (nome, categoria, quantidade, código)
- Listar itens cadastrados
- Buscar itens (por nome, categoria ou código)
- Excluir itens
- Armazenamento persistente em SQLite

---

## 🧩 Estruturas de Dados e Algoritmos

| Estrutura / Algoritmo | Uso | Complexidade | Observação |
|------------------------|-----|---------------|-------------|
| Dicionário (Hash) | Busca interna por código | **O(1)** | Tempo constante |
| Lista / Tabela SQL | Armazenamento e listagem | **O(n)** | Percorre todos os registros |
| Busca SQL com LIKE | Busca textual | **O(n)** | Linear em relação ao total de registros |
| Inserção (SQLite) | Inserir novo item | **O(1)** médio | Constante em bancos pequenos |
| Exclusão (SQLite) | Deletar item por código | **O(1)** médio | Constante |

---

## 📘 Complexidade Assintótica

### 🔹 Melhor caso
Busca em hash (por código exato): **O(1)**

### 🔹 Caso médio
Busca SQL (texto parcial com `LIKE`): **O(n)**

### 🔹 Pior caso
Busca linear percorrendo toda a tabela: **O(n)**

---

## 🧠 Justificativa de Estruturas
- **Tabela Hash (Python dict)**: busca direta eficiente por código.
- **SQLite**: banco relacional leve e persistente, ideal para protótipos web.
- **Flask**: framework minimalista, rápido e fácil de integrar com HTML.

---

## 🖥️ Como Executar no VSCode

1. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # no Windows
   source venv/bin/activate  # no Linux/Mac
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Rode a aplicação:
   ```bash
   python app.py
   ```
4. Acesse no navegador:
   ```
   http://127.0.0.1:5000
   ```

---

## ☁️ Deployment sugerido
- Railway (gratuito e fácil)
- Render ou Vercel (caso queira o frontend separado)

---

## ✍️ Autoria
Desenvolvido por **Luís Tavares**
Disciplina: **Algoritmos e Complexidade em Aplicação Web/Mobile**
Professor: MSc. Heleno Cardoso
