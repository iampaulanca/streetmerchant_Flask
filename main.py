from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

configUpdate_dir = "/Users/paulancajima/desktop/configUpdate.py"
streetmerchant_dir = "/Users/paulancajima/Desktop/streetmerchant"

options = {"APNS_AUTHKEY": "",
           "APNS_BUNDLEID": "",
           "APNS_DEVICETOKEN": "",
           "APNS_KEYID": "",
           "APNS_PRODUCTION": "",
           "APNS_TEAMID": "",
           "ASCII_BANNER": "",
           "ASCII_COLOR": "",
           "AUTO_ADD_TO_CART": "",
           "BROWSER_TRUSTED": "",
           "DESKTOP_NOTIFICATIONS": "",
           "DISCORD_NOTIFY_GROUP": "",
           "DISCORD_NOTIFY_GROUP_3060": "",
           "DISCORD_NOTIFY_GROUP_3060TI": "",
           "DISCORD_NOTIFY_GROUP_3070": "",
           "DISCORD_NOTIFY_GROUP_3080": "",
           "DISCORD_NOTIFY_GROUP_3090": "",
           "DISCORD_NOTIFY_GROUP_CORSAIR_SF": "",
           "DISCORD_NOTIFY_GROUP_RX6800": "",
           "DISCORD_NOTIFY_GROUP_RX6800XT": "",
           "DISCORD_NOTIFY_GROUP_RX6900XT": "",
           "DISCORD_NOTIFY_GROUP_RYZEN5600": "",
           "DISCORD_NOTIFY_GROUP_RYZEN5800": "",
           "DISCORD_NOTIFY_GROUP_RYZEN5900": "",
           "DISCORD_NOTIFY_GROUP_RYZEN5950": "",
           "DISCORD_NOTIFY_GROUP_SONYPS5C": "",
           "DISCORD_NOTIFY_GROUP_SONYPS5DE": "",
           "DISCORD_NOTIFY_GROUP_XBOXSX": "",
           "DISCORD_NOTIFY_GROUP_XBOXSS": "",
           "DISCORD_NOTIFY_GROUP_TEST": "",
           "DISCORD_WEB_HOOK": "",
           "EMAIL_PASSWORD": "",
           "EMAIL_TO": "",
           "EMAIL_USERNAME": "",
           "HEADLESS": "",
           "IN_STOCK_WAIT_TIME": "",
           "LOG_LEVEL": "",
           "LOW_BANDWIDTH": "",
           "MAX_PRICE_SERIES_3060": "",
           "MAX_PRICE_SERIES_3060TI": "",
           "MAX_PRICE_SERIES_3070": "",
           "MAX_PRICE_SERIES_3080": "",
           "MAX_PRICE_SERIES_3090": "",
           "MAX_PRICE_SERIES_CORSAIR_SF": "",
           "MAX_PRICE_SERIES_RX6800": "",
           "MAX_PRICE_SERIES_RX6800XT": "",
           "MAX_PRICE_SERIES_RX6900XT": "",
           "MAX_PRICE_SERIES_RYZEN5600": "",
           "MAX_PRICE_SERIES_RYZEN5800": "",
           "MAX_PRICE_SERIES_RYZEN5900": "",
           "MAX_PRICE_SERIES_RYZEN5950": "",
           "MAX_PRICE_SERIES_SONYPS5C": "",
           "MAX_PRICE_SERIES_SONYPS5DE": "",
           "MAX_PRICE_SERIES_XBOXSS": "",
           "MAX_PRICE_SERIES_XBOXSX": "",
           "MAX_PRICE_SERIES_TEST": "",
           "MICROCENTER_LOCATION": "",
           "MQTT_BROKER_ADDRESS": "",
           "MQTT_BROKER_PORT": "",
           "MQTT_CLIENT_ID": "",
           "MQTT_PASSWORD": "",
           "MQTT_QOS": "",
           "MQTT_TOPIC": "",
           "MQTT_USERNAME": "",
           "OPEN_BROWSER": "",
           "PAGE_BACKOFF_MIN": "",
           "PAGE_BACKOFF_MAX": "",
           "PAGE_SLEEP_MIN": "",
           "PAGE_SLEEP_MAX": "",
           "PAGE_TIMEOUT": "",
           "PAGERDUTY_INTEGRATION_KEY": "",
           "PAGERDUTY_SEVERITY": "",
           "PHILIPS_HUE_API_KEY": "",
           "PHILIPS_HUE_CLOUD_ACCESS_TOKEN": "",
           "PHILIPS_HUE_CLOUD_CLIENT_ID": "",
           "PHILIPS_HUE_CLOUD_CLIENT_SECRET": "",
           "PHILIPS_HUE_CLOUD_REFRESH_TOKEN": "",
           "PHILIPS_HUE_LAN_BRIDGE_IP": "",
           "PHILIPS_HUE_LIGHT_COLOR": "",
           "PHILIPS_HUE_LIGHT_IDS": "",
           "PHILIPS_HUE_LIGHT_PATTERN": "",
           "PHONE_CARRIER": "",
           "PHONE_NUMBER": "",
           "PLAY_SOUND": "",
           "PROXY_ADDRESS": "",
           "PROXY_PROTOCOL": "",
           "PROXY_PORT": "",
           "PUSHBULLET": "",
           "PUSHOVER_EXPIRE": "",
           "PUSHOVER_RETRY": "",
           "PUSHOVER_TOKEN": "",
           "PUSHOVER_USER": "",
           "PUSHOVER_PRIORITY": "",
           "RESTART_TIME": "",
           "SCREENSHOT": "",
           "SHOW_ONLY_BRANDS": "",
           "SHOW_ONLY_MODELS": "",
           "SHOW_ONLY_SERIES": "",
           "SLACK_CHANNEL": "",
           "SLACK_TOKEN": "",
           "SMARTTHINGS_TOKEN": "",
           "SMARTTHINGS_SWITCH_LABEL": "",
           "SMTP_ADDRESS": "",
           "SMTP_PORT": "",
           "STORES": "",
           "TELEGRAM_ACCESS_TOKEN": "",
           "TELEGRAM_CHAT_ID": "",
           "TWILIO_ACCOUNT_SID": "",
           "TWILIO_AUTH_TOKEN": "",
           "TWILIO_FROM_NUMBER": "",
           "TWILIO_TO_NUMBER": "",
           "TWITCH_ACCESS_TOKEN": "",
           "TWITCH_CHANNEL": "",
           "TWITCH_CLIENT_ID": "",
           "TWITCH_CLIENT_SECRET": "",
           "TWITCH_REFRESH_TOKEN": "",
           "TWITTER_ACCESS_TOKEN_KEY": "",
           "TWITTER_ACCESS_TOKEN_SECRET": "",
           "TWITTER_CONSUMER_KEY": "",
           "TWITTER_CONSUMER_SECRET": "",
           "TWITTER_TWEET_TAGS": "",
           "STREAMLABS_ACCESS_TOKEN": "",
           "STREAMLABS_TYPE": "",
           "STREAMLABS_IMAGE": "",
           "STREAMLABS_SOUND": "",
           "STREAMLABS_DURATION": "",
           "WEB_PORT": ""}


@app.route('/', methods=['GET'])
def hello_world():
    return "hello world"


@app.route('/getConfig', methods=['GET'])
def get_config():
    os.system(f'python3 getConfig.py')
    return "hello world"


@app.route('/updateConfig', methods=['POST'])
def update_config():
    if request.method == 'POST':
        data = request.json
    os.system(f'python3 configUpdate.py "{data}"')
    os.system(f"kill -9 $(pgrep -f '{streetmerchant_dir}')")
    subprocess.Popen(["npm", "start"], cwd=f"{streetmerchant_dir}", stdout=subprocess.DEVNULL)
    return jsonify(data)


@app.route('/killScript', methods=['GET'])
def kill_script():
    os.system(f"kill -9 $(pgrep -f '{streetmerchant_dir}')")
    return "Street merchant has been murdered"


if __name__ == '__main__':
    app.run()
