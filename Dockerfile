FROM python:3.8-slim

ENV FLASK_APP app.py

COPY app.py ./
COPY templates templates/
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

# Run main.py when the container launches
ENTRYPOINT [ "flask" ]
# run the app main.py
CMD [ "run" ]