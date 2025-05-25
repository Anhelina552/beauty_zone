from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Service, GalleryImage

def home(request):
    popular_services = Service.objects.all()[:3]  # твоя логіка

    values = [
      {'icon_path': 'M12 2L2 7l10 5 10-5-10-5zm0 13l-10-5v6l10 5 10-5v-6l-10 5z', 'title': 'Професіоналізм', 'desc': 'Кваліфіковані косметологи з великим досвідом.'},
      {'icon_path': 'M12 4a8 8 0 1 0 0 16 8 8 0 0 0 0-16z', 'title': 'Індивідуальний підхід', 'desc': 'Персональні консультації і догляд за кожним клієнтом.'},
      {'icon_path': 'M20 6h-4V2H8v4H4v16h16V6z', 'title': 'Сучасне обладнання', 'desc': 'Інноваційні технології для найкращих результатів.'}
    ]

    context = {
      'popular_services': popular_services,
      'values': values,
    }
    return render(request, 'main/home.html', context)


def services(request):
    all_services = Service.objects.all()
    return render(request, 'main/services.html', {'services': all_services})

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'main/gallery.html', {'images': images})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'main/service_detail.html'  # створимо цей шаблон
    context_object_name = 'service'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
