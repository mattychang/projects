# Automated Backup Script

This project provides an automated backup solution using a Python script. The script backs up a specified directory, compresses it, and saves it to a backup location. It also logs the backup operations to keep track of successful backups and any errors.

## Features

- Backup a specified directory.
- Compress the backup into a zip file.
- Save the compressed backup to a specified location.
- Log backup operations and errors.

## Disclaimers
- This does not backup the directory of interest on a timely manner. It only backups the directory when executed.

## Requirements

- Python 3.x
- Libraries: `shutil`, `os`, `zipfile`, `datetime`, `logging`

## Configuration

You need to configure the following parameters in the script:

```python
# Configuration
source_dir = '/path/to/your/source/directory'
backup_dir = '/path/to/your/backup/directory'
```

## Running the script

You can run the script manually from the command line:
```bash
python /path/to/backup_script.py
```

## Logs
The script logs backup operations to a log file located in the backup directory (`backup_log.txt`). This log file includes timestamps, log levels, and messages indicating the success or failure of backup operations.

