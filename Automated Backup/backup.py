import os
import shutil
import zipfile
from datetime import datetime
import logging

# Configuration
source_dir = '/path/to/your/source/directory'
backup_dir = '/path/to/your/backup/directory'
backup_prefix = 'backup_'

# Ensure the backup directory exists
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# Setup logging
log_file = os.path.join(backup_dir, 'backup_log.txt')
logging.basicConfig(filename=log_file, level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def create_backup(source, backup, prefix):
    try:
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        zip_file_name = os.path.join(backup, f"{prefix}{now}.zip")

        with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, source)
                    zipf.write(file_path, arcname)

        logging.info(f"Backup created successfully: {zip_file_name}")
        print(f"Backup created successfully: {zip_file_name}")
    except Exception as e:
        logging.error(f"Error creating backup: {e}")
        print(f"Error creating backup: {e}")

# Run the backup
create_backup(source_dir, backup_dir, backup_prefix)
