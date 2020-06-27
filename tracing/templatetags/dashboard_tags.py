from django import template

register = template.Library()

@register.filter(needs_autoescape=False)
def difference(value, arg):
    try:
        result_num = (float(arg) - float(value)) / (float(arg) * 0.01)
        if result_num > 0:
            result = '<span class="text-success mr-2"><i class="fa fa-arrow-up"></i>%s%%</span>' % result_num
            # result = '<font color="#28a901">%s%%</font>' % result_num
        elif result_num < 0:
            result = '<span class="text-danger mr-2"><i class="fas fa-arrow-down"></i>%s%%</span>' % result_num
            # result = '<font color="#f63434">%s%%</font>' % result_num
    except (TypeError, ZeroDivisionError):
        return None
    return result
