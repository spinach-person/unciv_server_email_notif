import json
import sys

# The player ID to find the email for is the first argument.
player_id_to_match = sys.argv[1]
player_id_email_json = "./email_info/player_id_emails.json"

with open(player_id_email_json, "rt") as file:
    json_data = json.load(file)

id_list = json_data["player-id-list"]

for item in id_list:
    if item["id"] == player_id_to_match:
        print(item["email"])
        quit()

print("No email found")
