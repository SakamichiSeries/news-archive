import requests
import json

# for group in ["nogizaka46", "keyakizaka46", "sakurazaka46", "hinatazaka46"]:
for y in range(2010, 2025):
    for m in range(1, 13):
        print(f"{y}{m:02d}")
        url = f"https://www.nogizaka46.com/s/s/api/json/news?dy={y}{m:02d}"
        with open(f"nogizaka46-{y}{m:02d}.json", "w") as f:
            print(url)
            json.dump(requests.get(url).json(), f, ensure_ascii=False, indent=2)

for y in range(2012, 2025):
    for m in range(1, 13):
        print(f"{y}{m:02d}")
        url = f"https://www.keyakizaka46.com/s/k46o/api/json/news?dy={y}{m:02d}"
        with open(f"keyakizaka46-{y}{m:02d}.json", "w") as f:
            print(url)
            json.dump(requests.get(url).json(), f, ensure_ascii=False, indent=2)

for y in range(2018, 2025):
    for m in range(1, 13):
        print(f"{y}{m:02d}")
        url = f"https://www.sakurazaka46.com/s/s46/api/json/news?dy={y}{m:02d}"
        with open(f"sakurazaka46-{y}{m:02d}.json", "w") as f:
            print(url)
            json.dump(requests.get(url).json(), f, ensure_ascii=False, indent=2)

for y in range(2018, 2025):
    for m in range(1, 13):
        print(f"{y}{m:02d}")
        url = f"https://www.hinatazaka46.com/s/official/api/json/news?dy={y}{m:02d}"
        with open(f"hinatazaka46-{y}{m:02d}.json", "w") as f:
            print(url)
            json.dump(requests.get(url).json(), f, ensure_ascii=False, indent=2)
