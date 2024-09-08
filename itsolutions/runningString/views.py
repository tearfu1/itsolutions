from wsgiref.util import FileWrapper

from django.shortcuts import render
from django.http import HttpResponse

from rs import create_text_video
from runningString.models import Prompts


# Create your views here.
def index(request):
    if request.GET['prompt']:
        prompt = request.GET['prompt']
        Prompts.objects.create(prompt=prompt)
        create_text_video(prompt)
        file = FileWrapper(open('videos/output.mp4', 'rb'))
        response = HttpResponse(file, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename=output.mp4'
    return response