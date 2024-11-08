from django.shortcuts import render, get_object_or_404
from  .models import Hamburger

def hamburger_detail(request, id):
    hamburger = get_object_or_404(Hamburger, id=id)
    return render(request, 'hamburger.html', {'hamburger': hamburger})