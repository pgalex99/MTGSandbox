import requests
from dateutil import parser

from api.models import CardSet

from django.core.management.base import BaseCommand


def fetch_card_sets():

    url = "https://api.scryfall.com/sets"
    response = requests.get(url)
    
    if response.status_code == 200:

        response = response.json()
        sets = response.get("data", [])

        for set_data in sets:

            name = set_data.get("name")
            date_str = set_data.get("released_at")
            set_type = set_data.get("set_type")

            # Skip token and memorabilia sets as they are not relevant for our database
            if set_type in ["token", "memorabilia"]:
                continue

            if date_str:
                date = parser.parse(date_str)

            if name and date_str:
                CardSet.objects.create(name=name, date=date)
    return


class Command(BaseCommand):
    help = "Populate CardSet table with Scryfall sets"

    def handle(self, *args, **options):

        self.stdout.write("Fetching and populating CardSet data...")
        fetch_card_sets()

        self.stdout.write(self.style.SUCCESS("CardSet data populated successfully."))
