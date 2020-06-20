from django.contrib.gis.db import models
import uuid

# Structure to support only one active map
class SingleActiveModel(models.Model):
    active = models.BooleanField(default=False)
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.active:
            # select all other active items
            qs = type(self).objects.filter(active=True)
            # except self (if self already exists)
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            # and deactive them
            qs.update(active=False)

        super(SingleActiveModel, self).save(*args, **kwargs)


# Used to save mapstyles
class MapStyle(SingleActiveModel):
    map_style = models.CharField(max_length=100, default='mapbox://styles/cfahlgren1/cjwhv3k951qzw1cs0q5ukvtxi')
    description = models.CharField(max_length=200)

    def has_add_permission(self, request):
        return False

    def __str__(self):
        return self.description

# Used to provide Mapbox API Key / Rotating
class MapAPIKey(SingleActiveModel):
    api_key = models.CharField(max_length=100)

    def __str__(self):
        return self.api_key


# Court model for db structure for basketball court
class Court(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4(), max_length=50, editable=True, unique=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=True)

    # Address Information
    house_number = models.CharField(max_length=10, blank=True)
    road = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=30, blank=False)
    state = models.CharField(max_length=30, blank=False)
    zip_code = models.CharField(max_length=10, blank=False)
    county = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=20, blank=False)
    location = models.PointField(blank=False, default=None)

    # Rating Information
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    court_logo = models.ImageField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + self.description

# MailChimp Email Signup Model
class Signup(models.Model):
    email = models.EmailField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email