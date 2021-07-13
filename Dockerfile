FROM python:3.7

WORKDIR /app
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./

RUN pipenv install --system --deploy

COPY ./app /app
COPY ./ml_models /app/ml_models

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]