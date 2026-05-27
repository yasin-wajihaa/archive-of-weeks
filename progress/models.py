from django.db import models
from courses.models import Course, SyllabusItem
from django.core.validators import MinValueValidator, MaxValueValidator


class Progress(models.Model):
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    week = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])

    lecs_done = models.IntegerField(validators=[MinValueValidator(0)])
    AQs_done = models.IntegerField(validators=[MinValueValidator(0)])
    PAs_done = models.IntegerField(validators=[MinValueValidator(0)])
    GAs_done = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f'W{self.week:02}-{self.course}'