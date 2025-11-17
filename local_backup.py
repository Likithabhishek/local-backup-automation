import os
import tarfile
import datetime


SOURCE_FOLDER = "/home/likith/mydata"
BACKUP_DIR = "/home/likith/backups"
BACKUP_NAME = f"backup-{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.tar.gz"
BACKUP_PATH = os.path.join(BACKUP_DIR, BACKUP_NAME)



os.makedirs(BACKUP_DIR, exist_ok=True)


with tarfile.open(BACKUP_PATH, "w:gz") as tar:
    tar.add(SOURCE_FOLDER, arcname=os.path.basename(SOURCE_FOLDER))

print(f"Backup created: {BACKUP_PATH}")
