import requests

response = requests.get("https://coinmarketcap.com/")

response_text = response.text

response_parse = response_text.split("<span>")

coins = []

for item in response_parse:
    if item.startswith("$"):
        for coin_item in item.split("</span>"):
            if coin_item.startswith("$") and  coin_item[1].isdigit():
                coins.append(coin_item)

print(coins)
print("Coin exchange rate -", coins[0])

bitcoin = int(input("How much bitcoins do you have? "))

bitcoin_str = coins[0][1:]
bitcoin_rate = float(bitcoin_str.replace(",", ""))

print("You have: $", bitcoin * bitcoin_rate)