# Utilisez une image Python de base
FROM python:3.9-slim

# Installer les outils de compilation nécessaires
RUN apt-get update && apt-get install -y gcc libc-dev

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier uniquement les fichiers Python dans le répertoire de travail
COPY ./Services/Producers/Weather-Kafka-Streamlit /app/

# Copier le dossier images dans le répertoire de travail
COPY ./images /app/images/

COPY ./Services/Producers/requirements.txt /app/

COPY ./Services/Producers/env.yml /app/

COPY ./Services/Producers/*.py /app/

# Installer les dépendances à partir du fichier requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Exposer les ports si nécessaire (pour Streamlit ou autre)
EXPOSE 8501