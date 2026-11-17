# StudyShop: Docker, Registry, CI и VPS (обновлённый мастер-класс)

Продолжение проекта прошлого занятия. API: `GET /`, `GET /health`,
`GET /calculate?price=100&quantity=3&discount=10` (ожидается total=270).

## Подготовка

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m pytest -q
```

## Docker

```bash
docker run --rm hello-world
docker build --progress=plain -t studyshop-web:1.0.0 .
docker run -d --name studyshop-web -p 127.0.0.1:8080:8080 studyshop-web:1.0.0
# В браузере http://127.0.0.1:8080/health
docker stop studyshop-web
docker rm studyshop-web
```

## Compose

```bash
docker compose config -q
docker compose up -d --build
docker compose ps
docker compose logs --tail 20
docker compose down
```

## Кэш времени сборки

`Dockerfile.original` — исходная сборка; `Dockerfile` — оптимизированная.
Внешние рабочие зависимости в `requirements-runtime.txt` должны соответствовать
`[project].dependencies` в `pyproject.toml`.

```bash
docker build --progress=plain -f Dockerfile.original -t studyshop:original .
docker build --progress=plain -t studyshop:optimized .
# Отредактируйте studyshop/web.py и повторите последнюю команду:
# шаг pip install -r requirements-runtime.txt должен быть CACHED.
```

Кэш-монтирование pip помогает повторным сборкам на той же машине; GitHub Actions
использует экспортируемый кэш слоёв `type=gha`, который не переносит pip cache mount
по умолчанию. Оптимизация времени может не уменьшать размер образа.

## Registry и VPS

Публикуйте точный тег `YOUR_DOCKER_ID/studyshop-web:v1.0.0`.
В `deploy-vps.yml` используются Secrets: SSH_HOST, SSH_USER, SSH_PRIVATE_KEY,
SSH_KNOWN_HOSTS, DOCKER_USERNAME. SSH_KNOWN_HOSTS должен содержать проверенную
строку формата `адрес ssh-ed25519 AAAA...`, а не только содержимое `.pub`.
При запуске VPS Docker слушает только 127.0.0.1:8080 на VPS; используйте SSH-туннель.

Подробные объяснения, диагностика ошибок SSH/Docker/Registry и сценарий занятия — в DOCX.
