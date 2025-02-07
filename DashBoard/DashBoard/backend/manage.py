import os
import sys

# Add the project root (Dashboard) to sys.path.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def main():
    # Update DJANGO_SETTINGS_MODULE if your settings file is nested.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.dashboard.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
