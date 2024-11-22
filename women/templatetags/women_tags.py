from django import template
from django.db.models import Count

import women.views as views
from women.models import Category, TagPost

register = template.Library()


@register.inclusion_tag('women/list_categories.html')
def show_categories(cats_selected=0):
    cats = Category.objects.annotate(total=Count('posts')).filter(total__gt=0)
    return {'cats': cats, 'cat_selected': cats_selected}


@register.inclusion_tag('women/list_tags.html')
def show_all_tags():
    return {'tags': TagPost.objects.annotate(total=Count('tags')).filter(total__gt=0)}
