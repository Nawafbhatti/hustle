from django.db import models
from django.db.models import Count
from django_extensions.db.fields import AutoSlugField

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
    
    use_in_home_page = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Event Items Counter"

class Event(models.Model):
    
    sponsors = models.ManyToManyField(Sponsor, related_name="sponsor")
    speakers = models.ManyToManyField(Speaker, related_name="speaker")
    
    main_image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True, null=True, blank=True, max_length=256)
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
    
    def get_sponsors_by_category(self):
        
        sponsors = self.sponsors.values('sponsor_type__name','id', 'name', 'image', 'text')
        sponsors = sponsors.annotate(category_count=Count('sponsor_type'))
        sponsor_data = {}
        
        for sponsor in sponsors:
            category_name = sponsor['sponsor_type__name']
            sponsor_data.setdefault(category_name, []).append({
                'id': sponsor['id'],
                'name': sponsor['name'],
                'image': sponsor['image'],
                'text': sponsor['text']
                })
            
        return sponsor_data
    
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
    

class EventRegisterForm(models.Model):
    
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    number_of_persons = models.IntegerField(null=True, blank=True)
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.email
    
class PAYMENT(models.Model):
    
    options = (
    ("Created", "Created"),
    ("Completed", "Completed"),
    ("Purchased", "Purchased"),
    ("Cancel", "Cancel"),
    )

    eventregister = models.ForeignKey(EventRegisterForm, on_delete=models.CASCADE, null=True, blank=True)
    
    total_price = models.CharField(max_length=255)
    session_id = models.TextField()
    stripe_payment_intent = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=options)

    def __str__(self):
        return self.stripe_payment_intent
    