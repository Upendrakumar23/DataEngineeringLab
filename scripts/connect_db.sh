#!/bin/bash

set -e

source "$(dirname "$0")/../config/db.conf"

echo "Connecting to PostgreSQL..."

docker exec -it "$POSTGRES_CONTAINER" \
    psql -U "$POSTGRES_USER" \
    -d "$POSTGRES_DB"