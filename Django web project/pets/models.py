from django.db import models


class Pet(models.Model):
    DOG = 'dog'
    CAT = 'cat'
    PARROT = 'parrot'
    UNKNOWN = 'unknown'
    PET_TYPE = (
        (DOG, 'dog'),
        (CAT, 'cat'),
        (PARROT, 'parrot'),
        (UNKNOWN, 'unknown')
    )

    type = models.CharField(max_length=10, choices=PET_TYPE, default=UNKNOWN)
    name = models.CharField(max_length=6, blank=False)
    age = models.IntegerField(blank=False)
    description = models.TextField(blank=False)
    image_url = models.URLField()
    likes = ''

    def __str__(self):
        return f'id:{self.id}, name: {self.name}, age: {self.age}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    test = models.CharField(max_length=2)


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    text = models.TextField(blank=False)