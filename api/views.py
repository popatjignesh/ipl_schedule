from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from cricket.models import *
from cricket.serializers import *
from rest_framework.views import APIView
from datetime import date
from django.db.models import Q
from datetime import datetime,date
from datetime import timedelta

class register(APIView):
	def post(self, request, format=None):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			psw1 = request.data['password']
			psw2 = request.data['confirm_password']
			if psw1 == psw2:
				obj = serializer.save()
				obj.set_password(request.data['password'])
				obj.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			else:
				return Response({'error': 'Both passwords must be same...!'}, status=status.HTTP_406_NOT_ACCEPTABLE)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class team(APIView):
	def post(self, request, format=None):
		serializer = TeamSerializer(data=request.data)
		if serializer.is_valid():
			t_count = Team.objects.all().count()
			if t_count < 8:
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			else:
				return Response({'error': 'You can not add more than 8 teams.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, format=None):
		teams = Team.objects.all()
		serializer = TeamSerializer(teams, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class team_detail(APIView):
	def get(self, request, pk, format=None):
		try:
			team = Team.objects.get(id=pk)
		except:
			return Response({'error': 'Team id not found'}, status=status.HTTP_400_BAD_REQUEST)
		serializer = TeamSerializer(team, many=False)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def delete(self, request, pk, format=None):
		try:
			team = Team.objects.get(id=pk)
		except:
			return Response({'error': 'Team id not found'}, status=status.HTTP_400_BAD_REQUEST)
		team.delete()
		return Response({'success': 'Team deleted successfully'}, status=status.HTTP_200_OK)

	def put(self, request, pk, format=None):
		try:
			team = Team.objects.get(id=pk)
		except:
			return Response({'error': 'Team id not found'}, status=status.HTTP_400_BAD_REQUEST)
		
		serializer = TeamSerializer(team, data=request.data, many=False)
		
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class venue(APIView):
	def post(self, request, format=None):
		serializer = VenueSerializer(data=request.data)
		if serializer.is_valid():
			v_count = Venue.objects.all().count()
			if v_count < 8:
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			else:
				return Response({'error': 'You can not add more than 8 venues.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, format=None):
		venues = Venue.objects.all()
		serializer = VenueSerializer(venues, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class venue_detail(APIView):
	def get(self, request, pk, format=None):
		try:
			venue = Venue.objects.get(id=pk)
		except:
			return Response({'error': 'Venue id not found'}, status=status.HTTP_400_BAD_REQUEST)
		serializer = VenueSerializer(venue, many=False)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def delete(self, request, pk, format=None):
		try:
			venue = Venue.objects.get(id=pk)
		except:
			return Response({'error': 'Venue id not found'}, status=status.HTTP_400_BAD_REQUEST)
		venue.delete()
		return Response({'success': 'Venue deleted successfully'}, status=status.HTTP_200_OK)

	def put(self, request, pk, format=None):
		try:
			venue = Venue.objects.get(id=pk)
		except:
			return Response({'error': 'Venue id not found'}, status=status.HTTP_400_BAD_REQUEST)		

		serializer = VenueSerializer(venue, data=request.data, many=False)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class match(APIView):
	def post(self, request, format=None):
		serializer = MatchSerializer(data=request.data)
		if serializer.is_valid():
			date = request.data.get('date')
			d1 = datetime.strptime(date, '%Y-%m-%d')
			no = d1.isoweekday()
			count = Match.objects.filter(date=date).count()

			if no in [1,2,3,4,5] and count < 1:
				h_team = request.data.get('home_team')
				a_team = request.data.get('away_team')
				if h_team == a_team:
					return Response({'error': 'Both teams can not be same.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
				else:
					serializer.save()
					return Response(serializer.data, status=status.HTTP_201_CREATED)				
			elif no in [6,7] and count < 2:
				h_team = request.data.get('home_team')
				a_team = request.data.get('away_team')
				if h_team == a_team:
					return Response({'error': 'Both teams can not be same.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
				else:
					serializer.save()
					return Response(serializer.data, status=status.HTTP_201_CREATED)				
			else:
				if no in [1,2,3,4,5]:
					return Response({'error': 'You can not add more than 1 match on weekdays.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
				elif no in [6,7]:
					return Response({'error': 'You can not add more than 2 match on weekends.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, format=None):
		matches = Match.objects.all()
		serializer = MatchSerializer(matches, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def get(self, request, format=None):
		try:
			team = request.GET['team']
		except:
			team = 0

		try:
			venue = request.GET['venue']
		except:
			venue = 0
		
		try:
			time=request.GET['time']
		except:
			time = 0

		if team == venue == time == 0:
			match = Match.objects.all()
		else:
			match = Match.objects.filter(Q(home_team=team) | Q(away_team=team) | Q(venue=venue) | Q(time=time))
		serializer = MatchSerializer(match, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class match_today(APIView):
	authentication_classes = (TokenAuthentication,)

	def get(self, request, format=None):
		f_team = Favourite.objects.values_list('teams__id',flat=True).filter(user=request.user)
		match = Match.objects.filter(Q(date = date.today()) & (Q(home_team__id_in=f_team) | Q(away_team__id_in=f_team)))
		serializer = MatchSerializer(match, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class match_nextweek(APIView):
	authentication_classes = (TokenAuthentication,)

	def get(self, request, format=None):
		f_team = Favourite.objects.values_list('teams__id',flat=True).filter(user=request.user)
		match = Match.objects.filter(Q(date__range=[today, week]) & (Q(home_team__id_in=f_team) | Q(away_team__id_in=f_team)))
		serializer = MatchSerializer(match, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class match_detail(APIView):
	def get(self, request, pk, format=None):
		try:
			match = Match.objects.get(id=pk)
		except:
			return Response({'error': 'Match id not found'}, status=status.HTTP_400_BAD_REQUEST)
		serializer = MatchSerializer(match, many=False)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def delete(self, request, pk, format=None):
		try:
			match = Match.objects.get(id=pk)
		except:
			return Response({'error': 'Match id not found'}, status=status.HTTP_400_BAD_REQUEST)
		match.delete()
		return Response({'success': 'Match deleted successfully'}, status=status.HTTP_200_OK)

	def put(self, request, pk, format=None):
		try:
			match = Match.objects.get(id=pk)
		except:
			return Response({'error': 'Match id not found'}, status=status.HTTP_400_BAD_REQUEST)

		serializer = MatchSerializer(match, data=request.data, many=False)

		if serializer.is_valid():
			h_team = request.data.get('home_team')
			a_team = request.data.get('away_team')
			if h_team == a_team:
				return Response({'error': 'Both teams can not be same.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
			else:
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class favourite(APIView):
	authentication_classes = (TokenAuthentication,)

	def post(self, request, format=None):
		if request.user.is_authenticated():
			serializer = FavouriteSerializer(data=request.data)
			teams = request.data.get("teams","").strip().split(',')
			if serializer.is_valid():
				u_id = request.user.id
				e = Favourite.objects.filter(user_id=u_id).exists()
				if e:
					return Response({'error': 'You already added favourite teams earlier.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
				else:
					l = len(teams)
 					if l < 4:
						obj = serializer.save()
						obj.teams = teams if teams else []
						obj.save()
						serializer = FavouriteSerializer(obj)
						return Response(serializer.data, status=status.HTTP_201_CREATED)
 					else:
						return Response({'error': 'You can not add more than 3 teams to favourite.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response({'error': 'You are not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

	def get(self, request, format=None):
		fav = Favourite.objects.all()
		serializer = FavouriteSerializer(fav, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class favourite_detail(APIView):
	authentication_classes = (TokenAuthentication,)
	
	def get(self, request, pk, format=None):
		try:
			fav = Favourite.objects.get(id=pk)
		except:
			return Response({'error': 'Favourite id not found'}, status=status.HTTP_400_BAD_REQUEST)

		usr = request.user
		owner = fav.user

		if usr == owner:
			serializer = FavouriteSerializer(fav, many=False)
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response({"error": "You are not authenticated to view other user's favourite teams."}, status=status.HTTP_401_UNAUTHORIZED)

	def delete(self, request, pk, format=None):
		try:
			fav = Favourite.objects.get(id=pk)
		except:
			return Response({'error': 'Favourite id not found'}, status=status.HTTP_400_BAD_REQUEST)

		usr = request.user
		owner = fav.user

		if usr == owner:
			fav.delete()
			return Response({'success': 'Favourite deleted successfully'}, status=status.HTTP_200_OK)
		else:
			return Response({"error": "You are not authenticated to delete other user's favourite teams."}, status=status.HTTP_401_UNAUTHORIZED)

	def put(self, request, pk, format=None):
		try:
			fav = Favourite.objects.get(id=pk)
		except:
			return Response({'error': 'Favourite id not found'}, status=status.HTTP_400_BAD_REQUEST)

		if request.user.is_authenticated():
			usr = request.user
			owner = fav.user

			if usr == owner:
				serializer = FavouriteSerializer(fav, data=request.data, many=False)
				teams = request.data.get("teams","").strip().split(',')
				if serializer.is_valid():
					u_id = request.user.id
					e = Favourite.objects.filter(user_id=u_id).exists()
					if e:
						l = len(teams)
	 					if l < 4:
							obj = serializer.save()
							obj.teams = teams if teams else []
							obj.save()
							serializer = FavouriteSerializer(obj)
							return Response(serializer.data, status=status.HTTP_201_CREATED)
	 					else:
							return Response({'error': 'You can not add more than 3 teams to favourite.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
					else:
						return Response({"error": "You haven't added any favourite teams yet. Please add favourite teams first."}, status=status.HTTP_406_NOT_ACCEPTABLE)
				else:
					return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
			else:
				return Response({"error": "You are not authenticated to update other user's favourite teams."}, status=status.HTTP_401_UNAUTHORIZED)
		else:
			return Response({'error': 'You need to login first.'}, status=status.HTTP_401_UNAUTHORIZED)

