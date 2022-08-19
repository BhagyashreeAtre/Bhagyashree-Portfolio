from django.db import models

# Create your models here.
#Projects table will store details of myprojects which I need to show in database
#It will have Project title,Project screen Image,Summary about project,Start date of project,end date of project
#Since we are working with image field we need to install pillow
class Projects(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/')
    summary=models.CharField(max_length=350)
    start_date= models.DateField()
    end_date= models.DateField()

    def __str__(self) :
        return self.title
    
