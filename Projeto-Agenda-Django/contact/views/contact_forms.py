from django.shortcuts import get_object_or_404, render, redirect

from django.core.paginator import Paginator

from django.db.models import Q

from contact.models import Contact

# Create your forms here.

def create(request):    

    context = {
        
    }

    return render(
        request,
        'contact/create.html',
        context
    )