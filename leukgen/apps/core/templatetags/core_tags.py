from django.template import Library, loader, Context

register = Library()


# http://stackoverflow.com/questions/1490059/django-inclusion-tag-with-configurable-template
@register.simple_tag(takes_context=True)
def panel_default_form(context,  *args, **kwargs):

    head = kwargs['head']
    url_dir = kwargs['url_dir']
    btn_text = kwargs['btn_text']
    footer = kwargs['footer']

    t = loader.get_template("core/panel_default_form.html")

    try:
        context_object = context["object"]
    except KeyError:
        context_object = ''

    try:
        form = context["form"]
    except KeyError:
        form = ''

    try:
        csrf_token = context["csrf_token"]
    except KeyError:
        csrf_token = ''

    return t.render(Context({
        'head': head,
        'url_dir': url_dir,
        'btn_text': btn_text,
        'footer': footer,
        'form': form,
        'csrf_token': csrf_token,
        'object': context_object,
    }))
