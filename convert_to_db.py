import json
import datetime
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "gmaps_timeline_analysis.settings")

import django
django.setup()
from osm_view.models import Location, Activity

with file('data/2018-02-06-takeout.json') as f:
    raw = f.read()

json_data = json.loads(raw)

for i in json_data['locations']:
    longitude = i['longitudeE7']/1e7
    latitude = i['latitudeE7']/1e7
    t = i['timestampMs']
    # TODO support time zone awareness
    time = datetime.datetime.fromtimestamp(float(t)/1e3)
    location = Location(timestamp=time, lon=longitude, lat=latitude)
    location.save()
    if 'accuracy' in i:
        location.accuracy = i['accuracy']
    if 'verticalAccuracy' in i:
        location.verticalAccuracy = i['verticalAccuracy']
    if 'velocity' in i:
        location.velocity = i['velocity']
    if 'altitude' in i:
        location.altitude = i['altitude']
    if 'heading' in i:
        location.heading = i['heading']
    if 'activity' in i:
        for activities in i['activity']:
            for activity in activities['activity']:
                a = Activity()
                if 'confidence' in activity:
                    a.confidence = activity['confidence']
                if 'activity_type' in activity:
                    a.activity_type = activity['activity_type']
                a.save()
                location.activity.add(a)
                location.save()
