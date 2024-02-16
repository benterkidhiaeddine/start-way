"""
Some simple filters
 * `user_can`, which filters an object taking a string
   parameter, returning True or False depending on whether the current
   user "can" do the action in the parameter. This is done by calling
   `user_can_<action>` on the object.
   Anonymous users always return `False`.
 * `user_has`, which pulls the result of the `user_has_<feature>()`;
   anonymous users get `False`.
 * `user_property` pulls the result of `user_<property>()`; anonymous
   users get `None`.
Relies on django-globals: https://github.com/svetlyak40wt/django-globals
Untested, based on internal code that didn't use django-globals.
"""

from django import template

register = template.Library()


    
@register.filter
def is_user(user, role):
    "checks if the user is of relation to a particular role : employee ; founder or investor"
    return  hasattr(user, role)