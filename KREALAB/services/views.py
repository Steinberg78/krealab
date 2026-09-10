from django.shortcuts import render

from .models import ContactRequest


def handle_contact_form(request):
    submitted = False

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        service = request.POST.get('service', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and service and message:
            ContactRequest.objects.create(
                name=name,
                email=email,
                service=service,
                message=message,
            )
            submitted = True

    return submitted


def home(request):
    return render(request, 'services/pages/home_page.html')


def site_web(request):
    return render(request, 'services/pages/site_web.html')


def community(request):
    return render(request, 'services/pages/community.html')


def motion(request):
    return render(request, 'services/pages/motion.html')


def contenu(request):
    return render(request, 'services/pages/contenu.html')


def publicite(request):
    return render(request, 'services/pages/publicite.html')


def automation(request):
    return render(request, 'services/pages/automation.html')


def contact(request):
    submitted = handle_contact_form(request)
    return render(request, 'services/contact.html', {'submitted': submitted})
