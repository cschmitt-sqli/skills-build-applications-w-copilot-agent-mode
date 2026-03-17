from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Lösche alle bestehenden Daten
        User = get_user_model()
        User.objects.filter(pk__isnull=False).delete()
        octo_models.Team.objects.filter(pk__isnull=False).delete()
        octo_models.Activity.objects.filter(pk__isnull=False).delete()
        octo_models.Leaderboard.objects.filter(pk__isnull=False).delete()
        octo_models.Workout.objects.filter(pk__isnull=False).delete()

        # Teams

        marvel = octo_models.Team.objects.create(name='Marvel')
        dc = octo_models.Team.objects.create(name='DC')

        # Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='test123', team_name='Marvel')
        captain = User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='test123', team_name='Marvel')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='test123', team_name='DC')
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='test123', team_name='DC')

        # Activities
        octo_models.Activity.objects.create(username='ironman', type='Run', duration=30, calories=300)
        octo_models.Activity.objects.create(username='batman', type='Swim', duration=45, calories=400)

        # Workouts
        octo_models.Workout.objects.create(name='Morning Cardio', description='Cardio für den Start in den Tag', suggested_for_team_name='Marvel')
        octo_models.Workout.objects.create(name='Strength Training', description='Krafttraining für DC', suggested_for_team_name='DC')

        # Leaderboard
        octo_models.Leaderboard.objects.create(username='ironman', points=100)
        octo_models.Leaderboard.objects.create(username='batman', points=120)

        self.stdout.write(self.style.SUCCESS('Testdaten erfolgreich in octofit_db eingefügt.'))
