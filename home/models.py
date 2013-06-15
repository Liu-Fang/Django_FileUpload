# # -*- coding:utf-8 -*-

# from django.db import models

# # class SomeFile(models.Model):
# #     name = models.CharField(max_length=255)
# #     file = models.FileField(upload_to='uploaded_files')

# class CateTags(models.Model):
#     """        """
#     uid = models.BigIntegerField(
#         verbose_name='user id', primary_key=True, max_length=10
#         )
#     name = models.CharField(verbose_name='user screen name', max_length=30)


# class Cates(models.Model):
#     """     """
#     id = models.BigIntegerField(
#         verbose_name='user id', primary_key=True, max_length=10
#         )
#     name = models.CharField(verbose_name='cate name', max_length=30)


# def get_cate_tags(cate_num=None):
#     """            """
#     if cate_num:
#         cate = Cates.objects.get(id=cate_num).name
#         ctag = CateTags.objects.filter(pre_tag__contains=cate)
#     else:
#         ctag = CateTags.objects.all()
#     return ctag


# import datetime

# class Item(models.Model):
#     title = models.CharField(maxlength=250)
#     created_date = models.DateTimeField(default=datetime.datetime.now)
#     def __str__(self):
#         return self.title
    
