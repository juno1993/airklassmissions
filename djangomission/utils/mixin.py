from utils.api_view import CustomAPIView


class ListMixin(CustomAPIView):
    def get(self, request, **kwargs):
        return self.list(request, **kwargs)


class CreateMixin(CustomAPIView):
    def post(self, request, **kwargs):
        return self.create(request, **kwargs)


class DeleteMixin(CustomAPIView):
    def deleter(self, request, **kwargs):
        return self.delete(request, **kwargs)
