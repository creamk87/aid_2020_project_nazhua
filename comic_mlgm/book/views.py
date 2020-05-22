from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.db.models import F
import os
import time
import hashlib
from .models import *


# Create your views here.
def main(request):
    # 添加章节
    if request.method == "GET":
        return render(request, 'book/main.html')
    if request.method == "POST":
        try:
            book_id = request.POST['ID']
            begin = request.POST['begin']
            end = request.POST['end']
        except Exception as e:
            print(e)
            return HttpResponse('输入错误')

        md5 = hashlib.md5()
        path = f'{settings.BASE_DIR}/book/static/book/img/{book_id}/open'
        for chapterID in range(int(begin), int(end) + 1):
            try:
                list_book = os.listdir(f'{path}/{chapterID}')
                list_book.sort(key=lambda x:int(x.split('.')[0]))
            except FileNotFoundError:
                return HttpResponse('图片文件未上传')
            for index, img in enumerate(list_book):
                try:
                    new_id = int(book_id) << 24 | chapterID << 8 | index + 1
                except Exception as e:
                    print(e)
                    return HttpResponse('服务器文件夹设置错误')
                md5.update(f'{time.time()}{book_id}{chapterID}{img}'.encode())
                new_name = f'{md5.hexdigest()}'
                # 图片入库 和改名
                try:
                    PictureName.objects.create(pictureID=new_id, picture_name=new_name)
                except Exception as e:
                    print(e)
                    return HttpResponse(f'{index}图片插入数据库失败{book_id}/{chapterID}/{new_name}')
                os.rename(f'{path}/{chapterID}/{img}', f'{path}/{chapterID}/{new_name}.jpg')
            # 章节上传完成，更新总章节数
            ComicBook.objects.filter(id=book_id).update(all_number=F('all_number') + 1)
            ComicPath.objects.filter(id=book_id).update(all_number=F('all_number') + 1)
        return HttpResponse('存入成功')


def rename(request):
    # 更改文件夹名字
    return None


def new(request):
    # 创建一本新的漫画
    if request.method == 'GET':
        return render(request, 'book/new.html')
    if request.method == 'POST':
        try:
            book_name = request.POST['book_name']
            book_writer = request.POST['book_writer']
            book_classify = request.POST['book_classify']
        except Exception as e:
            print(e)
            return HttpResponse('提交数据错误，请仔细检查')
        # 将标签转换为二进制
        classify_by = 0
        for index, i in enumerate(book_classify[::-1]):
            classify_by = classify_by | int(i) << index

        # 在主表创建该图书数据
        book = ComicBook.objects.create(name=book_name, writer=book_writer, classify=classify_by, all_number=0)
        book_id = book.id
        # 在从表创建该图书数据
        ComicPath.objects.create(id_id=book_id, all_number=0)
        # 创建该书文件夹
        os.mkdir(f'{settings.BASE_DIR}/book/static/book/img/{book_id}')
        os.mkdir(f'{settings.BASE_DIR}/book/static/book/img/{book_id}/open')
        os.mkdir(f'{settings.BASE_DIR}/book/static/book/img/{book_id}/vip')
        return render(request, 'book/main.html')
