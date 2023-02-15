from django.db import models


class Sponsor(models.Model):
    
    sponsor_type = models.ForeignKey("SponsorCategory", on_delete=models.CASCADE, null=True, blank=True)
    
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    text = models.TextField()
    
    def __str__(self):
        return self.name or f"sponsor object {self.id}"

class SponsorCategory(models.Model):
    
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Speaker(models.Model):
    
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    speaker_intro = models.TextField()

    def __str__(self):
        return self.name


class Items(models.Model):
    
    name = models.CharField(max_length=255)
    counter = models.IntegerField()
    
    event = models.ForeignKey("Event", related_name="event", on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.event.title}"
    

class Event(models.Model):
    
    sponsors = models.ManyToManyField(Sponsor, related_name="sponsor")
    speakers = models.ManyToManyField(Speaker, related_name="speaker")
    
    
    main_image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    event_date = models.DateTimeField()
    location_header = models.CharField(max_length=255)
    location_detail = models.CharField(max_length=255)
    description = models.TextField()
    secondimage = models.ImageField(upload_to='images/')
    event_register_text = models.TextField()
    event_price = models.IntegerField()
    
    def __str__(self):
        return self.title
    
class Gallery(models.Model):
    
    Image = models.ImageField(upload_to='images/')
    
    
class Contact(models.Model):
    
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    cell = models.CharField(max_length=255)
    message = models.TextField(null=True)
    
    def __str__(self):
        return self.full_name
    