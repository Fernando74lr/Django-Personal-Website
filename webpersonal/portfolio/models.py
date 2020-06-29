from django.db import models

# This class will be represented as a table in the DB.
class Project(models.Model):
    # Every field represents a field in the table.
    title = models.CharField(max_length=100, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(verbose_name="Image", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")
    updated = models.DateTimeField(auto_now=True, verbose_name="Date of modification")

    # Metadata
    class Meta:
        # Single name.
        verbose_name = "proyect"
        # Plural name.
        verbose_name_plural = "proyects"
        # Order by field 'created'.
        # '-' means inverse order (show new first).
        ordering = ["-created"]
    
    # Return the title of the current project.
    def __str__(self):
        return self.title
        