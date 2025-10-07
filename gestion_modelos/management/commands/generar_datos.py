from django.core.management.base import BaseCommand
from faker import Faker
from gestion_modelos.models import *

class Command(BaseCommand):
    help = 'Generando datos; Usando Faker'
    
    def handle(self, *argsm, **kwargs):
        fake = Faker('es_ES')
    
        for _ in range(10):
            Usuario.objects.create(
                nombre = fake.name(),
                correoElectronico=fake.unique.email(),
                password=fake.password(length=12)
            )
            
        self.stdout.write(self.style.SUCCESS('Datos generados correctamente'))