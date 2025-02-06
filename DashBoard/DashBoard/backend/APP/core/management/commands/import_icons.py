import os
from django.core.management.base import BaseCommand
from django.conf import settings
from APP.core.models import Icon

class Command(BaseCommand):
    help = "Importe les icônes depuis le dossier frontend/Ressources/Icon"

    def handle(self, *args, **options):
        # Construit le chemin absolu vers le dossier des icônes
        icons_dir = os.path.join(settings.BASE_DIR,'..','Ressources', 'Icon')
        
        if not os.path.exists(icons_dir):
            self.stdout.write(self.style.ERROR(f"Dossier non trouvé: {icons_dir}"))
            return

        files = os.listdir(icons_dir)
        png_files = [f for f in files if f.lower().endswith('.png')]

        if not png_files:
            self.stdout.write(self.style.WARNING("Aucun fichier .png trouvé dans le dossier."))
            return

        for filename in png_files:
            icon_name = os.path.splitext(filename)[0]
            if Icon.objects.filter(icon_name=icon_name).exists():
                self.stdout.write(self.style.WARNING(f"L'icône '{icon_name}' existe déjà."))
                continue

            # Chemin relatif correspondant à upload_to défini dans le modèle
            relative_path = os.path.join('frontend', 'Ressources', 'Icon', filename)
            Icon.objects.create(icon_name=icon_name, icon_image=relative_path)
            self.stdout.write(self.style.SUCCESS(f"Icône importée : {icon_name}"))

        self.stdout.write(self.style.SUCCESS("Importation terminée."))