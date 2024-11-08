# app_18_3/views.py

from django.shortcuts import render
from .models import Resume  # Assuming you have a Resume model defined

def resume_view(request):
    resume = Resume.objects.first()  # Get the first Resume instance, or None if it doesn’t exist
    if resume is None:
        return render(request, 'no_resume.html')  # Render no_resume.html if no data is found

    context = {
        'resume': resume,
        'experiences': resume.experiences.all(),  # Adjust according to your model structure
        'education': resume.education.all(),
        'skills': resume.skills.all(),
    }
    return render(request, 'resume.html', context)
