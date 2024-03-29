# Generated by Django 4.1 on 2022-10-08 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('coffee_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, unique=True)),
                ('flavour_1', models.CharField(max_length=30)),
                ('flavour_2', models.CharField(max_length=30)),
                ('flavour_3', models.CharField(max_length=30)),
                ('flavour_4', models.CharField(blank=True, max_length=30)),
                ('flavour_5', models.CharField(blank=True, max_length=30)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('my_image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default='Państwo', max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='Jasno palona', max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roastery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Palarnia', max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user', models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UsersCoffees',
            fields=[
                ('uc_id', models.AutoField(default='1', primary_key=True, serialize=False)),
                ('coffee_id', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='coffee_app.coffee')),
                ('user', models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='coffee_app.users')),
            ],
        ),
        migrations.AddField(
            model_name='coffee',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='coffee_app.origin'),
        ),
        migrations.AddField(
            model_name='coffee',
            name='roast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='coffee_app.roast'),
        ),
        migrations.AddField(
            model_name='coffee',
            name='roastery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='coffee_app.roastery'),
        ),
    ]
