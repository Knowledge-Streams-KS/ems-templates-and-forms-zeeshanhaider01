from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Event
from .forms import UserForm, EventForm, eventRegisterForm


def createvent(request):

    if request.method=="POST":
        form=EventForm(request.POST)
        form.save()
        return HttpResponse("Event successfully created.")
        # if form.is_valid():
        #     name=form.cleaned_data["name"]
        #     detail=form.cleaned_data["detail"]
        #     datetime=form.cleaned_data["datetime"]
        #     location=form.cleaned_data["location"]          
        #     Event.objects.create(name=name,detail=detail,datetime=datetime,location=location)
        #     return HttpResponse("Event successfully created.")
    
    else:
        form=EventForm()
        return render(request,"app/eventForm.html",{"form":form})
    
def updateevent(request,id,name):
    if request.method=="POST":
        event=Event.objects.get(id=int(id))
        event.name=name
        form=EventForm(request.POST, instance=event)
        print("form.data: ",form.data)
        form.save()
        return HttpResponse("object is successfully updated")
    else:
        form=EventForm()


def createuser(request):

    if request.method=="POST":
        form=UserForm(request.POST)

        if form.is_valid():
            name=form.cleaned_data["name"]
            email=form.cleaned_data["email"]
            # eventslst=form.cleaned_data["events"]

            User.objects.create(name=name,email=email)

            return HttpResponse("user Successfully created")

    else:
        form=UserForm()
        return render(request,"app/userForm.html",{"form":form})
    

def allevents(request):
    events=Event.objects.all()

    return render(request,"app/allevents.html",{"events":events})

def register_in_event(request,id):    
    form=eventRegisterForm()
    event=Event.objects.get(id=int(id))
    return render(request,"app/restrationForm.html",{"form":form,"event":event})

def register_in_event_form(request):
    if request.method=="POST":
        form=eventRegisterForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data["email"]
            id=form.data["id"]
            user=User.objects.get(email=email)
            newevent=Event.objects.get(id=int(id))
            user.events.add(newevent)
            return HttpResponse(f"You are successfully registered in this event: {newevent.name}")
