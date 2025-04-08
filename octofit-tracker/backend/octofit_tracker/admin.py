from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

# Create custom admin classes for MongoDB models
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_type', 'duration')
    search_fields = ('activity_type',)

class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('score',)
    search_fields = ('score',)

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

# Register models with custom admin classes
# Note: For MongoEngine models, direct registration may require additional configuration
# These are placeholder registrations that would work with Django ORM models
try:
    admin.site.register(User, UserAdmin)
    admin.site.register(Team, TeamAdmin)
    admin.site.register(Activity, ActivityAdmin)
    admin.site.register(Leaderboard, LeaderboardAdmin)
    admin.site.register(Workout, WorkoutAdmin)
except:
    # For MongoEngine models, direct registration might raise exceptions
    # In a production app, you would use a proper MongoEngine admin integration
    pass
