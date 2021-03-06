# Generated by Django 3.0.7 on 2021-04-11 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sightings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latitude', models.FloatField(blank=True, help_text='Sighting Latitude: ')),
                ('Longitude', models.FloatField(blank=True, help_text='Sighting Longitude')),
                ('UniqueSquirrelID', models.CharField(blank=True, help_text='Squirrel ID', max_length=100)),
                ('Shift', models.CharField(blank=True, choices=[('AM', 'AM'), ('PM', 'PM')], help_text='Sighting Shift', max_length=2)),
                ('Date', models.DateField(blank=True, help_text='Sighting Date')),
                ('Age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], help_text="Squirrel's age", max_length=20)),
                ('Primary_Fur_Color', models.CharField(blank=True, choices=[('Black', 'Black'), ('Gray', 'Gray'), ('Cinnamon', 'Cinnamon')], help_text='Primary Fur Color', max_length=20)),
                ('Location', models.CharField(blank=True, choices=[('Above Ground', 'Above Ground'), ('Ground Plane', 'Ground Plane')], help_text='Sighting Location', max_length=20)),
                ('SpecificLocation', models.CharField(blank=True, help_text='Sighting Specific Location', max_length=100)),
                ('OtherActivities', models.CharField(blank=True, help_text='Other Activities', max_length=100)),
                ('Running', models.CharField(blank=True, choices=[('true', 'true'), ('false', 'false')], help_text='Is the squirrel running?', max_length=20)),
                ('Chasing', models.CharField(blank=True, choices=[('true', 'true'), ('false', 'false')], help_text='Is the squirrel chasing another squirrel?', max_length=20)),
                ('Climbing', models.CharField(blank=True, choices=[('true', 'true'), ('false', 'false')], help_text='Is the squirrel climbing?', max_length=5)),
                ('Eating', models.CharField(blank=True, choices=[('true', 'true'), ('false', 'false')], help_text='Is the squirrel eating?', max_length=5)),
                ('Foraging', models.CharField(blank=True, choices=[('true', 'true'), ('false', 'false')], help_text='Is the squirrel foraging?', max_length=5)),
                ('Kuks', models.CharField(blank=True, choices=[('true', 'true'), ('false', 'false')], help_text='Did the squirrel kuk?', max_length=5)),
                ('Quaas', models.CharField(blank=True, choices=[('true', 'true'), ('false', 'false')], help_text='Did the squirrel quaa?', max_length=5)),
                ('Moans', models.CharField(blank=True, choices=[('true', 'true'), ('false', 'false')], help_text='Did the squirrel moan?', max_length=5)),
                ('TailFlags', models.CharField(blank=True, choices=[('true', 'true'), ('false', 'false')], help_text='Did its tail flag?', max_length=5)),
                ('TailTwitches', models.CharField(blank=True, choices=[('true', 'true'), ('false', 'false')], help_text='Did its tail twitch?', max_length=5)),
                ('Approaches', models.CharField(blank=True, choices=[('true', 'true'), ('false', 'false')], help_text='Did it approach you?', max_length=5)),
                ('Indifferent', models.CharField(blank=True, choices=[('true', 'true'), ('false', 'false')], help_text='Was it indifferent towards you?', max_length=5)),
                ('RunsFrom', models.CharField(blank=True, choices=[('true', 'true'), ('false', 'false')], help_text='Did it run from you?', max_length=5)),
            ],
        ),
    ]
