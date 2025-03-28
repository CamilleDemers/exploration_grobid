Ce répertoire content les scripts nécessaires pour lancer un serveur GROBID à partir de son image Docker ainsi qu'à interagir avec le client python de GROBID pour traiter des pichiers PDFs en lot.

*Pour accéder au service Web de GROBID via un navigateur*
- Installer Docker : https://docs.docker.com/get-started/get-docker/  
- Lancer Docker et attendre que l'engin soit activé  
- Ouvrir le terminal et saisir la commande pour exécuter l'image souhaitée (https://grobid.readthedocs.io/en/latest/Run-Grobid/)    
  `docker run --rm --init --ulimit core=0 -p 8070:8070 lfoppiano/grobid:0.8.1`
- Ouvrir un navigateur au port local où le serveur est exposé (http://localhost:8070/)  

*Pour accéder au client Python de GROBID*
``` 
# Lancer un serveur Docker avec l'image de GROBID 
python src/lancer_serveur_docker.py

# Exécuter le client Grobid pour traiter des fichiers en lot
python src/grobid.py

# Arrêter le serveur une fois les fichiers traités
python src/arreter_serveur_docker.py
```




