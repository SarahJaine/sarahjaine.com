from django.db import models
from django.template.defaultfilters import slugify


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(unique=True, db_index=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Tag, self).save(**kwargs)


class Project(models.Model):
	name = models.CharField(max_length=30, unique=True)
	subtitle = models.CharField(max_length=50, unique=False)
	teaser = models.CharField(max_length=500, unique=True)
	description = models.TextField(blank=True, max_length=2000, unique=False)
	slug = models.SlugField(db_index=True, unique=True)
	order = models.IntegerField(default=0)
	featured = models.BooleanField(default=True)
	git_url = models.URLField(blank=True, unique=False)
	hosted_url = models.URLField(blank=True, unique=False)
	image = models.ImageField(blank=True, null=True, upload_to='project-images/')
	image_detail = models.ImageField(blank=True, null=True, upload_to='project-images/')
	video = models.FileField(blank=True, null=True, upload_to='project-videos/')
	tags = models.ManyToManyField(Tag, blank=True)

	class Meta:
		ordering = ["name"]

	def __str__(self):
		return self.name

	def save(self, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super(Project, self).save(**kwargs)
