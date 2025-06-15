# Crypto database
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

# CryptoBuddy’s voice
def greet():
    print("Hey there! I'm CryptoBuddy. Ask me about trends or sustainability, and I’ll help you invest smarter!")

# Main chatbot function
def chatbot():
    greet()
    while True:
        user_query = input("\nYou: ").lower()

        if "exit" in user_query or "bye" in user_query:
            print("CryptoBuddy: Catch you later! Remember: crypto is risky—do your own research!")
            break

        elif "trending" in user_query or "rising" in user_query:
            trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
            print(f"CryptoBuddy: These coins are trending up: {', '.join(trending)}")

        elif "sustainable" in user_query or "eco" in user_query:
            best = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            print(f"CryptoBuddy: Go for {best}! 🌱 It’s eco-friendly and has long-term potential.")

        elif "long-term" in user_query or "growth" in user_query:
            for coin, data in crypto_db.items():
                if data["price_trend"] == "rising" and data["market_cap"] == "high":
                    print(f"CryptoBuddy: {coin} is profitable and has great momentum! ")
                    break

        else:
            print("CryptoBuddy: Hmm... I didn’t catch that. Try asking about trending or sustainable cryptos!")

# To run the chatbot
chatbot()
