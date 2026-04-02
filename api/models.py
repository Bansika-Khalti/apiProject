import django.db

class Blog(django.db.models.Model):
    title = django.db.models.CharField(max_length=200)
    content = django.db.models.TextField()

    # Fixed the double underscores and the space
    def __str__(self):
        return self.title