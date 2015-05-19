from django import forms

from .models import OPMLStorage


class OPMLUploadForm(forms.ModelForm):
    class Meta:
        model = OPMLStorage
        fields = ('opml_file', )
