from django.db import models
from django.contrib.auth.models import User


class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    puzzle = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user}: {self.date}'


class Solve(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    time = models.DecimalField(decimal_places=3, max_digits=7)

    def __str__(self):
        return f'{self.session.puzzle}: {self.time}'
