from django.db import models
import random
import string


def generate_category_id():
    id = ''.join(random.sample(string.lowercase + string.digits, 32))
    if not Component.objects.filter(pk=id).exists():
        return 'category-' + id


def generate_component_id():
    id = ''.join(random.sample(string.lowercase + string.digits, 32))
    if not Component.objects.filter(pk=id).exists():
        return 'component-' + id


class Category(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=generate_category_id, editable=False)
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)

    class Meta:
        db_table = 'categories'

    def __unicode__(self):
        return u"%s" % self.name


class Component(models.Model):
    STATE_NEW = 'new'
    STATE_OLD = 'old'
    STATE_CHOICES = (
        (STATE_NEW, 'new'),
        (STATE_OLD, 'old'),
    )
    id = models.CharField(max_length=64, primary_key=True, default=generate_component_id, editable=False)
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    state = models.CharField(max_length=3, choices=STATE_CHOICES, default=STATE_NEW, null=False, blank=False)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'components'

    def __unicode__(self):
        return u"%s [%s]" % (self.name, self.state)
