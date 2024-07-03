# Automated Backup Shell Script
## Author: Matthew Chang

This shell script backs up all files in a specified directory by creating a compressed archive of the directory. The backup file will be named with the current date and time for easy identification.

## Usage

To use this script, follow these steps:

1. Save the script to a file, e.g., `backup.sh`.
2. Make the script executable by running:
    ```sh
    chmod +x backup.sh
    ```
3. Run the script with the directory you want to back up as an argument:
    ```sh
    ./backup.sh /path/to/your/directory
    ```

## Features

- Backs up all files in the specified directory.
- Creates a backup directory (`~/backups`) in the user's home directory if it doesn't already exist.
- Names the backup file with the current date and time for easy identification.

## Script Explanation

### Argument Check

The script checks if a directory argument is provided. If not, it prints a usage message and exits.

### Directory Check

The script verifies if the provided argument is a valid directory. If not, it prints an error message and exits.

### Backup Directory

The script creates a backup directory (`$HOME/backups`) if it doesn't already exist.

### Timestamp

A timestamp (`YYYYMMDDHHMMSS`) is created to uniquely identify the backup file.

### Backup Filename

The backup filename is constructed using the backup directory and the timestamp.

### Create Backup

The script uses `tar` to create a compressed archive (`tar.gz`) of the source directory. The `-C` option allows `tar` to change to the source directory before creating the archive, which ensures that the directory structure is preserved.

### Success Check

The script checks if the `tar` command was successful and prints a success or failure message accordingly.
