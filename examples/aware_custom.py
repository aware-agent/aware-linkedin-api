from linkedin_api import Linkedin

import json

with open("credentials.json", "r") as f:
    credentials = json.load(f)

if credentials:
    linkedin = Linkedin(credentials["username"], credentials["password"])

    profile = linkedin.get_profile("nzlz")
    print("NESTOR PROFILE: ", profile)
    profile["contact_info"] = linkedin.get_profile_contact_info(
        "nzlz"
    )
    connections = linkedin.get_profile_connections(profile["profile_id"])
    # Drop connection in a .txt
    with open("connections.txt", "w") as f:
        for connection in connections:
            f.write(f"{connection}\n")
    # send a message
    response = linkedin.send_message(
        message_body="Hello Nestor, this is an automated message for our app.",
        recipients=[profile["profile_id"]],
    )
    print(f"Message sent: {response}")
    result = linkedin.share_post("Hello World. This is Aware!")
    print(f"Post shared: {result}")
