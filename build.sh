#! /bin/bash

# Stop and remove existing containers
docker compose down

# Remove old images
docker compose rm -f

# Clean up
docker system prune -f

# Build the images and Start the containers
docker compose up --build -d


echo "Build and deployment complete."

docker ps

echo "check above info for docker containers' details"


