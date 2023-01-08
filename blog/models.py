from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)  # we could use CharField, but we have EmailField

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)  # automatically set whenever we save our database model
    slug = models.SlugField(unique=True)  # will need to be unique, db_index is automatically set to True
    # so we don't need to put it in parameters, also - if unique=True, db_index does too
    content = models.TextField(validators=[MinLengthValidator(10)])  # CharField is for shorter texts
    # for text we don't need to set a max length
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")  # one-to-many
    # once the author is deleted, the author info for his posts will be set to null
    tags = models.ManyToManyField(Tag)  # many-to-many

    def __str__(self):
        return f"{self.title} by {self.author}"
