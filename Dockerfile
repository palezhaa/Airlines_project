# базовый образ с Python 3
FROM python:3.9

# задаем рабочую директорию
WORKDIR    /opt/oracle
# устанавливаем зависимости проекта
RUN apt-get update && apt-get install -y libaio1

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install cx_Oracle
RUN pip install pandas
RUN pip install openpyxl

RUN cd /opt/oracle \
    && wget https://download.oracle.com/otn_software/linux/instantclient/199000/instantclient-basic-linux.x64-19.9.0.0.0dbru.zip \
    && unzip instantclient-basic-linux.x64-19.9.0.0.0dbru.zip \
    && rm -f instantclient-basic-linux.x64-19.9.0.0.0dbru.zip \
    && echo /opt/oracle/instantclient_19_9 > /etc/ld.so.conf.d/oracle-instantclient.conf \
    && ldconfig

# копируем файлы проекта в рабочую директорию
COPY . .

# задаем переменные окружения для Django
ENV DJANGO_SETTINGS_MODULE=airlines.settings
ENV PYTHONUNBUFFERED=1
ENV LD_LIBRARY_PATH="/opt/oracle/instantclient_19_9"

# открываем порт для приложения
EXPOSE 8000


# запускаем приложение
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]