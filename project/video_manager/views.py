from django.shortcuts import render
from .models import Video, Comment
# Create your views here.
def home(request):
    videos = Video.objects.all()
    
    context = {
                'videos': videos 
                }
    return render(request,'video_manager/home.html', context)

def upload(request):
    if request.method == "POST":
        title  = request.POST.get('title')
        description = request.POST.get('description')
        video_file = request.POST.get('video_file')
        thumbnail = request.POST.get('thumbnail')

        data = Video(
            title=title,
            description=description,
            video_file=video_file,
            thumbnail=thumbnail
        )
        try:
            data.save()
            return redirect('home')
        except:
            messages.error('Video could not be upload')
    return render(request,'video_manager/video_upload.html')

def watch(request, id):
    video = Video.objects.get(id=id)
    context = {
                'video': video 
                }
    return render(request,'video_manager/video_view.html', context)

def react(request):
    pass

def comment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')

        data = Comment(
            comment=comment
        )
        try:
            data.save()
        except:
            messages.error("There was a problem!! Try Again.")
