from django.shortcuts import render

# Create your views here.

def addAlbum(req):
    return render(req,'album_form.html')
def editAlbum(req):
    return render(req,'album_form.html')
    
# def addAlbum(req):
#     return render(req,'album_form.html')