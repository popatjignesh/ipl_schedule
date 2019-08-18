from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from cricket.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')


class TeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = Team


class VenueSerializer(serializers.ModelSerializer):
	class Meta:
		model = Venue


class MatchSerializer(serializers.ModelSerializer):
	class Meta:
		model = Match


class FavouriteSerializer(serializers.ModelSerializer):
	teams = TeamSerializer(many=True, read_only=True)

	class Meta:
		model = Favourite
		fields = ('user', 'teams')