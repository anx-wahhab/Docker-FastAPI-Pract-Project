# base image
FROM python:3.10

# work directory
WORKDIR /app

# copy command ==> copy all files to app dir
COPY . /app
# run
RUN pip install -r requirements.txt

# port export
EXPOSE 8501

# executable command
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8501"]