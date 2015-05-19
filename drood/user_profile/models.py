import datetime

from django.db import models


def opml_directory(instance, filename):
    return '/'.join(['opml', str(datetime.datetime.now().year), str(datetime.datetime.now().month), filename])


class OPMLStorage(models.Model):
    IMPORT_STATUS = (
        ('P', 'Pending'),
        ('I', 'Imported'),
        ('F', 'Failed'),
    )

    opml_file = models.FileField(upload_to=opml_directory)
    import_status = models.CharField(max_length=1, choices=IMPORT_STATUS, default='P')
