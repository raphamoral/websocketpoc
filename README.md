# websocketpoc

Prova de conceito de WebSocket utilizando Django Channels.

## Executando

```bash
pip install -r requirements.txt  # caso ainda não tenha instalado
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000
```

Acesse `http://localhost:8000/` e verifique no console do navegador os
dados recebidos via WebSocket.
