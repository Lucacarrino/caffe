# Usa un'immagine Python come base
FROM python:3.9-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file del progetto
COPY . /app/

# Installa le dipendenze
RUN pip install -r requirements.txt

# Raccogli i file statici
RUN python manage.py collectstatic --noinput

# Esponi la porta che il server Django utilizza
EXPOSE 8000

# Comando per avviare l'app
CMD ["gunicorn", "caffe.Giornalino.giornalino.wsgi:application", "--bind", "0.0.0.0:8000"]
