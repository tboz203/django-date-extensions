from django.shortcuts import render_to_response
from . import forms 
from django.views.decorators.http import require_GET


@require_GET
def view(request):
    form = forms.ExampleForm(request.GET or None)
    # form = forms.DatesForm(request.GET or None)
    if form.is_valid():
        form.save()
    return render_to_response('form.html', {'form': form})

