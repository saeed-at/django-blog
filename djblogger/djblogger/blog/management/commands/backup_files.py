import os
import shutil
from datetime import datetime
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    """
    To backing up database.

    This command creates timestamped backups of the SQLite database
    maintaining only the 5 most recent backups to manage storage space.

    Attributes
    ----------
    help : str
        Brief description of the command's purpose
    """

    help = "Backup logs and database files"

    def handle(self, *args, **options):
        """
        Execute the backup command.

        Parameters
        ----------
        args : tuple
            Additional positional arguments
        options : dict
            Additional keyword arguments from command line

        Returns
        -------
        None
        """
        # Define backup directory at project root level
        backup_dir = os.path.join(settings.BASE_DIR.parent.parent, "backups")
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        # Generate timestamp in format YYYYMMDD_HHMMSS for unique backup naming
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Retrieve database path from Django settings and create backup if exists
        db_path = settings.DATABASES["default"]["NAME"]
        if os.path.exists(db_path):
            db_backup_path = os.path.join(backup_dir, f"db_backup_{timestamp}.sqlite3")
            shutil.copy2(db_path, db_backup_path)  # copy2 preserves metadata
            self.stdout.write(
                self.style.SUCCESS(f"Database backed up to {db_backup_path}")
            )

        # Maintain backup directory by removing older files
        self._cleanup_old_backups(backup_dir)

    def _cleanup_old_backups(self, backup_dir):
        """
        Remove old backup files keeping only the 5 most recent ones.

        Parameters
        ----------
        backup_dir : str
            Path to the backup directory

        Returns
        -------
        None
        """
        db_backups = sorted(
            [f for f in os.listdir(backup_dir) if f.startswith("db_backup_")]
        )
        # Remove all but the 5 most recent database backups
        if len(db_backups) > 5:
            for old_backup in db_backups[:-5]:
                os.remove(os.path.join(backup_dir, old_backup))
