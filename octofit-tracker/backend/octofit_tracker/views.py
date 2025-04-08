from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import User, Team, Activity, Leaderboard, Workout

@api_view(['GET'])
def api_root(request, format=None):
    base_url = 'http://127.0.0.1:8080/'
    return Response({
        'users': base_url + 'api/users/',
        'teams': base_url + 'api/teams/',
        'activities': base_url + 'api/activities/',
        'leaderboard': base_url + 'api/leaderboard/',
        'workouts': base_url + 'api/workouts/'
    })

class UserViewSet(ViewSet):
    def list(self, request):
        users = User.objects.all()
        data = [{"username": user.username, "email": user.email} for user in users]
        return Response(data)

class TeamViewSet(ViewSet):
    def list(self, request):
        teams = Team.objects.all()
        data = [{"name": team.name, "members": [member.username for member in team.members]} for team in teams]
        return Response(data)

class ActivityViewSet(ViewSet):
    def list(self, request):
        activities = Activity.objects.all()
        data = [{"user": activity.user.username, "activity_type": activity.activity_type, "duration": activity.duration} for activity in activities]
        return Response(data)

class LeaderboardViewSet(ViewSet):
    def list(self, request):
        leaderboard = Leaderboard.objects.all()
        data = [{"user": entry.user.username, "score": entry.score} for entry in leaderboard]
        return Response(data)

class WorkoutViewSet(ViewSet):
    def list(self, request):
        workouts = Workout.objects.all()
        data = [{"name": workout.name, "description": workout.description} for workout in workouts]
        return Response(data)
