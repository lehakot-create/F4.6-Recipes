from django.core.management.base import BaseCommand

from .data import value
from ...models import Category, Recipes


class Command(BaseCommand):

    help = "This command populates the database"

    def handle(self, *args, **kwargs):
        for val in value:
            try:
                category_name = Category.objects.create(name=val['category'])
                category_name.save()
                Recipes.objects.create(title=val['title'],
                                        description=val['description'],
                                        category=category_name,
                                        ingredients=val['ingredients'])
            except BaseException as e:
                    print(e)
        self.stdout.write(self.style.SUCCESS('Данные успешно записаны в базу данных'))
