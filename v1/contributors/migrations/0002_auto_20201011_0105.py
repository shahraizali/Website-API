# Generated by Django 3.1.1 on 2020-10-11 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='github_username',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='profile_image',
            field=models.FileField(blank=True, default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contributor',
            name='slack_username',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]