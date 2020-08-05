from django.db import models

class Question(models.Model):
    QUESTION_TYPES = (
     ('Math problem','Math problem'),
     ('Computer program','Computer program'),
     ('English', 'English'),
     ('Science', 'Science')
     )

    type = models.CharField('Question type',max_length=20, choices=QUESTION_TYPES, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    image= models.ImageField(upload_to='', blank=True)
    email= models.EmailField('Email Address', max_length=50, blank=False, null=False)

    def __str__(self):
        return self.text
