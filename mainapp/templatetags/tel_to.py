from xml.etree import ElementTree as ET

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="tel_to")
def tel_to(input_str):
    """
    Create link `telto:`
    """
    link_telto = ET.Element("a", {"href": f"tel:{input_str}"})
    link_telto.text = input_str
    return mark_safe(ET.tostring(link_telto, encoding="unicode"))
