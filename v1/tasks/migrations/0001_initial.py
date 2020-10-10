# Generated by Django 3.1.1 on 2020-10-10 20:48

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('repository', models.CharField(max_length=250)),
                ('completed_date', models.DateTimeField(null=True)),
                ('amount', models.PositiveIntegerField()),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.contributor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]