import requests
import json
import datetime
import re

y = datetime.datetime.now().year
m = datetime.datetime.now().month

try:
    print(f"{y}{m:02d}")
    url = f"https://www.nogizaka46.com/s/s/api/json/news?dy={y}{m:02d}"
    with open(f"Nogizaka46-{y}{m:02d}.json", "w") as f:
        print(url)
        temp = requests.get(url).json()
        for entry in temp["news"]:
            entry["link"] = (
                f"https://www.nogizaka46.com/s/n46/news/detail/{entry['code']}"
            )
            entry["content"] = re.sub(r"\?ima=\d{4}", "", entry["content"])
        json.dump(temp, f, ensure_ascii=False, indent=2)

    print(f"{y}{m:02d}")
    url = f"https://www.keyakizaka46.com/s/k46o/api/json/news?dy={y}{m:02d}"
    with open(f"Keyakizaka46-{y}{m:02d}.json", "w") as f:
        print(url)
        temp = requests.get(url).json()
        for entry in temp["news"]:
            entry["link"] = (
                f"https://www.keyakizaka46.com/s/k46o/news/detail/{entry['code']}"
            )
            entry["content"] = re.sub(r"\?ima=\d{4}", "", entry["content"])
        json.dump(temp, f, ensure_ascii=False, indent=2)

    print(f"{y}{m:02d}")
    url = f"https://www.sakurazaka46.com/s/s46/api/json/news?dy={y}{m:02d}"
    with open(f"Sakurazaka46-{y}{m:02d}.json", "w") as f:
        print(url)
        temp = requests.get(url).json()
        for entry in temp["news"]:
            entry["link"] = (
                f"https://sakurazaka46.com/s/s46/news/detail/{entry['code']}"
            )
            entry["content"] = re.sub(r"\?ima=\d{4}", "", entry["content"])
        json.dump(temp, f, ensure_ascii=False, indent=2)

    print(f"{y}{m:02d}")
    url = f"https://www.hinatazaka46.com/s/official/api/json/news?dy={y}{m:02d}"
    with open(f"Hinatazaka46-{y}{m:02d}.json", "w") as f:
        print(url)
        temp = requests.get(url).json()
        for entry in temp["news"]:
            entry["link"] = (
                f"https://www.hinatazaka46.com/s/official/news/detail/{entry['code']}"
            )
            entry["content"] = re.sub(r"\?ima=\d{4}", "", entry["content"])
        json.dump(temp, f, ensure_ascii=False, indent=2)

except Exception as e:
    print(e)
    pass
