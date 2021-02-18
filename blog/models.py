from django.db import models

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key= True)
    tilte = models.CharField(max_length=50)
    head0 = models.CharField(max_length=500, default="")
    chead0 = models.TextField(max_length=50000, default="")
    head1 = models.CharField(max_length=500, default="")
    chead1 = models.TextField(max_length=50000, default="")
    head2 = models.CharField(max_length=500, default="")
    chead2 = models.TextField(max_length=50000, default="")
    head3 = models.CharField(max_length=500, default="")
    chead3 = models.TextField(max_length=50000, default="")
    head4= models.CharField(max_length=500, default="")
    chead4 = models.TextField(max_length=50000, default="")
    head5 = models.CharField(max_length=500, default="")
    chead5 = models.TextField(max_length=50000, default="")
    pub_date = models.DateField()
    auth=models.CharField(max_length=20,default="")
    thumbnail = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.tilte


class Contact(models.Model):
    email=models.CharField(max_length=122)
    name=models.CharField(max_length=122)
    desc=models.TextField(max_length=122)
    date= models.DateField()

    def __str__(self):
        return self.name
         