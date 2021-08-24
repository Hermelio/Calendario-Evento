from datetime import datetime
from django.db import models
from django.urls import reverse

from calendarapp.models import EventAbstract
from accounts.models import User


class EventManager(models.Manager):
    """ Event manager """

    def get_all_events(self, user):
        events = Event.objects.filter(
            user=user, is_active=True, is_deleted=False
        )
        return events

    def get_running_events(self, user):
        running_events = Event.objects.filter(
            user=user, is_active=True, is_deleted=False,
            inicio=datetime.now().date()
        ).order_by('inicio')
        return running_events


class Event(EventAbstract):
    """ Event model """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='events'
    )
    titulo = models.CharField(max_length=200, unique=True)
    descricao = models.TextField()
    inicio = models.DateTimeField()
    final = models.DateTimeField()

    objects = EventManager()

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('calendarapp:event-detail', args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse('calendarapp:event-detail', args=(self.id,))
        return f'<a href="{url}"> {self.titulo} </a>'
