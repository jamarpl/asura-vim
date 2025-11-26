import json

with open("/home/jamar/Documents/Scripts/AsuraScrape/recent_chapters.json", "r") as f:
    series = json.loads(f.read());
    
    max_length = max(len(series[k]) for k in series)
    for key in series:
        print(f'{series[key].ljust(max_length)} {key.ljust(max_length+20)}')
