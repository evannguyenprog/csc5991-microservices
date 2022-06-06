FROM python:3.8

WORKDIR /flask_app/venv

ADD assignment1.py .

RUN python -m pip install --upgrade pip
RUN pip install wheel
RUN pip install flask

EXPOSE 5000

CMD ["python3", "assignment1.py"]