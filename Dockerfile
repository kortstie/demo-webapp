FROM python:3.8-slim

#WORKDIR /usr/app

#ENV FLASK_ENV development
ENV FLASK_APP app

COPY app.py ./
COPY templates templates/
COPY static static/
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

# Run main.py when the container launches
ENTRYPOINT [ "flask" ]
# run the app main.py
CMD [ "run" ]