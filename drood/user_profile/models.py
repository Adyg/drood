import datetime
import opml

from django.db import models


def opml_directory(instance, filename):
    return '/'.join(['opml', str(datetime.datetime.now().year), str(datetime.datetime.now().month), filename])


class OPMLStorage(models.Model):
    IMPORT_STATUS = (
        ('P', 'Pending'),
        ('I', 'Imported'),
        ('F', 'Failed'),
        ('R', 'Import running')
    )

    opml_file = models.FileField(upload_to=opml_directory)
    import_status = models.CharField(max_length=1, choices=IMPORT_STATUS, default='P')

    @classmethod
    def extract_opml(cls, node):
        for child in node:
            #text = (" " * depth) + "* " + child.text
            #blocks.append(text)

            if len(child) > 0:
                cls.extract_opml(child)


    @classmethod
    def import_pending(cls):
        pending_files = cls.objects.filter(import_status='P')

        # mark the files as being imported so they are not picked up by another task
        # pending_files.update(import_status='R')
        for pending_file in pending_files:
            #outline = opml.parse(pending_file.opml_file.url)
            outlines = opml.parse('/vagrant/drood/media/opml/2015/5/sarahmarshallfeedly.opml')
            for outline in outlines:
                print outline.title
                try:
                    print outline.xmlUrl
                except:
                    pass
