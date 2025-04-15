import json

tag_set = set()
print(tag_set)
tag_set.add("test")
print(tag_set)
for y in range(2010, 2026):
    for m in range(1, 13):
        for group in ["Nogizaka46", "Keyakizaka46", "Hinatazaka46", "Sakurazaka46"]:
            try:
                data = {}
                with open(f"{group}-{y}{m:02d}.json", "r") as f:
                    data = json.load(f)
                for entry in data["news"]:
                    if "tags" in entry:
                        # print(entry["tags"])
                        for tag in entry["tags"]:
                            tag_set.add(tag)

                            if str(int(tag)) != tag and ("0" + str(int(tag))) != tag:
                                print(entry["tags"])

            except Exception as e:
                # print(e)
                pass

print(tag_set)
