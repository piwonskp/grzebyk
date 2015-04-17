
from mainapp.models import Product
from mainapp.views.my_list_view import MyListView


class ShopView(MyListView):
    template_name = 'shop.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 8
