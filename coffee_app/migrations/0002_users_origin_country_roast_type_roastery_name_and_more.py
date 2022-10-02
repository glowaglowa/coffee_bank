# Generated by Django 4.1.1 on 2022-09-30 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='origin',
            name='country',
            field=models.CharField(default='Państwo', max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='roast',
            name='type',
            field=models.CharField(default='Jasno palona', max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='roastery',
            name='name',
            field=models.CharField(default='Palarnia', max_length=15, unique=True),
        ),
        migrations.CreateModel(
            name='UsersCoffees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coffee_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='coffee_app.coffee')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='coffee_app.users')),
            ],
        ),
    ]