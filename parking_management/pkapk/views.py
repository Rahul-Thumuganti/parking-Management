from django.shortcuts import render, redirect
from .models import Category,add_vehicle
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from django.db.models import Count
from decimal import Decimal
from django.db.models import Sum

from django.contrib.auth import login, authenticate, logout



from .forms import categoryform, add_vehicleform

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
def showallservices(request):
    category = Category.objects.all()

    page_num = request.GET.get('page')  # creating total pages
    paginator = Paginator(category, 5)

    try:
        category = paginator.page(page_num)
    except PageNotAnInteger:
        category = paginator.page(1)
    except EmptyPage:
        category = paginator.page(paginator.num_pages)

    context = {
        'category':category
    }
    return render(request,'category.html',context)

def edit(request,pk):
    ecategory = Category.objects.get(id=pk)
    context = {
        'ecategory': ecategory
    }
    return render(request, 'empdetails.html', context)

def update(request, id):
    if request.method == 'POST':
        parking_area_no = request.POST.get('parking_area_no')
        vehicle_type = request.POST.get('vehicle_type')
        vehicle_limit = request.POST.get('vehicle_limit')
        parking_charge = request.POST.get('parking_charge')

        ecategory = Category(
            id=id,
            parking_area_no=parking_area_no,
            vehicle_type=vehicle_type,
            vehicle_limit=vehicle_limit,
            parking_charge=parking_charge,
        )
        ecategory.save()
        return redirect('showvehicle')

    return redirect(request, 'category.html')

def deletevehicle(request, pk):
    b = Category.objects.get(id=pk)   # storing records 1,2,3,4 in product
    b.delete()  # 1=> delete

    return redirect('showvehicle')

def addvehicle(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        parking_area_no = request.POST.get('parking_area_no')
        vehicle_type = request.POST.get('vehicle_type')
        vehicle_limit = request.POST.get('vehicle_limit')
        parking_charge = request.POST.get('parking_charge')

        emp = Category(
            parking_area_no=parking_area_no,
            vehicle_type=vehicle_type,
            vehicle_limit=vehicle_limit,
            parking_charge=parking_charge,
        )
        emp.save()
        return redirect('showvehicle')

    return render(request, 'category.html',{'categories': categories})

def activate_item(request, item_id):

    item = Category.objects.get(pk=item_id)
    item.status = True
    item.save()

    return redirect('showvehicle')

def deactivate_item(request, item_id):

    item = Category.objects.get(pk=item_id)
    item.status = False
    item.save()

    return redirect('showvehicle')

# manage vehicles=======================================================
def managevehicle(request):
    vehicle_entry_data = add_vehicle.objects.all()

    context = {
        'vehicle_entry_data': vehicle_entry_data,
    }
    return render(request, 'managevehicle.html', context)

def togglestatus(request, item_id):
    item = add_vehicle.objects.get(pk=item_id)
    item.status = not item.status  # Toggle the status
    item.save()
    return redirect('managevehicle')


# search===================================================================================
def search(request):
    vehicle_entry_data = add_vehicle.objects.all()

    context = {
        'vehicle_entry_data': vehicle_entry_data,
    }
    return render(request,'search.html',context)

# dashboard==============================================================================

def dashboard(request):
    dash = Category.objects.all()
    parked_count = add_vehicle.objects.filter(status=False).count()
    departed_count = add_vehicle.objects.filter(status=True).count()

    total_parked_charge = Decimal('0.00')
    parked_vehicles = add_vehicle.objects.filter(status=False)
    for vehicle in parked_vehicles:
        total_parked_charge += Decimal(vehicle.parking_charge)

    total_departed_charge = Decimal('0.00')
    departed_vehicles = add_vehicle.objects.filter(status=True)
    for vehicle in departed_vehicles:
        total_departed_charge += Decimal(vehicle.parking_charge)

    overall_total_charge = total_parked_charge + total_departed_charge

    total_vehicle_limit = int(Category.objects.aggregate(total_limit=Sum('vehicle_limit'))['total_limit'])

    unique_vehicle_types = Category.objects.values('vehicle_type').annotate(count=Count('vehicle_type'))

    total_vehicle_count = Category.objects.count()

    context = {
        'dash': dash,
        'parked_count': parked_count,
        'departed_count':departed_count,
        'overall_total_charge': overall_total_charge,
        'total_vehicle_limit': total_vehicle_limit,
        'unique_vehicle_types': unique_vehicle_types,
        'total_vehicle_count': total_vehicle_count,
    }
    return render(request, 'dashboard.html', context)


# ===========================================================================================================
def report(request):
    v_data = add_vehicle.objects.all()

    context = {
        'v_data': v_data,
    }
    return render(request, 'report.html', context)

# vehicle_entry=================================================================
def vehicleentry(request):
    display = Category.objects.all()
    vehicle_entry_data = add_vehicle.objects.all()

    context = {
        'vehicle_entry_data': vehicle_entry_data,
        'display': display,
    }
    return render(request,'vehicleentry.html',context)


from django.utils import timezone

def addvehicle_entry(request):
    if request.method == 'POST':
        vehicle_no = request.POST.get('vehicle_no')
        parking_area_no= request.POST.get('parking_area_no')  # Get the ID
        parking_charge = request.POST.get('parking_charge')
        vehicle_type_id = request.POST.get('vehicle_type')
        arrival_time = timezone.now()

        # Retrieve the Category instance with the given ID
        v_type = Category.objects.get(id=vehicle_type_id)

        # Create the add_vehicle instance with the correct data
        v = add_vehicle(
            vehicle_no=vehicle_no,
            parking_area_no=parking_area_no,  # Use the ID
            vehicle_type=v_type,
            parking_charge=parking_charge,  # Assign the value from the form
            arrival_time=arrival_time,
        )
        v.save()

        return redirect('vehicle_entry')

    return render(request, 'vehicleentry.html')



#change_password======================================================================================
def c_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if new_password == confirm_password:
            if User.objects.filter(current_password=current_password).exists():
                print('current_password Exists...! Try with another name')
                return redirect('c_password')
            else:
                if User.objects.filter(current_password=new_password).exists():
                    print("Password is almost similar, Try another one")
                    return redirect('c_password')

                else:
                    user = User.objects.create_user(current_password=current_password, new_password=new_password, confirm_password=confirm_password)
                    user.save()   # Send the data to the database : Table : User
                    return redirect('c_password')

        else:
            print('Current password and new password are same..!')
            return redirect('c_password')

    else:
        return render(request, 'account_settings.html')

# reports=====================================================================================
def v_report(request):
    c_data = Category.objects.all()
    v_data = add_vehicle.objects.all()

    report_data = list(c_data) + list(v_data)

    page_num = request.GET.get('page')  # creating total pages
    paginator = Paginator(report_data, 10)

    try:
        report_data = paginator.page(page_num)
    except PageNotAnInteger:
        report_data = paginator.page(1)
    except EmptyPage:
        report_data = paginator.page(paginator.num_pages)

    context = {
        'report_data': report_data,
    }
    return render(request, 'report.html', context)


def addcategory(request):
    if request.method == 'POST':
        parking_area_no = request.POST.get('parking_area_no')
        vehicle_type = request.POST.get('vehicle_type')  # Removed the space before 'vehicle_type'
        vehicle_limit = request.POST.get('vehicle_limit')
        parking_charge = request.POST.get('parking_charge')  # Removed the space before 'parking_charge'
        new_v = Category(parking_area_no=parking_area_no, vehicle_type=vehicle_type, vehicle_limit=vehicle_limit,
                         parking_charge=parking_charge)
        new_v.save()
        return redirect('showvehicle')  # Redirect to the employee list page or a success page

    return render(request, 'category.html')






#account setting function
def accountsetting(request):
    return render(request, 'accountsetting.html')

#
# def change_password(request):
#     context = {}
#     ch = register_table.objects.filter(user__id=request.user.id)
#     if len(ch) > 0:
#         data = register_table.objects.get(user__id=request.user.id)
#         context["data"] = data
#     if request.method == "POST":
#         current = request.POST["cpwd"]
#         new_pas = request.POST["npwd"]
#
#         user = User.objects.get(id=request.user.id)
#         un = user.username
#         check = user.check_password(current)
#         if check == True:
#             user.set_password(new_pas)
#             user.save()
#             context["msz"] = "Password Changed Successfully!!!"
#             context["col"] = "alert-success"
#             user = User.objects.get(username=un)
#             login(request, user)
#         else:
#             context["msz"] = "Incorrect Current Password"
#             context["col"] = "alert-danger"
#
#     return render(request, "change_password.html", context)





