FROM python:3.7

WORKDIR /app
RUN pip install pipenv
COPY Pipfile Pipfile.lock .

RUN pipenv install --system --deploy

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]