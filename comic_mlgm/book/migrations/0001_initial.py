# Generated by Django 2.2.12 on 2020-06-09 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComicBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='名字')),
                ('writer', models.CharField(max_length=20, verbose_name='作者')),
                ('all_number', models.IntegerField(verbose_name='总章节数')),
                ('update_time', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('set_up_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('is_active', models.BooleanField(default=0, verbose_name='授权')),
                ('classify', models.IntegerField(default=1, verbose_name='标签')),
            ],
        ),
        migrations.CreateModel(
            name='PictureName',
            fields=[
                ('pictureID', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='图片ID')),
                ('picture_name', models.CharField(max_length=50, verbose_name='图片名字')),
            ],
        ),
        migrations.CreateModel(
            name='ComicPath',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='book.ComicBook')),
                ('open_name', models.CharField(default='open', max_length=100, verbose_name='免费dir')),
                ('vip_name', models.CharField(default='vip', max_length=100, verbose_name='会员dir')),
                ('open_number', models.IntegerField(default=9999, verbose_name='免费章节数')),
                ('all_number', models.IntegerField(verbose_name='总章节数')),
            ],
        ),
    ]
