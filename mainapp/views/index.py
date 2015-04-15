

from mainapp.models import Article
from mainapp.views.MyListView import MyListView

class Index(MyListView):
    template_name = 'index.html'
    context_object_name = 'articles'
    model = Article
    paginate_by = 5