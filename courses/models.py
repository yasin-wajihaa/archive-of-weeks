from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from terms.models import Term


course_choices = {
    # Programming Diploma
    'DBMS': 'Database Management Systems',
    'PDSA': 'Programming, Data Structures and Algorithms using Python',
    'MAD-1': 'Modern Application Development I',
    'JAVA': 'Programming Concepts using Java',
    'MAD-2': 'Modern Application Development II',
    'SC': 'System Commands',

    # Data Science Diploma
    'MLF': 'Machine Learning Foundations',
    'BDM': 'Business Data Management',
    'MLT': 'Machine Learning Techniques',
    'MLP': 'Machine Learning Practice',
    'TDS': 'Tools in Data Science',

    # Option 1
    'BA': 'Business Analytics',

    # Option 2
    'DLGA': 'Introduction to Deep Learning and Generative AI',
}

project_choices = {
    'MAD-1P': 'Modern Application Development I - Project',
    'MAD-2P': 'Modern Application Development II - Project',

    'MLPP': 'Machine Learning Practice - Project',

    'BDMP': 'Business Data Management - Project',

    'DLGAP': 'Deep Learning and Generative AI - Project',
}

class Course(models.Model):
    term = models.ForeignKey(Term, on_delete = models.CASCADE)

    name = models.CharField(max_length = 5, choices = course_choices)

    def __str__(self):
        return f'{self.term}-{self.name}'

class Project(models.Model):
    term = models.ForeignKey(Term, on_delete = models.CASCADE)

    name = models.CharField(max_length = 6, choices = project_choices)

    def __str__(self):
        return f'{self.name}-{self.term}'


class SyllabusItem(models.Model):
    course = models.ForeignKey(Course, on_delete = models.CASCADE)

    week = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])

    lectures = models.IntegerField(validators=[MinValueValidator(0)])
    AQs = models.IntegerField(validators=[MinValueValidator(0)])
    PAs = models.IntegerField(validators=[MinValueValidator(0)])
    GAs = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f'W{self.week:02}-{self.course}'