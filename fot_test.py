import json

with open("7_wonders.json") as f:
    wonders = json.load(f)

wonders.append({'where': 'ВКИ', 'what': 'Ну типа'})

for wonder in wonders:
    print(wonder['what'])

with open("7_wonders.json", "w") as f:
    json.dump(wonders, f, indent=4, ensure_ascii=False)
