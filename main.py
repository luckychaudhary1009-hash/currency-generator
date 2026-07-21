import requests

def convert_currency(amount, from_currency, to_currency):
    # Using a free, no-key-required exchange rate API
    url = f"https://open.er-api.com/v6/latest/{from_currency.upper()}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["result"] == "success":
            rates = data["rates"]
            if to_currency.upper() in rates:
                exchange_rate = rates[to_currency.upper()]
                converted_amount = amount * exchange_rate
                return converted_amount
            else:
                return f"Error: Currency '{to_currency}' not found."
        else:
            return "Error: Unable to fetch data from the API."
            
    except Exception as e:
        return f"An error occurred: {e}"

# Test it out!
if __name__ == "__main__":
    print("--- Currency Converter ---")
    amt = float(input("Enter amount: "))
    from_curr = input("From currency (e.g., USD): ")
    to_curr = input("To currency (e.g., EUR, INR): ")
    
    result = convert_currency(amt, from_curr, to_curr)
    print(f"\n{amt} {from_curr.upper()} is equal to: {result} {to_curr.upper()}")