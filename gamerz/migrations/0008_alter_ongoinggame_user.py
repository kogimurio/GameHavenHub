# Generated by Django 4.2.10 on 2024-08-29 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamerz', '0007_alter_achievement_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ongoinggame',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerz.client'),
        ),
    ]
