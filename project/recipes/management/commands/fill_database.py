from django.core.management.base import BaseCommand

from .data import value
from ...models import Category, Reciepes


class Command(BaseCommand):

    help = "This command populates the database"

    def handle(self, *args, **kwargs):
        for val in value:
            try:
                category_name = Category.objects.create(name=val['category'])
                category_name.save()
                Reciepes.objects.create(title=val['title'],
                                        description=val['description'],
                                        category=category_name,
                                        ingredients=val['ingredients'])
            except BaseException as e:
                    print(e)
        self.stdout.write(self.style.SUCCESS('Данные успешно записаны в базу данных'))



        #  data = json.loads(f.read())
        #     for el in data:
        #         try:
        #             Company.objects.create(
        #                 id_company=el.get('id_company', None),
        #                 Company=el.get('Company', None),
        #                 Direction=el.get('Direction', None),
        #                 Description=el.get('Description', None),
        #                 Categories=el.get('Categories', None),
        #                 Products=el.get('Products', None),
        #                 Status=el.get('Status', None),
        #                 INN=el.get('INN', None),
        #                 OGRN=el.get('OGRN', None),
        #                 KPP=el.get('KPP', None),
        #                 Entity=el.get('Entity', None),
        #                 Employ_number=el.get('Employ_number', None),
        #                 Region=el.get('Region', None),
        #                 Locality=el.get('Locality', None),
        #                 Address=el.get('Address', None),
        #                 Telephone=el.get('Telephone', None),
        #                 Post=el.get('Post', None),
        #                 URL=el.get('URL', None),
        #                 VK=el.get('VK', None),
        #                 Instagram=el.get('Instagram', None),
        #                 Facebook=el.get('Facebook', None),
        #                 Youtube=el.get('Youtube', None),
        #                 Catalogs=el.get('Catalogs', None)
        #             )
        #             print(f'Сделана запись: {el.get("id_company")}')
        #         except BaseException as e:
        #             print(f'{el.get("id_company")} - error - {e}')
        #     self.stdout.write(self.style.SUCCESS('Данные успешно записаны в базу данных'))
