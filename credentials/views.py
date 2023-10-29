from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import Department, Course, Purpose
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .forms import RegistrationForm
# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            request.session['logged_in'] = True
            return redirect('dashboard')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Pass']
        conf_pass = request.POST['conf_pass']
        if password == conf_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password = password)
            user.save();
            return redirect('login')
        else:
            messages.info(request,"password not matched")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

@login_required(login_url='/credentials/login')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def dashboard(request):
    if request.user.is_authenticated and request.session.get('logged_in'):
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            name = request.POST.get('name')
            dob = request.POST.get('dob')
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            address = request.POST.get('address')
            department = request.POST.get('dept')
            course = request.POST.get('crs')
            purpose = request.POST.get('prs')
            materials = request.POST.getlist('materials[]')
            errors = []

            if not form.is_valid():
                if not department or department == "0":
                    errors.append('Please select a Department.')
                if not course or course == "0":
                    errors.append('Please select a Course.')
                if not purpose or purpose == "0":
                    errors.append('Please select a Purpose.')

                if not materials:
                    errors.append('Select at least one material provided.')

            if errors:
                deptcontext = Department.objects.all()
                crscontext = Course.objects.all()
                prscontext = Purpose.objects.all()
                return render(request, 'dashboard.html', {'errors': errors,'department': deptcontext, 'course': crscontext, 'purposes': prscontext})
            else:
                return redirect('confirm')

        deptcontext = Department.objects.all()
        crscontext = Course.objects.all()
        prscontext = Purpose.objects.all()
        return render(request, "dashboard.html", {'department': deptcontext, 'course': crscontext, 'purposes': prscontext})
    else:
        return redirect('login')


def logout(request):
    if 'logged_in' in request.session:
        del request.session['logged_in']
    auth.logout(request)
    return redirect('login')

def confirm(request):
    return render(request,'test.html')