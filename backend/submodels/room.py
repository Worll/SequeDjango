from django.conf import settings
from django.db import models


class RoomManager(models.Manager):
    def create_instance(self, organizer, playlistUrl, inviteCode):
        instance = self.create(organizer=organizer, playlistUrl=playlistUrl,
                               inviteCode=inviteCode)
        return instance


class Room(models.Model):
    uid = models.AutoField(primary_key=True)
    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    playlistUrl = models.CharField(max_length=255)
    inviteCode = models.CharField(max_length=255)
    objects = RoomManager()
