import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category,State, Iso, Region, Site


def run():
    fhand = open('whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        try:
            c, created_c = Category.objects.get_or_create(category=row[7])
        except:
            c = None
        try:
            s, created_s = State.objects.get_or_create(state=row[8])
        except:
            s = None
        try:
            i, created_i = Iso.objects.get_or_create(iso=row[10])
        except:
            i = None
        try:
            r, created_r = Region.objects.get_or_create(region=row[9])
        except:
            r = None

        try:
            y = int(row[3])
        except:
            y = None
        try:
            validate_hectares = float(row[6])
        except:
            validate_hectares = None

        site = Site(name=row[0],description = row[1],justification=row[2],year=y,longitude=row[4],latitude=row[5],area_hectares=validate_hectares,category=c, state=s, iso=i, region=r)
        site.save()