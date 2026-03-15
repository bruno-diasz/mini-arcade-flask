# Mini Arcade Educativo

Um sistema web com jogos simples para crianças, incluindo funcionalidades administrativas para gerenciar conteúdo do quiz.

## 🚀 Como executar

### Pré-requisitos
- Python 3.8 ou superior
- pip

### Instalação

1. Clone ou baixe o projeto
2. Navegue até o diretório do projeto
3. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # ou
   .venv\Scripts\activate     # Windows
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute a aplicação:
   ```bash
   python run.py
   ```

6. Abra o navegador e acesse: http://127.0.0.1:5000

## 🎮 Jogos Disponíveis

- **🔢 Adivinhar Número**: Tente adivinhar um número entre 1 e 100
- **🐶 Quiz de Animais**: Responda perguntas de múltipla escolha sobre animais
- **🎨 Desafio de Desenho**: Receba desafios criativos para desenhar

## ⚙️ Funcionalidades Administrativas

Acesse `/admin` para gerenciar as perguntas do quiz:
- Criar novas perguntas
- Listar todas as perguntas
- Editar perguntas existentes
- Remover perguntas

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask
- **Banco de dados**: SQLite
- **ORM**: SQLAlchemy
- **Frontend**: HTML, CSS, Bootstrap

## 📁 Estrutura do Projeto

```
mini-arcade-educativo/
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── models.py
│   ├── services.py
│   ├── views.py
│   ├── static/
│   └── templates/
│       ├── index.html
│       ├── guess.html
│       ├── quiz.html
│       ├── draw.html
│       ├── admin.html
│       ├── questions.html
│       └── question_form.html
├── requirements.txt
├── run.py
└── README.md
```