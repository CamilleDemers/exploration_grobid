import docker

# Initialisation du client Docker
client = docker.from_env()

# Image Docker de GROBID
grobid_image = 'lfoppiano/grobid' 
image_digest = 'sha256:bdcef8653dec41432532a29a65a98ddf390b5b4e37f2cdc904c835c93c8f9652'

# Lancer le conteneur avec le port 8070 local exposé
container = client.containers.run(
    image=image_digest, 
    ports={'8070/tcp': 8070},  # Mappage du port local 8070 vers le port 8070 du conteneur
    detach=True  # Détacher pour que le conteneur s'exécute en arrière-plan
)

print(f"Le conteneur est démarré avec l'ID : {container.short_id}")
print('Pour accéder au service Web: http://localhost:8070/')