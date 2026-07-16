#!/bin/bash

set -e

source "$(dirname "$0")/../config/db.conf"

echo "🚀 Starting PostgreSQL..."

cd "$DOCKER_DIR"

docker compose -f "$COMPOSE_FILE" up -d

echo "✅ PostgreSQL is running."