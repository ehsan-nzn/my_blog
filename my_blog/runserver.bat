@echo off
start cmd /k "cd.. && cd .venv\Scripts && activate && cd.. && cd.. && cd my_blog && py manage.py runserver"