FROM svizor/zoomcamp-model:3.11.5-slim


RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "predict.py", "./"]
RUN pipenv install --system --deploy

EXPOSE 6969

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:6969", "predict:app"]