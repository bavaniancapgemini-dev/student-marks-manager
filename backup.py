import shutil

def backup_database():

    shutil.copy(
        "school.db",
        "school_backup.db"
    )

    print(
        "Backup Created"
    )