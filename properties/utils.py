# properties/utils.py
from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Returns all properties, cached in Redis for 1 hour (3600s).
    """
    properties = cache.get('all_properties')
    if properties is None:
        properties = list(Property.objects.all())
        cache.set('all_properties', properties, 3600)  # Cache for 1 hour
    return properties
