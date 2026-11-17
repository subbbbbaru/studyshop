# StudyShop: кэшируем внешние пакеты отдельно от часто меняющегося исходного кода.
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app

RUN useradd --create-home --uid 10001 appuser

# Зависимости меняются реже, чем код: слой остаётся CACHED при правке web.py.
COPY requirements-runtime.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    python -m pip install -r requirements-runtime.txt

# Теперь устанавливаем учебный Python-пакет без повторного разрешения зависимостей.
COPY pyproject.toml README.md ./
COPY studyshop/ ./studyshop/
RUN --mount=type=cache,target=/root/.cache/pip \
    python -m pip install --no-deps .

USER appuser
EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "studyshop.web:app"]
