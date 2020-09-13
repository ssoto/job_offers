from django.db import models


TECHNOLOGIES_AREAS = (
    ('DV', 'DevOps'),
    ('SYS', 'Systems'),
    ('D', 'Develop'),
    ('DB', 'Database'),
    ('T', 'Testing'),
)


class Technology(models.Model):

    name = models.CharField(max_length=200,
                            unique=True)
    technology_type = models.CharField(max_length=3, choices=TECHNOLOGIES_AREAS)

