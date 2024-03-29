# Generated by Django 2.2.7 on 2019-11-16 15:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sn_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('domain', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(0, 'disabled'), (1, 'active'), (2, 'inactive'), (3, 'maintenance')], db_index=True, default=1)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sites', to='sn_auth.Profile')),
            ],
        ),
    ]
