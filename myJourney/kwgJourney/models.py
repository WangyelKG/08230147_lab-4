from django.db import models

# Model for your learning journey entries
class LearningJourney(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


# Model for about me details
class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    hobbies = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name
