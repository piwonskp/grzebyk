from django.views.generic import ListView


class MyListView(ListView):
    ''' Nawigacja miedzy stronami
    '''
    def get_context_data(self, **kwargs):
        context = super(MyListView, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page = context['page_obj']
        step_links = self.page_links(paginator, page)
        context['step_links'] = step_links
        return context

    @staticmethod
    def page_links(paginator, page):
        step_links = [1]
        page_number = page.number
        pages = paginator.num_pages
        if page_number > 3:
            step_links.append('...')
        page_start = page_number-3 if page_number-3 > 1 else 2
        page_stop = page_number+3 if page_number+3 < pages else pages
        for i in range(page_start, page_stop):
            step_links.append(i)
        if page.number < pages-3:
            step_links.append('...')
        if pages > 1:
            step_links.append(pages)
        return step_links


