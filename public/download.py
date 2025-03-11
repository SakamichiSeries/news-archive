import requests
import json

# for group in ["nogizaka46", "keyakizaka46", "sakurazaka46", "hinatazaka46"]:

for y in range(2012, 2026):
    for m in range(1, 13):
        print(f"{y}{m:02d}")
        url = f"https://www.nogizaka46.com/s/s/api/json/news?dy={y}{m:02d}"
        with open(f"nogizaka46-{y}{m:02d}.json", "w") as f:
            print(url)
            temp = requests.get(url).json()
            for entry in temp["news"]:
                entry["link"] = (
                    f"https://www.nogizaka46.com/s/n46/news/detail/{entry['code']}"
                )
            json.dump(temp, f, ensure_ascii=False, indent=2)

for y in range(2015, 2026):
    for m in range(1, 13):
        print(f"{y}{m:02d}")
        url = f"https://www.keyakizaka46.com/s/k46o/api/json/news?dy={y}{m:02d}"
        with open(f"keyakizaka46-{y}{m:02d}.json", "w") as f:
            print(url)
            temp = requests.get(url).json()
            for entry in temp["news"]:
                entry["link"] = (
                    f"https://www.keyakizaka46.com/s/k46o/news/detail/{entry['code']}"
                )
            json.dump(temp, f, ensure_ascii=False, indent=2)

for y in range(2020, 2026):
    for m in range(1, 13):
        print(f"{y}{m:02d}")
        url = f"https://www.sakurazaka46.com/s/s46/api/json/news?dy={y}{m:02d}"
        with open(f"sakurazaka46-{y}{m:02d}.json", "w") as f:
            print(url)
            temp = requests.get(url).json()
            for entry in temp["news"]:
                entry["link"] = (
                    f"https://sakurazaka46.com/s/s46/news/detail/{entry['code']}"
                )
            json.dump(temp, f, ensure_ascii=False, indent=2)

for y in range(2019, 2026):
    for m in range(1, 13):
        print(f"{y}{m:02d}")
        url = f"https://www.hinatazaka46.com/s/official/api/json/news?dy={y}{m:02d}"
        with open(f"hinatazaka46-{y}{m:02d}.json", "w") as f:
            print(url)
            temp = requests.get(url).json()
            for entry in temp["news"]:
                entry["link"] = (
                    f"https://www.hinatazaka46.com/s/official/news/detail/{entry['code']}"
                )
            json.dump(temp, f, ensure_ascii=False, indent=2)
