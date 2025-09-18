# Go For It Gas & Liquor - Docker Compose Makefile

# Variables
CONTAINER_NAME = go-for-it-container
IMAGE_NAME = oven/bun:1-alpine
EXTERNAL_PORT = 4000
INTERNAL_PORT = 3000

# Start the container with docker-compose
up:
	docker-compose up -d

# Start the container interactively
up-interactive:
	docker-compose up

# Stop the container
down:
	docker-compose down

# Pull the latest Bun image
pull:
	docker pull $(IMAGE_NAME)

# Execute into the running container
exec:
	docker exec -it $(CONTAINER_NAME) /bin/sh

# Execute into the running container with bash
exec-bash:
	docker exec -it $(CONTAINER_NAME) /bin/bash

# Show container logs
logs:
	docker-compose logs -f

# Show running containers
ps:
	docker ps

# Clean up everything
clean: down
	docker system prune -f

# Clean up everything including images
clean-all: down
	docker system prune -af

# Install bun in the container (if not already installed)
install-bun:
	docker exec -it $(CONTAINER_NAME) curl -fsSL https://bun.sh/install | sh

# Show bun version
bun-version:
	docker exec -it $(CONTAINER_NAME) bun --version

# Show node version
node-version:
	docker exec -it $(CONTAINER_NAME) node --version

# Help
help:
	@echo "Available commands:"
	@echo "  up              - Start the container with docker-compose"
	@echo "  up-interactive  - Start the container interactively"
	@echo "  down            - Stop the container"
	@echo "  pull            - Pull the latest Bun image"
	@echo "  exec            - Execute into the running container (sh)"
	@echo "  exec-bash       - Execute into the running container (bash)"
	@echo "  logs            - Show container logs"
	@echo "  ps              - Show running containers"
	@echo "  clean           - Clean up everything"
	@echo "  clean-all       - Clean up everything including images"
	@echo "  bun-version     - Show bun version"
	@echo "  node-version    - Show node version"
	@echo "  help            - Show this help message"
	@echo ""
	@echo "Quick start:"
	@echo "  1. make up      (starts container with official Bun image)"
	@echo "  2. make exec    (enter container)"
	@echo "  3. Inside container: bun --version (to verify bun is installed)"
	@echo ""
	@echo "Port Configuration:"
	@echo "  External: $(EXTERNAL_PORT) (host machine)"
	@echo "  Internal: $(INTERNAL_PORT) (container)"
	@echo "  Access: http://localhost:$(EXTERNAL_PORT)"

.PHONY: up up-interactive down pull exec exec-bash logs ps clean clean-all bun-version node-version help
