from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt

from .models import Author

# Create your views here.
@csrf_exempt
def hooks(request):
    if request.method == 'POST':

        x = request.body
        x=json.loads(x)
        print(x)
        b = Author(name=x['name'])
        b.save()
        try:
            one_entry = Author.objects.get(name = 'Deepak')
        except :
            one_entry=None
        print(one_entry)
        convid = one_entry.email
        print(convid)
        return HttpResponse("nice")

