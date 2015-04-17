
from mainapp.models import Article
from mainapp.views.my_list_view import MyListView

class IndexView(MyListView):
    template_name = 'index.html'
    context_object_name = 'articles'
    model = Article
    paginate_by = 5