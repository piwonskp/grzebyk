
from mainapp.models import Product
from mainapp.views.MyListView import MyListView


class Shop(MyListView):
    template_name = 'shop.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 10
