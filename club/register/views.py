from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def home(request):
    clubs = Club.objects.all()
    return render(request, 'home.html', {'clubs': clubs})

def detail(request, club_id):
    club = get_object_or_404(Club, pk=club_id)
    return render(request, "detail.html", {'club': club})

def register(request):
    if request.method == 'POST':
        club = Club()
        club.club_name = request.POST['club_name']
        club.introduction = request.POST['introduction']
        club.member = int(request.POST['member'])
        return redirect('detail', club.id)
    return render(request, 'register.html')

def edit(request, id):
    edit_post = Club.objects.get(id=id)
    return render(request, 'edit.html', {'club': edit_post})

def update(request, id):
    if request.method == 'GET':
        return render(request, 'edit.html')
    else:
        club = Club.objects.get(id=id)
        club.club_name = request.POST['club_name']
        club.introduction = request.POST['introduction']
        club.member = int(request.POST['member'])
        club.save()
        return redirect('detail', club.id)

def delete(request, id):
    delete_club = Club.objects.get(id=id)
    delete_club.delete()
    return redirect('home')