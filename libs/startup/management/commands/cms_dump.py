from __future__ import print_function, absolute_import, unicode_literals

from django.core.management import BaseCommand, call_command



class Command(BaseCommand):
    """
    Startup restores the main database to its original state. Loads fixtures. Create base user.
    """

    def handle(self, **options):
        self.dump_data()

    @staticmethod
    def dump_data():
        call_command('dumpdata','cms > fixtures/cms.json' )
        call_command('dumpdata', 'custom_plugins', '> fixtures/cms.json' )
