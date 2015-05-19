from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .forms import OPMLUploadForm


def upload_opml(request):
    form = OPMLUploadForm()

    if request.method == 'POST':
        form = OPMLUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('home'))

    return render(request, 'user_profile/upload_opml.html', { 'form' : form })
