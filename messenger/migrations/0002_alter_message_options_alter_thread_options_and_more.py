# Generated by Django 4.0.4 on 2022-06-23 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['created']},
        ),
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['-updated']},
        ),
        migrations.RemoveField(
            model_name='message',
            name='thread',
        ),
        migrations.AddField(
            model_name='thread',
            name='messages',
            field=models.ManyToManyField(to='messenger.message'),
        ),
        migrations.AddField(
            model_name='thread',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
