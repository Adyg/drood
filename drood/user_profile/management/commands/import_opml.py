from django.core.management.base import NoArgsCommand
from user_profile.models import OPMLStorage


class Command(NoArgsCommand):
    help = "Import pending OPML files."

    def handle_noargs(self, **options):
        OPMLStorage.import_pending()
