# Generated by Django 3.0.4 on 2020-03-10 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cd_library', '0006_auto_20200310_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contentcategoryid',
            old_name='albumID',
            new_name='album',
        ),
        migrations.RenameField(
            model_name='contentcategoryid',
            old_name='categoryID',
            new_name='category',
        ),
    ]
