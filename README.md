# Girls Backend (Django)

Backend for the frontend in `girls-front/OF`.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_girls
python manage.py runserver
```

## Core endpoints

### Auth
- `POST /api/auth/register/` — register `{ username, email?, password }`
- `POST /api/auth/login/` — JWT login `{ username, password }`
- `POST /api/auth/refresh/` — refresh `{ refresh }`
- `GET /api/auth/me/` — current user

### Girl profiles
- `GET /api/girls/` — list
  - query: `search`, `tag`, `is_new=true|false`
- `GET /api/girls/{id}/` — detail

### Chats
- `POST /api/chats/start/` — create/get chat `{ girl_id }`
- `GET /api/chats/` — list
- `GET /api/chats/{id}/` — detail
- `GET /api/chats/{id}/messages/` — messages
- `POST /api/chats/{id}/messages/send/` — send `{ content }`

## Notes
- `SendMessageView` returns two messages: user + mock AI. Replace with a real LLM integration when ready.
- CORS defaults to `http://localhost:3000` via `CORS_ALLOWED_ORIGINS`.
