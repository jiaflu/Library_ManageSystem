# -*- coding: utf-8 -*-
from django.db import models

#书库
class Book(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Book_ID')
    Available = models.BooleanField(default=1)
    Title = models.CharField(max_length=64,default='')
    Author = models.CharField(max_length=32, default='')
    ISBN = models.CharField(max_length=32, default='')
    Publisher = models.CharField(max_length=32, default='')
    Pub_Time = models.DateField(null=True)
    # Modified_Time = models.DateTimeField(auto_now=True)
    Pages = models.IntegerField(null=True)
    Description = models.TextField(null=True)
    Position = models.CharField(max_length=8, default='A-101')

    def __unicode__(self):   #python3使用__str__ 作用是美化打印出来的结果
        return str(self.id)

class Reader(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Reader_ID')
    Name = models.CharField(max_length=16, null=False, unique=True)
    Password = models.CharField(max_length=16, null=False)
    Active = models.BooleanField(default=0)

    def __unicode__(self):
        return str(self.id)

class Record(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Record_ID')
    #V=models.ForeignKey(othermodel<, **options>) 外键，关联其它模型，创建关联索引
    Book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name="The_Book")
    Reader = models.ForeignKey('Reader', on_delete=models.CASCADE)
    Created_time = models.DateTimeField(auto_now_add=True)
    Modified_time = models.DateTimeField(auto_created=True)

    WAITFORCHECK = 'WAITFORCHECK'
    BORROWED = 'BORROWED'
    RETURNED = 'RETURN'
    TURNDOWN = 'TURNDOWN'
    STATUS_CHOICES = (
        ( WAITFORCHECK, 'WAITFORCHECK'),
        ( BORROWED , 'BORROWED'),
        ( RETURNED , 'RETURNED'),
        ( TURNDOWN , 'TURNDOWN'),
    )
    Status = models.CharField(
        max_length= 16,
        choices=STATUS_CHOICES, #choices    一个用来选择值的2维元组。第一个值是实际存储的值，第二个用来方便进行选择。
        default=WAITFORCHECK, #缺省值
    )

    def __unicode__(self):
        return str(self.id)