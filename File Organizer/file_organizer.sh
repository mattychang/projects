#!/bin/bash

# Check if a directory is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 directory"
    exit 1
fi

TARGET_DIR="$1"

# Check if the provided argument is a directory
if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: $TARGET_DIR is not a directory"
    exit 1
fi

# Function to get the directory name based on file extension
get_directory_name() {
    case "$1" in
        jpg|jpeg|png|gif|bmp) echo "Images" ;;
        mp3|wav|flac) echo "Music" ;;
        mp4|mkv|avi|mov) echo "Videos" ;;
        doc|docx|pdf|txt|odt) echo "Documents" ;;
        zip|tar|gz|bz2|rar) echo "Archives" ;;
        *) echo "Others" ;;
    esac
}

# Function to organize files
organize_files() {
    for FILE in "$TARGET_DIR"/*; do
        if [ -f "$FILE" ] && [ "$(basename "$FILE")" != "$(basename "$0")" ]; then
            EXT="${FILE##*.}"
            EXT=$(echo "$EXT" | tr '[:upper:]' '[:lower:]')
            DIR=$(get_directory_name "$EXT")
            mkdir -p "$TARGET_DIR/$DIR"
            if mv "$FILE" "$TARGET_DIR/$DIR/"; then
                echo "Moved $FILE to $TARGET_DIR/$DIR/"
            else
                echo "Failed to move $FILE to $TARGET_DIR/$DIR/"
            fi
        fi
    done
}

# Run the function to organize files
organize_files

echo "File organization complete!"
