import os
import sys

# Ajoutez le dossier parent au PYTHONPATH, pour inclure "frontend"
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Impossible d'importer Django.") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
