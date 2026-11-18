import json
data = {"group": "T118","checked": 2}
with open("ekeb_21.json", "w", encoding = "utf-8") as file:
    json.dump(data, file, ensure_ascii= False,indent=4)

with open("ekeb_21.json", "r", encoding = "utf-8") as file:  #превращаем файл снова в словарь
    json.load(file)
print(data["group"])
print(data["checked"] + 1)