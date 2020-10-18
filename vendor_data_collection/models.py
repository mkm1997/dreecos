import sys
from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

from django.db import models

VENDOR_TYPE_CHOICES=(
    ('ice-cream','Ice Cream Vendor'),
    ('vegetables','Vegetable/Fruits Vendor'),
    ('street-food','Street Food Vendor'),
    ('drinks','Drinks')
)

AVAILABILITY_CHOICES=(
    ('year','Yearly'),
    ('season','Seasonally')
)


# Create your models here.
class Vendor(models.Model):
    id_field = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    availability=models.CharField(max_length=20,choices=AVAILABILITY_CHOICES,default='year')
    paytm_available=models.BooleanField(default=False)
    vendor_type=models.CharField(max_length=20,choices=VENDOR_TYPE_CHOICES,default='street-food')
    hygeine_rating=models.CharField(max_length=1)
    taste_rating=models.CharField(max_length=1)
    
    def __str__(self):
        return str(self.id_field)


class Submitters(models.Model):
    id_field = models.AutoField(primary_key=True)
    submitter=models.CharField(max_length=6)
    vendor_id=models.ForeignKey(Vendor,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_field)

class GeoLocation(models.Model):
    id_field = models.AutoField(primary_key=True)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    lat=models.CharField(max_length=30)
    long=models.CharField(max_length=30)
    pin=models.CharField(max_length=7)
    start=models.CharField(max_length=10)
    end=models.CharField(max_length=10)

    def __str__(self):
        return str(self.id_field)

class Menu(models.Model):
    id_field = models.AutoField(primary_key=True)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category=models.CharField(max_length=30)
    item=models.CharField(max_length=30)
    price=models.CharField(max_length=6)

    def __str__(self):
        return str(self.id_field)

class VendorImage(models.Model):
    vendor_id = models.OneToOneField(Vendor,on_delete=models.CASCADE,primary_key=True)
    image=models.ImageField()

    def save(self,*args,**kwargs):
        # Opening the uploaded image
        im = Image.open(self.image)

        output = BytesIO()

        # Resize/modify the image
        # im = im.resize((100, 100))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=70)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)

        super(VendorImage, self).save(*args,**kwargs)

    def __str__(self):
        return str(self.vendor_id)