from django.db import models

# Create your models here.
class Music(models.Model):
    #define table(with default value)
    ranking = models.TextField(default="Unknown")
    song = models.TextField(default="Unknown")
    singer = models.TextField(default="Unknown")
    release_date = models.TextField(default="Unknown")
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    name = models.TextField(null=True, blank=True)
 
    class Meta:
        db_table = "music" #table's name in the database
        get_latest_by="created"

    def display_type_name(self):
        return self.get_type_display()

