from django.http import JsonResponse
from django.shortcuts import render
from book.models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def details(request):
    return render(request, 'details.html')


def picture(request):
    return JsonResponse([{'name': book.name,
                          'path': f'/static/book/img/{book.id}/{ComicPath.objects.get(id_id=book.id).open_name}/1/{PictureName.objects.get(pictureID=book.id << 24 | 1 << 8 | 1).picture_name}.jpg',
                          'id': f'{book.id}'}
                         for book in ComicBook.objects.all()], safe=False)


def details_id(request, x):
    count = 1
    list01 = []
    while True:
        try:
            list01.append({
                              'path': f'/static/book/img/{x}/{ComicPath.objects.get(id_id=x).open_name}/{count}/{PictureName.objects.get(pictureID=x << 24 | count << 8 | 1).picture_name}.jpg'})
            count += 1
        except Exception:
            return JsonResponse(list01, safe=False)
