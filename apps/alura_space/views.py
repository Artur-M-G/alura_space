from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from photography_api.models import Photography
from .forms import PhotographyForms

def index(request):
    """
    Displays the website's home page with all registered images
    """

    photographys = Photography.objects.order_by('-date').filter(published=True)
    categories = Photography.get_category_choices()
    return render(request, 'alura_space/index.html', {'cards':photographys, 'categories': categories})

def image(request, id):
    """
    Display the image in detail by id
    """

    photo = get_object_or_404(Photography, pk=id)
    return render(request, 'alura_space/image.html', {'photo': photo})

def filter_category(request, category_display):
    """
    Filter images by their category
    """

    category = Photography.get_category_id(category_display)
    photographys = Photography.objects.order_by('-date').filter(published=True, category=category)
    categories = Photography.get_category_choices()

    return render(request, 'alura_space/index.html', {'cards':photographys, 'categories': categories})

def search(request):
    """
    Filter image by user search
    """

    photographys = Photography.objects.order_by('-date').filter(published=True)
    categories = Photography.get_category_choices()
    
    if 'search' in request.GET:
        search_field = request.GET['search']
        if search_field:
            photographys = Photography.objects.order_by('-date').filter(published=True, name__icontains=search_field)

    return render(request, 'alura_space/index.html', {'cards':photographys, 'categories': categories})

def create_image(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User not logged in')
        return redirect('login')
    
    form = PhotographyForms()

    if request.method == 'POST':
        form = PhotographyForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New photo registered!')
            return redirect('index')

    return render(request, 'alura_space/new_image.html', {'form':form})

def edit_image(request, id):
    if not request.user.is_authenticated:
        messages.error(request, 'User not logged in')
        return redirect('login')
    
    photography = Photography.objects.get(id=id)
    form = PhotographyForms(instance=photography)

    if request.method == 'POST':
        form = PhotographyForms(request.POST, request.FILES, instance=photography)
        if form.is_valid():
            print(request.POST)
            form.save()
            messages.success(request, 'Photo edited successfully!')
            return redirect('index')

    return render(request, 'alura_space/edit_image.html', {'form':form, 'foto_id': id})

def delete_image(request, id):
    if not request.user.is_authenticated:
        messages.error(request, 'User not logged in')
        return redirect('login')
    
    photography = Photography.objects.get(id=id)
    photography.delete()
    messages.success(request, 'Photo deleted successfully!')

    return redirect('index')
