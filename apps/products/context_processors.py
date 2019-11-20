from apps.products.models import Magazine
from django.conf import settings # import the settings file


def latest_magazine(request):
    # Create fixed data structures to pass to template
    # data could equally come from database queries
    # web services or social APIs
    latest_magazine = Magazine.objects.last()
    return {'latest_magazine': latest_magazine}


def ga_tracking_id(request):
	return {'ga_tracking_id' : settings.BIEN_GA_TRACKING_ID }