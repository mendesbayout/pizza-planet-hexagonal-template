FROM python:3.9

# set the directory
WORKDIR /api

#  copy requirements
COPY ./requirements.txt /api/requirements.txt

# install requirements
RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

# copy backend
COPY app /api

#Exponsing the port
EXPOSE 80

#build the image
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
