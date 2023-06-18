# Generated by Django 3.2 on 2023-06-18 16:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='身份标识'),
        ),
    ]
