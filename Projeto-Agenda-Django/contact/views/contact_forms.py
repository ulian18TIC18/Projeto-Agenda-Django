from django.shortcuts import render

from contact.forms import ContactForm


# Create your forms here.


def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)        
        }

        return render(
            request,
            'contact/create.html',
            context
        )            

    context = {
        'form': ContactForm()        
    }

    return render(
        request,
        'contact/create.html',
        context
    )