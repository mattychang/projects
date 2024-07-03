# File Organizer Shell Script

This shell script organizes files in a specified directory by creating new directories as needed and moving files into those directories based on their file types.

## Usage

To use this script, follow these steps:

1. Save the script to a file, e.g., `file_organizer.sh`.
2. Make the script executable by running:
    ```sh
    chmod +x file_organizer.sh
    ```
3. Run the script with the directory you want to organize as an argument:
    ```sh
    ./file_organizer.sh /path/to/your/directory
    ```

## Features

- Organizes files based on their file types.
- Creates new directories as needed (e.g., Images, Music, Videos, Documents, Archives, Others).
- Moves files into the appropriate directories.

## Script Explanation

### Argument Check

The script checks if a directory argument is provided. If not, it prints a usage message and exits.

### Directory Check

The script verifies if the provided argument is a valid directory. If not, it prints an error message and exits.

### Directory Name Function

The `get_directory_name` function maps file extensions to directory names.

### Organize Files Function

The `organize_files` function loops through files in the target directory, determines their extension, and moves them to the appropriate directory.
