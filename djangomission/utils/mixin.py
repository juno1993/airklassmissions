from utils.api_view import CustomAPIView


class ListMixin(CustomAPIView):
    def get(self, request, **kwargs):
        return self.list(request, **kwargs)


class CreateMixin(CustomAPIView):
    def get(self, request, **kwargs):
        return self.creator(request, **kwargs)


class DeleteMixin(CustomAPIView):
    def get(self, request, **kwargs):
        return self.deleter(request, **kwargs)
