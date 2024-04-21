from django.db import models
import os



"""Serverda rasmlar saqlanib qolmasligi kerak keyinroq qo'shib ketaman"""

class Corousel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='carousel')
    status = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(default="#")

    class Meta:
        verbose_name_plural = "Corousel ma'lumotlari"
        verbose_name = "Corousel"

    def file_delete(self):
        if self.image:
            if os.path.exists(self.image.path):
                os.remove(self.image.path)


    def delete(self, *args, **kwargs):
        self.file_delete()
        return super().delete(*args, **kwargs)

    def __str__(self):
        return self.title


"""Qadamjo ma'lumotlari"""
class Qadamjo(models.Model):
    title = models.CharField(max_length=255)
    short_title = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='places')
    status = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True, default="Judayam chiroyli joylar")

    class Meta:
        verbose_name_plural = "Qadamjo ma'lumotlari"
        verbose_name = "Qadamjo"

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.exists(self.image.path):
                os.remove(self.image.path)
        return super().delete(*args, **kwargs)


    def __str__(self):
        return self.title

class FotoPlus(models.Model):
    pleace = models.ForeignKey(Qadamjo, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='places_photos')

    class Meta:
        verbose_name_plural = "Qadamjo rasmlari"
        verbose_name = "rasm"

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.exists(self.image.path):
                os.remove(self.image.path)
        return super().delete(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if self.pk: 
            old_instance = FotoPlus.objects.get(pk=self.pk)
            if old_instance.image != self.image:
                if os.path.exists(old_instance.image.path):
                    os.remove(old_instance.image.path)

        super().save(*args, **kwargs)


    def __str__(self):
        return self.pleace.title
    

"""Umumiy ma'lumotlari"""
class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='about')
    status = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True, default="Umumiy ma'lumotlar")

    class Meta:
        verbose_name_plural = "Umumiy ma'lumotlari"
        verbose_name = "Umumiy ma'lumot"
    
    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.exists(self.image.path):
                os.remove(self.image.path)
        return super().delete(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if self.pk: 
            old_instance = AboutUs.objects.get(pk=self.pk)
            if old_instance.image != self.image:
                if os.path.exists(old_instance.image.path):
                    os.remove(old_instance.image.path)

        super().save(*args, **kwargs)


    def __str__(self):
        return self.title



"""Umumiy rasmlari"""
class AboutImages(models.Model):
    about = models.ForeignKey(AboutUs, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='about_us')

    class Meta:
        verbose_name_plural = "Umumiy rasmlari"
        verbose_name = "rasm"
    
    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.exists(self.image.path):
                os.remove(self.image.path)
        return super().delete(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if self.pk: 
            old_instance = AboutImages.objects.get(pk=self.pk)
            if old_instance.image != self.image:
                if os.path.exists(old_instance.image.path):
                    os.remove(old_instance.image.path)

        super().save(*args, **kwargs)


    def __str__(self):
        return self.about.title
