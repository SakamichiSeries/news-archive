import requests
import json
import datetime
import re
import random
import os
import time


def sort_key(x):
    try:
        return (0, int(x))
    except ValueError:
        return (1, x)


def _send_part(part, channel_id, bot_token):
    max_retries = 5
    for attempt in range(max_retries):
        try:
            payload = {
                "chat_id": channel_id,
                "text": part,
                "link_preview_options": {"is_disabled": True},
            }
            response = requests.post(
                f"https://api.telegram.org/bot{bot_token}/sendMessage",
                headers={"Content-Type": "application/json"},
                json=payload,
            )
            resp_json = response.json()
            if response.ok:
                print(resp_json)
                return resp_json["result"]["message_id"]
            else:
                raise Exception(resp_json.get("description", "Unknown error"))
        except Exception as e:
            print(f"Error: {e}")
            if attempt < max_retries - 1:
                time.sleep(10)
    print(f"Failed to send part after {max_retries} retries")
    return None


def send_telegram_message(msg, channel_id, bot_token):
    MAX_LENGTH = 3000
    parts = msg.split("\n")
    current_part = ""
    message_ids = []
    for part in parts:
        if len(current_part) + len(part) + 1 > MAX_LENGTH:
            if current_part:
                mid = _send_part(current_part, channel_id, bot_token)
                if mid:
                    message_ids.append(mid)
            current_part = part
        else:
            current_part += ("\n" if current_part else "") + part
    if current_part:
        mid = _send_part(current_part, channel_id, bot_token)
        if mid:
            message_ids.append(mid)
    return message_ids[0] if message_ids else None


def scrape(y, m, group, current_y, current_m, bot_token, channels, channel_usernames):
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

        filename = f"{group}-{y}{m:02d}.json"
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

        is_current = y == current_y and m == current_m
        if is_current:
            old_data = {}
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    old_data = json.load(f)
            old_codes = {entry["code"] for entry in old_data.get("news", [])}
            new_entries = [
                entry for entry in temp["news"] if entry["code"] not in old_codes
            ]

            channel_id = channels.get(group)
            summary_channel_id = channels.get("summary")
            username = channel_usernames.get(group)
            if channel_id and new_entries:
                for entry in new_entries:
                    content = entry["content"]
                    text = re.sub(r"<img[^>]*>", "", content)
                    text = re.sub(r"<br\s*\/?>\s*", "\n", text)
                    text = re.sub(r"<[^>]+>", "", text)
                    text = re.sub(r"&[^;]+;", "", text)
                    text = re.sub(r"\n\s*\n", "\n", text).strip()
                    msg = f"{group} news: {entry['title']}\n{text}\n{entry['link']}"
                    message_id = send_telegram_message(msg, channel_id, bot_token)
                    if message_id and summary_channel_id and username:
                        tg_link = f"https://t.me/{username}/{message_id}"
                        summary_msg = f"{entry['title']} {tg_link}"
                        send_telegram_message(
                            summary_msg, summary_channel_id, bot_token
                        )

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(temp, f, ensure_ascii=False, indent=2)

    except Exception as e:
        print(e)
        pass


y = current_y = datetime.datetime.now().year
m = current_m = datetime.datetime.now().month
random_number = random.randint(0, 20051031)

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
channels = {
    "Nogizaka46": os.getenv("TELEGRAM_NOGI_CHANNEL"),
    "Keyakizaka46": os.getenv("TELEGRAM_NEWS_CHANNEL"),
    "Hinatazaka46": os.getenv("TELEGRAM_HINA_CHANNEL"),
    "Sakurazaka46": os.getenv("TELEGRAM_SAKU_CHANNEL"),
    "summary": os.getenv("TELEGRAM_NEWS_CHANNEL"),
}
channel_usernames = {
    "Nogizaka46": "Nogizaka46_News",
    "Keyakizaka46": "Keyakizaka46_News",
    "Hinatazaka46": "Hinatazaka46_News",
    "Sakurazaka46": "Sakurazaka46_News",
}

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
            scrape(
                y,
                m,
                group,
                current_y,
                current_m,
                bot_token,
                channels,
                channel_usernames,
            )
            if random_number > 46:
                break
        else:
            continue
        break
