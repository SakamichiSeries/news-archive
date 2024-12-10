import requests
import json

for y in range(2020, 2025):
    for m in range(1, 13):
        print(f"{y}{m:02d}")
        for group in ["nogizaka46", "keyakizaka46", "sakurazaka46", "hinatazaka46"]:
            url = f"https://www.{group}.com/s/s/api/json/news?dy={y}{m:02d}"
            with open(f"{group}-{y}{m:02d}.json", "w") as f:
                print(url)
                json.dump(requests.get(url).json(), f, ensure_ascii=False, indent=2)
