# Учебная сборка: устанавливаем пакет StudyShop с его Python-зависимостями.
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app

# Непривилегированный пользователь для выполнения сервиса.
RUN useradd --create-home --uid 10001 appuser

COPY pyproject.toml README.md ./
COPY studyshop/ ./studyshop/
RUN python -m pip install --no-cache-dir .

USER appuser
EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "studyshop.web:app"]
