from .models import Service  # або як у вас називається модель послуги

def all_services(request):
    services = Service.objects.all()
    return {'all_services': services}
