import cachetools
import psycopg2
from django.db import connection
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')
django.setup()

category_cache = cachetools.LRUCache(maxsize=100)


def get_categories():
    if 'name' in category_cache:
        return category_cache['name']
    else:
        categories = fetch_categories_from_database()
        category_cache['name'] = categories
        return categories

def fetch_categories_from_database():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM main_category")
        categories = cursor.fetchall()
        return categories


if __name__ == "__main__":
    print(get_categories())