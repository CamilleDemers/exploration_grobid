import docker

# Initialisation du client Docker
client = docker.from_env()

# Digest de l'image que vous recherchez
target_digest = 'sha256:bdcef8653dec41432532a29a65a98ddf390b5b4e37f2cdc904c835c93c8f9652'

# Parcourir tous les conteneurs actifs pour trouver celui avec l'image correspondante
for container in client.containers.list():
    image_id = container.image.id  # ID de l'image du conteneur
    if target_digest in image_id:
        print(f"Conteneur trouvé : {container.short_id}")
        
        # Arrêter le conteneur
        container.stop()
        print(f"Le conteneur avec l'ID {container.short_id} a été arrêté.")
        break
else:
    print("Aucun conteneur trouvé pour le digest spécifié.")
