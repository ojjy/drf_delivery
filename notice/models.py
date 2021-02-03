from django.db import models
from django.utils.timezone import now
from django.template.defaultfilters import slugify

# Create your models here.
# 공지사항 관련된 APP

class Notice(models.Model):
    title = models.CharField(max_length=256)
    pub_date = models.DateTimeField(default=now)
    update_date = models.DateTimeField(default=now)
    content = models.TextField()

    def __str__(self):
        return self.title

def get_image_filename(instance, filename):
    title = instance.notice.title
    slug = slugify(title)
    return "notice_images/%s-%s"%(slug, filename)

class Image(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE, null=True)
    img = models.ImageField(upload_to=get_image_filename, blank=True)
