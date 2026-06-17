from django.shortcuts import render, get_object_or_404
from .models import Vehicle, Enquiry


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def vehicles(request):
    query = request.GET.get('q')

    vehicles = Vehicle.objects.filter(status='available')

    if query:
        vehicles = vehicles.filter(title__icontains=query)

    return render(request, 'vehicles.html', {
        'vehicles': vehicles,
        'query': query
    })


def vehicle_detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)

    if request.method == 'POST':
        Enquiry.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message'),
            vehicle=vehicle
        )

    return render(request, 'vehicle_detail.html', {
        'vehicle': vehicle
    })

    return render(request, 'vehicle_detail.html', {
        'vehicle': vehicle
    })


def parts(request):
    return render(request, 'parts.html')

def sold_vehicles(request):
    vehicles = Vehicle.objects.filter(status='sold')
    return render(request, 'sold_vehicles.html', {'vehicles': vehicles})