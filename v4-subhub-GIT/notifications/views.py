from django.shortcuts import render, redirect, get_object_or_404
from .models import Notification, Alert
from django.core.mail import send_mail
from .forms import NotificationForm
from django.conf import settings
from .filters import OrderFilter

def notifications_view(request):
    notifications = Notification.objects.all().order_by('-date_sent')
    alerts = Alert.objects.all()
    myFilter = OrderFilter(request.GET, queryset=notifications)
    notifications=myFilter.qs
    context = {'notifications': notifications, 'alerts': alerts, 'myFilter': myFilter}
    return render(request, 'notifications/notifications.html',context)

def new_notification_view(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['recipient']
            subject = form.cleaned_data['title']
            message = form.cleaned_data['details']
            # Send email
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                    [email],
                fail_silently=False,
            )
            form.save()
            return redirect('notifications')
    else:
        form = NotificationForm()
    
    return render(request, 'notifications/new_notification.html', {'form': form})

def update_notification_view(request,pk):
    record = get_object_or_404(Notification, pk=pk)
    if request.method == 'POST':
        form = NotificationForm(request.POST,instance=record)
        if form.is_valid():
            email = form.cleaned_data['recipient']
            subject = form.cleaned_data['title']
            message = form.cleaned_data['details']
            # Send email
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                    [email],
                fail_silently=False,
            )
            form.save()
            return redirect('notifications')
    else:
        form = NotificationForm(instance=record)
    
    return render(request, 'notifications/update_notification.html', {'form': form})

def all_notifications_view(request):
    notifications = Notification.objects.all().order_by('-date_sent')
    myFilter = OrderFilter(request.GET, queryset=notifications)
    notifications=myFilter.qs
    context={'notifications': notifications,'myFilter':myFilter}
    return render(request, 'notifications/notifications_list.html',context)

def notification_detail(request, pk):
    notification = get_object_or_404(Notification, id=pk,)
    return render(request, 'notifications/details_noti.html', {'notification': notification})

def search_noti(request):
    if request.method == "POST":
        searched=request.POST.get('searched','')
        notifications=Notification.objects.filter(title__contains=searched)

    return render(request,'notifications/search_noti.html',{'searched':searched,'notifications':notifications})

