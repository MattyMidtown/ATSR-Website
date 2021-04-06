from django import template

from products.models import Orders, AuthUser, Userprofile

register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Orders.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].id.count()
        return 0
