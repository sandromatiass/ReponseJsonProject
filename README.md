```markdown
# 🚀 API de Usuários - Django REST Framework

Este projeto demonstra a criação de uma API RESTful usando Django Rest Framework para retornar dados de usuários em formato JSON.

## 📋 Descrição do Projeto

### Objetivos Atendidos:
- **Passo 2 (UA10)**: Criar arquivo JSON com dados de usuários
- **Passo 3 (UA11)**: Desenvolver API usando Django REST Framework

### Funcionalidades:
- ✅ API RESTful retornando dados em JSON
- ✅ Interface web responsiva e moderna
- ✅ Dados formatados de forma elegante
- ✅ Código JSON destacado com syntax highlighting

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Django 4.x**
- **Django REST Framework**
- **HTML5 & CSS3**
- **JavaScript**

## 📁 Estrutura do Projeto

```
backend/
├── 📄 manage.py
├── 📁 backend/
│   ├── 📄 settings.py
│   ├── 📄 urls.py
│   └── 📄 wsgi.py
├── 📁 usuarios/
│   ├── 📄 views.py
│   ├── 📄 urls.py
│   └── 📁 templates/
│       └── 📄 home.html
├── 📁 static/
│   └── 📁 css/
│       └── 📄 style.css
├── 📄 usuarios.json
└── 📄 README.md
```

## 🎯 Endpoints da API

### 1. Página Principal (Interface Web)
**URL:** `http://localhost:8000/`
- Apresenta os dados formatados em interface moderna
- Mostra o código JSON com destaque de sintaxe

### 2. API JSON Puro
**URL:** `http://localhost:8000/api/usuarios/`
- Retorna dados em formato JSON puro
- Resposta:
```json
{
  "usuarios": [
    {
      "nome": "Carlos",
      "email": "carlos@email.com"
    },
    {
      "nome": "João",
      "email": "joão@email.com"
    }
  ]
}
```

## 🚀 Como Executar o Projeto

### Pré-requisitos:
- Python 3.x instalado
- pip (gerenciador de pacotes Python)

### Passos para execução:

1. **Clone ou baixe o projeto**
```bash
cd ReponseJsonProject
```

2. **Crie e ative o ambiente virtual**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install django djangorestframework
```

4. **Execute as migrações**
```bash
python manage.py migrate
```

5. **Inicie o servidor**
```bash
python manage.py runserver
```

6. **Acesse no navegador**
- Interface web: http://localhost:8000/
- API JSON: http://localhost:8000/api/usuarios/

## 📊 Dados da Aplicação

Os dados estão fixos na aplicação e representam:

| Nome  | Email               |
|-------|---------------------|
| Carlos | carlos@email.com   |
| João  | joão@email.com     |

## 🎨 Layout e Design

A interface apresenta:
- **Design moderno** com gradientes e sombras
- **Layout responsivo** para mobile e desktop
- **Cards organizados** com dados formatados
- **Syntax highlighting** para o código JSON
- **Animações suaves** e efeitos hover

## 🔧 Desenvolvimento

### Arquivos Principais:

- **`usuarios/views.py`**: Contém a lógica da aplicação
- **`usuarios/templates/home.html`**: Template HTML da interface
- **`static/css/style.css`**: Estilos CSS personalizados
- **`backend/urls.py`**: Configuração de URLs

### Customizações CSS:
- Gradientes modernos
- Cards com sombras e bordas arredondadas
- Destaque de sintaxe para JSON
- Design responsivo com Grid CSS

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais.

---

**Desenvolvido com ❤️ usando Django REST Framework**
