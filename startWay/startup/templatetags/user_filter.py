from django import template

register = template.Library()


    
@register.filter
def is_user(user, role):
    """
    checks if the user is of relation to a particular role : employee ; founder or investor to setup simple 
    """
    return  hasattr(user, role)