from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Vehicle, Rental, Category
from datetime import datetime


def home(request):
    categories = Category.objects.all()
    return render(request, 'rental_app/home.html', {'categories': categories})

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'rental_app/vehicle_list.html', {'vehicles': vehicles})

def vehicle_list_filtered(request, slug):
    category = get_object_or_404(Category, slug=slug)
    vehicles = Vehicle.objects.filter(category=category)
    return render(request, 'rental_app/vehicle_list.html', {
        'vehicles': vehicles,
        'vehicle_type': category.name,
    })

def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'rental_app/vehicle_detail.html', {'vehicle': vehicle})

def rent_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    # Optional: redirect directly to checkout with vehicle_id param
    return redirect('checkout') + f'?vehicle_id={vehicle.id}'

def checkout(request):
    vehicle_id = request.GET.get('vehicle_id')
    if not vehicle_id:
        return redirect('home')

    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)

    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        payment_method = request.POST.get('payment_method')

        if not start_date or not end_date or not payment_method:
            return render(request, 'rental_app/checkout.html', {
                'vehicle': vehicle,
                'error_message': "All fields are required."
            })

        try:
            start = datetime.strptime(start_date, '%Y-%m-%d').date()
            end = datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'rental_app/checkout.html', {
                'vehicle': vehicle,
                'error_message': "Invalid date format."
            })

        rental_days = (end - start).days + 1
        if rental_days <= 0:
            return render(request, 'rental_app/checkout.html', {
                'vehicle': vehicle,
                'error_message': "End date must be after start date."
            })

        subtotal = float(vehicle.daily_rate) * rental_days
        taxes = round(subtotal * 0.1, 2)
        total_price = round(subtotal + taxes, 2)

        Rental.objects.create(
            vehicle=vehicle,
            start_date=start,
            end_date=end,
            payment_method=payment_method,
            total_price=total_price
        )

        request.session['rental_data'] = {
            'vehicle_id': vehicle.id,
            'start_date': start_date,
            'end_date': end_date,
            'payment_method': payment_method,
            'subtotal': round(subtotal, 2),
            'taxes': taxes,
            'total_price': total_price,
        }

        return redirect('confirm-rental')

    return render(request, 'rental_app/checkout.html', {'vehicle': vehicle})

def confirm_rental(request):
    rental_data = request.session.get('rental_data')
    if not rental_data:
        return redirect('home')

    vehicle = get_object_or_404(Vehicle, pk=rental_data['vehicle_id'])

    # Clear session rental data after displaying confirmation
    del request.session['rental_data']

    return render(request, 'rental_app/confirm_rental.html', {
        'vehicle': vehicle,
        'rental_data': rental_data
    })

def about(request):
    return render(request, 'rental_app/about.html')

def contact(request):
    return render(request, 'rental_app/contact.html')
