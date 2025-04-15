import requests
import json
import datetime
import re
import random


def sort_key(x):
    try:
        return (0, int(x))  # 可以转换为int的，优先级高，按int值排序
    except ValueError:
        return (1, x)  # 不能转换为int的，按字符串排序


scrape_all = False if random.randint(0, 1031) > 46 else True

y = current_y = datetime.datetime.now().year
m = current_m = datetime.datetime.now().month
for group in ["Nogizaka46", "Keyakizaka46", "Hinatazaka46", "Sakurazaka46"]:
    match group:
        case "Nogizaka46":
            start = 2012
        case "Keyakizaka46":
            start = 2015
        case "Hinatazaka46":
            start = 2019
        case "Sakurazaka46":
            start = 2020

    for y in range(current_y, start - 1, -1):
        for m in range(current_m if y == current_y else 12, 0, -1):
            try:
                print(f"{y}{m:02d}")
                match group:
                    case "Nogizaka46":
                        code = f"n46"
                    case "Keyakizaka46":
                        code = f"k46o"
                    case "Hinatazaka46":
                        code = f"official"
                    case "Sakurazaka46":
                        code = f"s46"
                url = f"http://mobile-ssl.com/s/{code}/api/json/news?dy={y}{m:02d}"

                with open(f"{group}-{y}{m:02d}.json", "w") as f:
                    print(url)
                    temp = requests.get(url).json()
                    for entry in temp["news"]:
                        match group:
                            case "Nogizaka46":
                                entry["link"] = (
                                    f"https://www.nogizaka46.com/s/n46/news/detail/{entry['code']}"
                                )
                            case "Keyakizaka46":
                                entry["link"] = (
                                    f"https://www.keyakizaka46.com/s/k46o/news/detail/{entry['code']}"
                                )
                            case "Hinatazaka46":
                                entry["link"] = (
                                    f"https://www.hinatazaka46.com/s/official/news/detail/{entry['code']}"
                                )
                            case "Sakurazaka46":
                                entry["link"] = (
                                    f"https://sakurazaka46.com/s/s46/news/detail/{entry['code']}"
                                )

                        entry["content"] = re.sub(r"\?ima=\d{4}", "", entry["content"])
                        if "tags" in entry:
                            entry["tags"] = sorted(entry["tags"], key=sort_key)
                    json.dump(temp, f, ensure_ascii=False, indent=2)

            except Exception as e:
                print(e)
                pass
