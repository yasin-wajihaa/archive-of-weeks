from django.db import models
from courses.models import Course, SyllabusItem
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Progress(models.Model):
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    week = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])

    lecs_done = models.IntegerField(validators=[MinValueValidator(0)])
    AQs_done = models.IntegerField(validators=[MinValueValidator(0)])
    PAs_done = models.IntegerField(validators=[MinValueValidator(0)])
    GAs_done = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f'W{self.week:02}-{self.course}'
    
    def clean(self):
        o = SyllabusItem.objects.get(course=self.course, week=self.week)
        if (self.AQs_done > o.AQs) or (self.PAs_done > o.PAs) or (self.GAs_done > o.GAs) or (self.lecs_done > o.lectures) :
            raise ValidationError (
                'Ehhhh!?'
            )
        