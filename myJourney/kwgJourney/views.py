from django.shortcuts import render

# Homepage — Learning Journey
def index(request):
    return render(request, 'index.html')

# About Me page
def aboutMe(request):
    return render(request, 'aboutMe.html')
