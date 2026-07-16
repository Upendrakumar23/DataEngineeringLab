#!/bin/bash

set -e

source "$(dirname "$0")/../config/db.conf"

echo "🛑 Stopping PostgreSQL..."

cd "$DOCKER_DIR"

docker compose -f "$COMPOSE_FILE" down

echo "✅ PostgreSQL stopped."