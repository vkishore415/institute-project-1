from django.shortcuts import render
from .models import FeedBackData,ContactFormData
from.forms import FeedbackForm
from.forms import ContactForm
from django.http.response  import HttpResponse
#from django.http.response import HttpResponse
import datetime
#added demo to git
#added demo from pycharm to git
date1=datetime.datetime.now()
# Create your views here.
def main_page(request):
    return render(request,'base.html')


def home_page(request):
    return render(request,'home_page.html')


def contact_page(request):
    if request.method=='POST':
        cform=ContactForm(request.POST)
        if cform.is_valid():
            try:
                name=cform.cleaned_data.get('name')
                mobile=cform.cleaned_data.get('mobile')
                email=cform.cleaned_data.get('email')
                courses=cform.cleaned_data.get('courses')
                shifts=cform.cleaned_data.get('shifts')
                location=cform.cleaned_data.get('location')
                gender=cform.cleaned_data.get('gender')
                start_date=cform.cleaned_data.get('start_date')
                data1=ContactFormData(
                    name=name,
                    mobile=mobile,
                    email=email,
                    courses=courses,
                    shifts=shifts,
                    location=location,
                    gender=gender,
                    start_date=start_date
                )
                data1.save()
                cform=ContactForm()
                return render(request,'contact_page.html',{'cform':cform})
            except Exception as e:
                return HttpResponse(str(e))
        else:
            return HttpResponse('invalid data')
    else:
        cform = ContactForm()

        return render(request, 'contact_page.html', {'cform':cform})


def courses_page(request):
    return render(request,'couses_page.html')


def feedback_page(request):
    if request.method=="POST":
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name=request.POST.get('name','')
            rating=request.POST.get('rating','')
            feedback=request.POST.get('feedback','')
            data=FeedBackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date1
            )
            data.save()

            fform=FeedbackForm()
            return render(request,'feedback_page.html',{'fform':fform})
        else:
            return HttpResponse('invali user data')

    else:
            fform=FeedbackForm()
            return render(request,'feedback_page.html',{'fform':fform})

















    return render(request,'feedback_page.html')


def team_page(request):
    return render(request,'team_page.html')


def gallery_page(request):
    return render(request,'gallery_page.html')
