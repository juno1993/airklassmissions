





def get_object_or_None(model, **fields):
    items = model.objects.filter(**fields)
    return items.first() if items.exists() else None
