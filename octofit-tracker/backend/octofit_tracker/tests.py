from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='test123', team=team)
        self.assertEqual(user.email, 'test@example.com')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='test123', team=team)
        activity = Activity.objects.create(user=user, type='Run', duration=30, calories=300)
        self.assertEqual(activity.type, 'Run')

    def test_workout_creation(self):
        team = Team.objects.create(name='Test Team')
        workout = Workout.objects.create(name='Morning Cardio', description='Cardio', suggested_for_team=team)
        self.assertEqual(workout.name, 'Morning Cardio')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='test123', team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)
