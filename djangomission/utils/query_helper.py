from utils.custom_exception import NotFoundException, ForbiddenException


def get_object_or_None(model, **fields):
    items = model.objects.filter(**fields)
    return items.first() if items.exists() else None


def get_object_or_404(model, **fields):
    obj = get_object_or_None(model, **fields)
    if obj is None:
        raise NotFoundException(model=model, **fields)
    return obj
