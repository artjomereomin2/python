import json
data = {
    "president": {
        "Фамилия": "Путин",
        "Страна": "Россия"
    }
}
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)