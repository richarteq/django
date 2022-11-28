from django.db import models

# Create your models here.

class Menu(models.Model):    
    UBICATION = [
        ('main_menu', 'Main Menu'),
        ('left_sidebar', 'Let Sidebar'),
        ('right_sidebar', 'Right Sidebar'),
        ('tree_menu', 'Tree Menu'),
        ('up_menu', 'Up Menu'),
        ('bottom_menu', 'Bottom Menu'),
    ]
    ubication = models.CharField(null=False, choices=UBICATION, default='main_menu', max_length=20)       
    label = models.CharField(null=False, blank=False, max_length=20)    
    weight = models.IntegerField(null=True, blank=True, default=0)    
    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    father = models.OneToOneField('self', on_delete=models.CASCADE, related_name="father_menu", blank=True, null=True)

    class Meta:
        ordering = ['ubication', 'label', 'weight', 'status']

    def save(self, *args, **kwargs):
        self.label = self.label.upper()
        return super(Menu, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s %s" % (self.ubication, self.label, self.weight, self.status)
