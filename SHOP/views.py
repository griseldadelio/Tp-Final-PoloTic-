from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # product_objects = Products.objects.all()

    # #search code
    # item_name = request.GET.get('item_name')
    # if item_name != '' and item_name is not None:
    #     product_objects = product_objects.filter(title__icontains=item_name)

    # #paginator code
    # paginator = Paginator(product_objects,4)
    # page = request.GET.get('page')
    # product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html')
