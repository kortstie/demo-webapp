FROM python:3.8-slim

#WORKDIR /usr/app

COPY app.py ./
COPY templates templates/
COPY static static/
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

# Run main.py when the container launches
ENTRYPOINT [ "python" ]
# run the app main.py
CMD [ "app.py" ]