#!/bin/bash

# Check if a directory is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 directory"
    exit 1
fi

SOURCE_DIR="$1"

# Check if the provided argument is a directory
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: $SOURCE_DIR is not a directory"
    exit 1
fi

# Create a backup directory if it doesn't exist
BACKUP_DIR="$HOME/backups"
mkdir -p "$BACKUP_DIR"

# Create a timestamp for the backup filename
TIMESTAMP=$(date +"%Y%m%d%H%M%S")

# Define the backup filename
BACKUP_FILE="$BACKUP_DIR/backup_$TIMESTAMP.tar.gz"

# Create the backup
tar -czf "$BACKUP_FILE" -C "$SOURCE_DIR" .

# Check if the backup was successful
if [ $? -eq 0 ]; then
    echo "Backup successful: $BACKUP_FILE"
else
    echo "Backup failed"
    exit 1
fi
