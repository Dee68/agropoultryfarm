from django.db import models
from django.core.mail import send_mail

# Create your models here.
class Setting(models.Model):
    """"settings of the site"""
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=100)
    address = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=20)
    fax = models.CharField(blank=True, max_length=20)
    email = models.EmailField(blank=True, max_length=50)
    icon = models.ImageField(blank=True, upload_to='icons/')
    facebook = models.CharField(blank=True, max_length=20)
    instagram = models.CharField(blank=True, max_length=20)
    twitter = models.CharField(blank=True, max_length=20)
    smtpserver = models.CharField(blank=True, max_length=20)
    smtpemail = models.CharField(blank=True, max_length=20)
    smtppassword = models.CharField(blank=True, max_length=20)
    smtpport = models.CharField(blank=True, max_length=20)
    aboutus = models.TextField()
    contact = models.TextField()
    #references = models.TextField()
    status = models.CharField(max_length=5, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class SubscribedUser(models.Model):
    """subscribed user of the site"""
    email = models.EmailField(max_length=50, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.email

class ContactMessage(models.Model):
    """contact message model of contact form"""
    STATUS = (
        ('New','New'),
        ('Closed','Closed'),
        ('Read','Read'),
        )
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=255)
    ip = models.CharField(blank=True, max_length=50)
    note = models.CharField(blank=True, max_length=50)
    status = models.CharField(max_length=6, choices=STATUS, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name+" - message"
        
# message from admin to subscribers
class MailMessage(models.Model):
    """mail message model of subscribers"""
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField()
    attachement = models.FileField(blank=True, null=True)
    subscribers = models.ManyToManyField(SubscribedUser)
    send_it = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self):
        if self.send_it:
            # create/get list of subscribers
            subscribers_list = []
            for subscriber in self.subscribers:
                subscribers_list.append(subscriber.email)
            # then send message
            send_mail(
                str(self.subject),
                str(self.message),
                subscribers_list,
                fail_silently=False
            )

    def __str__(self):
        return self.subject

