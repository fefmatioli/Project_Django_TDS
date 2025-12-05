# The ADHD DailyGenda API

API REST com Django REST Framework para gerenciamento pessoal de **notes**, **events** e **tasks** por usuário autenticado.

## Requisitos
- Python 3.10+
- Pip
- Virtualenv recomendado

## Instalação rápida
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
