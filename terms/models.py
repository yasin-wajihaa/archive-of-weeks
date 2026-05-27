from django.db import models
from datetime import date
from django.core.exceptions import ValidationError

def current_yr():
    return str(date.today().year)[2:]

term_code_choices = {
    'F1': 'first_term',
    'F2': 'second_term',
    'F3': 'third_term'
}

class Term(models.Model):

    start_date = models.DateField()
    end_date = models.DateField()

    yr = models.CharField(max_length=2, default=current_yr)  
    code = models.CharField(max_length=2, choices = term_code_choices)

    def __str__(self):
        return f'{self.yr}{self.code}'
    
    class Meta:
        unique_together = [
            ['yr', 'code']
        ]

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError (
                'End date of the term can not be earlier than the start date.'
            )