from backend.entity import Pagination
from backend.errors.errors import Errors
from backend.errors.http_exception import HttpException
from backend.models import BaseModel


class BaseRepository:
    Model = None

    def __init__(self, model_class) -> None:
        super().__init__()
        self.Model: BaseModel = model_class

    def get_all(self, paginator=None, order_by: list = None):
        if order_by:
            records = self.Model.objects.order_by(*order_by).filter(deleted=False).all()
        else:
            records = self.Model.objects.filter(deleted=False).all()
        return records[paginator.offset:paginator.limit] if paginator else records

    def get_by_id(self, record_id):
        try:
            return self.Model.objects.get(id=record_id)
        except self.Model.DoesNotExist:
            raise HttpException(status_code=Errors.NOT_FOUND.value,
                                detail=Errors.NOT_FOUND.name)

    def filter_by_kwargs(self, kwargs, paginator=None, order_by=list()):
        try:
            if order_by:
                records = self.Model.objects.order_by(*order_by).exclude(deleted=True).filter(**kwargs)
            else:
                records = self.Model.objects.exclude(deleted=True).filter(**kwargs)
        except Exception:  # no 'deleted' field
            if order_by:
                records = self.Model.objects.order_by(*order_by).filter(**kwargs)
            else:
                records = self.Model.objects.filter(**kwargs)
        return records[paginator.offset:paginator.limit] if paginator else records

    def create(self, **kwargs):
        return self.Model.objects.create(**kwargs)

    def update(self, record_id, **kwargs):
        if self.Model.objects.filter(id=record_id).exists():
            self.Model.objects.filter(id=record_id).update(**kwargs)
            return self.get_by_id(record_id)
        else:
            raise HttpException(status_code=Errors.NOT_FOUND.value,
                                detail=self.Model.__str__())

    def update_or_create(self, record_id, **kwargs):
        if record_id:
            return self.update(record_id, **kwargs)
        else:
            return self.create(**kwargs)

    def delete(self, record_id):
        record = self.get_by_id(record_id)
        record.deleted = True
        record.save()
        return record

    def hard_delete(self, record_id):
        return self.get_by_id(record_id).delete()

    def delete_by_kwargs(self, kwargs):
        return self.Model.objects.filter(**kwargs).update({'deleted': True})

    def hard_delete_by_kwargs(self, kwargs):
        return self.Model.objects.filter(**kwargs).delete()

    def get_random(self):
        return self.Model.objects.order_by("?").first()
