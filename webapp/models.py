from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.deletion import get_candidate_relations_to_delete
from django.contrib.auth import get_user_model


class Manager(models.Manager):
    def get_queryset(self):
        return super(Manager, self).get_queryset().filter(is_deleted=False)


# Create your models here.
class IsDeletedMixin(models.Model):
    is_deleted = models.BooleanField(default=False)

    objects = Manager()

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        delete_candidates = get_candidate_relations_to_delete(self.__class__._meta)
        if delete_candidates:
            for rel in delete_candidates:
                if rel.on_delete.__name__ == 'CASCADE' and rel.one_to_many and not rel.hidden:
                    for item in getattr(self, rel.related_name).all():
                        item.delete()

        self.save(update_fields=['is_deleted', ])

    class Meta:
        abstract = True


class Review(IsDeletedMixin):
    STATUSES = [
        ('Принят', 'Принят'),
        ('Отклонен', 'Отклонен'),
        ('На модерации', 'На модерации')
    ]
    name = models.CharField(max_length=15, verbose_name='Имя')
    image = models.ImageField(upload_to='review_pics', verbose_name='Image')
    text = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Текст поста')
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.CharField(max_length=50, choices=STATUSES, default='На модерации', 
                              verbose_name='Статус', null=True)
    author = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE,
        verbose_name='Автор', related_name='reviews'
    )
    edit_by_admin = models.CharField(max_length=50, verbose_name='Изменен админом')

    def __str__(self):
        return self.name
    