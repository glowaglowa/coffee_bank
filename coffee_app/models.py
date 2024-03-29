from django.contrib.auth.models import User
from django.db.models import CharField, Model, ForeignKey, TextField, DateTimeField, DO_NOTHING, \
    AutoField, ImageField, OneToOneField, CASCADE


class Roastery(Model):
    name = CharField(max_length=15, unique=True, default="Palarnia")

    def __str__(self):
        return self.name


class Origin(Model):
    country = CharField(max_length=20, unique=True, default='Państwo')

    def __str__(self):
        return self.country


class Roast(Model):
    type = CharField(max_length=20, unique=True, default='Jasno palona')

    def __str__(self):
        return self.type


class Coffee(Model):
    coffee_id = AutoField(primary_key=True)
    name = CharField(max_length=80, unique=True)
    roastery = ForeignKey(Roastery, on_delete=DO_NOTHING)
    origin = ForeignKey(Origin, on_delete=DO_NOTHING)
    roast = ForeignKey(Roast, on_delete=DO_NOTHING)
    flavour_1 = CharField(max_length=30)
    flavour_2 = CharField(max_length=30)
    flavour_3 = CharField(max_length=30)
    flavour_4 = CharField(max_length=30, blank=True)
    flavour_5 = CharField(max_length=30, blank=True)
    description = TextField(blank=True)
    created = DateTimeField(auto_now_add=True)
    my_image = ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.name


class Users(Model):
    user = OneToOneField(User, on_delete=CASCADE, primary_key=True, default="1")
    username = CharField(max_length=32,)
    password = CharField(max_length=32)

    def __str__(self):
        return self.username


class UsersCoffees(Model):
    uc_id = AutoField(primary_key=True, default="1")
    coffee_id = OneToOneField(Coffee, on_delete=DO_NOTHING)
    user = ForeignKey(Users, on_delete=DO_NOTHING, default="1")

