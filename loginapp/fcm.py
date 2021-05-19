import requests


url = "https://fcm.googleapis.com/fcm/send"

payload="{\n    \"to\": \"doTymDK-FUU:APA91bEavso8L1txtIWHlYBnZ36yuX0gEn_mjF2XhcXIOTPP-jY1GgK6ZZsUsmVnLNWuwDVyzSI8cA4ImjfmENL-0WwNTE07wRPCvVPEDnaz7sXXt-4GVDyADs-hf6HpyNcPOCfWcP4X\",\n    \"priority\": \"high\",\n    \"data\": {\n        \"title\": \"FG Title\",\n        \"body\": \"Foreground Message\",\n        \"extra\": \"extraData\"\n    }\n}"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'key=AAAALUAVmVA:APA91bEIlGyaOV54J0MzUgNClZPbEnFy3ip0DMQQnRwRmZ1DxMBLAspsP5ZZcH3Uw_px5hC5R6gDGOj52WMT5fjkI16PUu_T9URudbdukO4pGt9NwxkZniVK-prFBk1Dj00ylVr6rHEJ'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)