#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Post(models.Model):

	title = models.CharField('Título', max_length=120, null=False, blank=True)
	autor = models.ForeignKey('auth.User')
	created_date = models.DateTimeField('Data de Criação', default=timezone.now)
	publish_date = models.DateTimeField('Data de Publicação', blank=True, null=True)
	text = models.TextField('Texto')

	def publish(self):
		self.publish_date = timezone.now()
		self.save()

	def __str__(self):
		str = self.title
		return str.encode(encoding='UTF-8', errors='strict')

	def get_absolute_url(self):
		return 'post/%i/' % self.pk