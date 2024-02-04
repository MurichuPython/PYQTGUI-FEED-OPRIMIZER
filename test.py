import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "feed_gui.settings")

import django
django.setup()

def check(num):
    if num == '' or num== None:
        return 0
    return float(num)
from feed.models import Feed
Feed.objects.all().delete()
data={'Maize': {'DM%': 88, 'CP%': 8, 'CF%': 12, 'Ca%': 0.17, 'P%': 0.55, 'ME': 3000, 'Lysine%': 0.53, 'Methionine%': 0.29, 'cost': 33.56}, 'Maize_bran': {'DM%': 88, 'CP%': 9.4, 'CF%': 13, 'Ca%': 0.04, 'P%': 1.03, 'ME': 2200, 'Lysine%': 0.18, 'Methionine%': 0.21, 'cost': 66.8}, 'Maize_cob_meal': {'DM%': 88, 'CP%': 7, 'CF%': 8, 'Ca%': None, 'P%': 0.3, 'ME': None, 'Lysine%': None, 'Methionine%': None, 'cost': 17.86}, 'Rice_bran': {'DM%': 88, 'CP%': 13.5, 'CF%': 6.5, 'Ca%': 0.06, 'P%': 1.43, 'ME': 3000, 'Lysine%': 0.5, 'Methionine%': 0.22, 'cost': 87.13}, 'Cassava_meal': {'DM%': 88, 'CP%': 2.8, 'CF%': 4.0, 'Ca%': 0.3, 'P%': 0.05, 'ME': 3000, 'Lysine%': None, 'Methionine%': None, 'cost': 88.56}, 'Molasses': {'DM%': 75, 'CP%': 3.0, 'CF%': None, 'Ca%': 0.75, 'P%': 0.08, 'ME': 2330, 'Lysine%': None, 'Methionine%': None, 'cost': 89.91}, 'Millet': {'DM%': 88, 'CP%': 10.5, 'CF%': 2.0, 'Ca%': 0.05, 'P%': 0.4, 'ME': 1392, 'Lysine%': 0.2, 'Methionine%': 0.27, 'cost': 26.3}, 'Sorghum': {'DM%': 88, 'CP%': 9.0, 'CF%': 2.1, 'Ca%': 0.03, 'P%': 0.28, 'ME': 3250, 'Lysine%': 0.2, 'Methionine%': 0.12, 'cost': 10.61}, 'Fish_meal': {'DM%': 88, 'CP%': 60.0, 'CF%': 1.0, 'Ca%': 4.37, 'P%': 2.53, 'ME': 2310, 'Lysine%': 4.08, 'Methionine%': 1.7, 'cost': 28.42}, 'Cotton_seed_cake': {'DM%': 88, 'CP%': 40.0, 'CF%': 14, 'Ca%': 0.2, 'P%': 1.2, 'ME': 968, 'Lysine%': 1.6, 'Methionine%': 0.52, 'cost': 53.12}, 'Soya_bean_meal': {'DM%': 88, 'CP%': 43.0, 'CF%': 6, 'Ca%': 0.53, 'P%': 0.64, 'ME': 2800, 'Lysine%': 2.84, 'Methionine%': 0.65, 'cost': 9.29}, 'Limestone': {'DM%': 98, 'CP%': None, 'CF%': None, 'Ca%': 38.0, 'P%': None, 'ME': None, 'Lysine%': None, 'Methionine%': None, 'cost': 45.74}, 'Oyster_shells': {'DM%': 98, 'CP%': None, 'CF%': None, 'Ca%': 35.0, 'P%': None, 'ME': None, 'Lysine%': None, 'Methionine%': None, 'cost': 17.99}, 'Wheat_pollard': {'DM%': 98, 'CP%': 15.0, 'CF%': None, 'Ca%': None, 'P%': None, 'ME': None, 'Lysine%': 0.6, 'Methionine%': 0.35, 'cost': 36.69}, 'Wheat_bran': {'DM%': 91.4, 'CP%': 15.0, 'CF%': 12.5, 'Ca%': None, 'P%': 1.2, 'ME': None, 'Lysine%': 0.6, 'Methionine%': 0.35, 'cost': 61.48}, 'Sunflower_cake': {'DM%': 92, 'CP%': 35.0, 'CF%': 26.7, 'Ca%': None, 'P%': None, 'ME': None, 'Lysine%': 1.8, 'Methionine%': 1.2, 'cost': 23.94}, 'Groundnut_cake': {'DM%': 93, 'CP%': 40.0, 'CF%': 7.3, 'Ca%': None, 'P%': None, 'ME': None, 'Lysine%': 2.0, 'Methionine%': 1.8, 'cost': 9.33}, 'Rice_polishings': {'DM%': 92.5, 'CP%': 12.0, 'CF%': 4.2, 'Ca%': None, 'P%': None, 'ME': None, 'Lysine%': 4.0, 'Methionine%': 0.4, 'cost': 16.97}, 'Dicalcium_phosphate': {'DM%': None, 'CP%': None, 'CF%': None, 'Ca%': 24, 'P%': 18, 'ME': None, 'Lysine%': None, 'Methionine%': None, 'cost': 23.67}, 'Tricalcium_phosphate': {'DM%': None, 'CP%': None, 'CF%': None, 'Ca%': 38, 'P%': 19, 'ME': None, 'Lysine%': None, 'Methionine%': None, 'cost': 73.57}, 'Alfalfa_hay': {'DM%': 87.5, 'CP%': 18.9, 'CF%': 33.1, 'Ca%': None, 'P%': None, 'ME': None, 'Lysine%': None, 'Methionine%': None, 'cost': 22.22}, 'Sugarcane_bagasse': {'DM%': 90.5, 'CP%': 1.7, 'CF%': 50.3, 'Ca%': None, 'P%': None, 'ME': None, 'Lysine%': None, 'Methionine%': None, 'cost': 14.16}, 'Sesame_cake': {'DM%': 93, 'CP%': 36.1, 'CF%': 6.7, 'Ca%': None, 'P%': None, 'ME': None, 'Lysine%': None, 'Methionine%': None, 'cost': 60.38}, 'Sugarcane_tops': {'DM%': 33.5, 'CP%': 6.2, 'CF%': 29.5, 'Ca%': None, 'P%': None, 'ME': None, 'Lysine%': None, 'Methionine%': None, 'cost': 9.96}, 'Whey': {'DM%': 90, 'CP%': 13.0, 'CF%': 1.3, 'Ca%': 0.97, 'P%': 0.76, 'ME': 3100, 'Lysine%': None, 'Methionine%': 0.2, 'cost': 18.03}}
das={}
for ingredient, values in data.items():
    nut={}  
    for nutrient, value in values.items():
        nut[nutrient.lower()] = check(value)
    das[ingredient.lower()]=nut
   
for ingredient, nutrients in das.items():
    data={ingredient:nutrients}
    feed_instance = Feed(ingridient_batch=data)
    feed_instance.save()

