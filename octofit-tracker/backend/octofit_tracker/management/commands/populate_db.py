from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from mongoengine import connect
from mongoengine.connection import get_db
from datetime import timedelta

def format_timedelta(td):
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}:{minutes:02}:{seconds:02}"

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB using mongoengine
        connect(db="octofit_db", host="localhost", port=27017)

        # Clear existing collections
        db = get_db()
        db.user.drop()
        db.team.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workout.drop()

        # Create users
        users = [
            User(username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword').save(),
            User(username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword').save(),
            User(username='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword').save(),
            User(username='crashoverride', email='crashoverride@hmhigh.edu', password='crashoverridepassword').save(),
            User(username='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword').save(),
        ]

        # Create teams
        team1 = Team(name='Blue Team').save()
        team2 = Team(name='Gold Team').save()
        team1.members.extend(users[:3])
        team1.save()
        team2.members.extend(users[3:])
        team2.save()

        # Create activities
        activities = [
            Activity(user=users[0], activity_type='Cycling', duration=format_timedelta(timedelta(hours=1))).save(),
            Activity(user=users[1], activity_type='Crossfit', duration=format_timedelta(timedelta(hours=2))).save(),
            Activity(user=users[2], activity_type='Running', duration=format_timedelta(timedelta(hours=1, minutes=30))).save(),
            Activity(user=users[3], activity_type='Strength', duration=format_timedelta(timedelta(minutes=30))).save(),
            Activity(user=users[4], activity_type='Swimming', duration=format_timedelta(timedelta(hours=1, minutes=15))).save(),
        ]

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=users[0], score=100).save(),
            Leaderboard(user=users[1], score=90).save(),
            Leaderboard(user=users[2], score=95).save(),
            Leaderboard(user=users[3], score=85).save(),
            Leaderboard(user=users[4], score=80).save(),
        ]

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event').save(),
            Workout(name='Crossfit', description='Training for a crossfit competition').save(),
            Workout(name='Running Training', description='Training for a marathon').save(),
            Workout(name='Strength Training', description='Training for strength').save(),
            Workout(name='Swimming Training', description='Training for a swimming competition').save(),
        ]

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
