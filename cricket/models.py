from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import m2m_changed

class Team(models.Model):
	name = models.CharField(max_length = 50, null=True, blank=True)

	class Meta:
		verbose_name = "Team"
		verbose_name_plural = "Team"

	def __str__(self):
		return self.name


class Venue(models.Model):
	stadium_name = models.CharField(max_length = 50, null=True, blank=True)
	address = models.CharField(max_length = 70)
	capacity = models.IntegerField()
	image = models.ImageField(upload_to = 'venue_images/', null=True, blank=True)

	class Meta:
		verbose_name = "Stadium Name"
		verbose_name_plural = "Stadium Name"

	def __str__(self):
		return self.address


class Match(models.Model):
	times = (
		('4','4 PM'),
		('8','8 PM'),
		)

	date = models.DateField()
	time = models.CharField(choices=times, max_length = 10)
	home_team = models.ForeignKey(Team, related_name='hometeams',)
	away_team = models.ForeignKey(Team, related_name='awayteams',)
	venue = models.ForeignKey(Venue, related_name="venues",)

	class Meta:
		verbose_name = "Match"
		verbose_name_plural = "Match"

	def __str__(self):
		return self.home_team.name + ' vs. ' + self.away_team.name


class Favourite(models.Model):
	user = models.ForeignKey(User, related_name='users',)
	teams = models.ManyToManyField(Team, null=True, blank=True)

	class Meta:
		verbose_name = "Favourite"
		verbose_name_plural = "Favourite"

	def __str__(self):
		return self.user.username