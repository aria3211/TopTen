from atexit import register
from unicodedata import name
from django import template




register = template.Library()


@register.filter(name='lst')

def lists(value):
    lst = []
    for i in range(len(value)):
        lst.append(i)
        return lst[0],i


# def For(value):
