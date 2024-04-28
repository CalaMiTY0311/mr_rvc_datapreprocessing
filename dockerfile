FROM python:3.9

COPY ./processor /processor
WORKDIR /processor

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python","ffmpeg.py"]
CMD ["python","main.py"]
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]