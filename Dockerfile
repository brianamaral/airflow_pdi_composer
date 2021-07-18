FROM apache/airflow
COPY requirements.txt .
RUN pip install -r requirements.txt