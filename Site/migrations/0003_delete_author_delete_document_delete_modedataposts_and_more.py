# Generated by Django 4.1.4 on 2023-03-06 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0002_remove_picture_tags_delete_tags'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='ModeDataPosts',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]
