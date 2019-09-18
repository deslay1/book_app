#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are SellerOrBuyeru sure it's installed and "
            "available on SellerOrBuyerur PYTHONPATH environment variable? Did SellerOrBuyeru "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
