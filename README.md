# StudyShop: продолжение мастер-класса — Docker и Docker Registry

Это **тот же учебный пакет StudyShop**: сохранены `studyshop/pricing.py`, `studyshop/cli.py`, 6 исходных тестов, `pyproject.toml` и `Makefile`. Добавлены Flask API, четыре HTTP-теста и файлы Docker/CI.

## Локальный запуск

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e '.[dev]'
python -m pytest -q
python -m flask --app studyshop.web run --host 127.0.0.1 --port 8080
```

Проверка: http://127.0.0.1:8080/health и http://127.0.0.1:8080/calculate?price=100&quantity=3&discount=10

## Docker

```bash
docker build -t studyshop-web:1.0.0 .
docker run --rm -d --name studyshop-web -p 127.0.0.1:8080:8080 studyshop-web:1.0.0
docker logs studyshop-web
docker stop studyshop-web
```

## Compose

```bash
docker compose up --build -d
docker compose ps
docker compose down
```

## Docker Hub

Замените `YOUR_DOCKER_ID` своим Docker ID. Создайте репозиторий `studyshop-web` на Docker Hub.

```bash
docker login -u YOUR_DOCKER_ID
docker tag studyshop-web:1.0.0 YOUR_DOCKER_ID/studyshop-web:v1.0.0
docker push YOUR_DOCKER_ID/studyshop-web:v1.0.0
```

## GitHub Actions

`tests.yml` проверяет PR и изменения main/development. `publish.yml` по Git-тегу `v*` проводит тесты и публикует образ; нужны Secrets `DOCKER_USERNAME`, `DOCKER_ACCESS_TOKEN`.

## VPS (отдельное необязательное задание)

Workflow `deploy-vps.yml` запускается вручную, требует **проверенный** `SSH_KNOWN_HOSTS`, `SSH_PRIVATE_KEY`, `SSH_HOST`, `SSH_USER`, `DOCKER_USERNAME`; на сервере заранее должен работать Docker и пользователь должен иметь право запускать Docker. Он связывает порт **только с 127.0.0.1**, поэтому доступ извне организуют отдельно через HTTPS reverse proxy. Не публикуйте порт Docker напрямую в интернет без настройки межсетевого экрана и TLS.

Выполнение Docker-процедур и публикация требуют установленного Docker и доступа в сеть; в архиве нет токенов, паролей, закрытых ключей.
# studyshop
