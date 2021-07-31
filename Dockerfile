FROM python:latest
ENV PYTHONBUFFERED 1
RUN mkdir /dataFlowDashboard
WORKDIR /dataFlowDashboard
ADD . /dataFlowDashboard/
ADD requirements.txt /backend
RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

