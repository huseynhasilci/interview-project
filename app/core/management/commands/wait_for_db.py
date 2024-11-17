"""
Django command to wait for the datbase to be available.
"""
import time

from psycopg2 import OperationalError as PostgreOpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database start up"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up = False

        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (PostgreOpError, OperationalError):
                self.stdout.write('Database unavailable...')
                time.sleep(3)

        self.stdout.write(self.style.SUCCESS('Database available.'))
