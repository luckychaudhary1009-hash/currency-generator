import streamlit as st
import requests

st.set_page_config(page_title="Currency Converter", page_icon="💱")

st.title("💱 Currency Converter")

# Fetch exchange rates
@st.cache_data(ttl=3600)
def get_rates(base="USD"):
    url = f"https://open.er-api.com/v6/latest/{base}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["result"] == "success":
            return data["rates"]
    return None

rates = get_rates()

if rates:
    currencies = sorted(rates.keys())

    amount = st.number_input(
        "Enter Amount",
        min_value=0.0,
        value=1.0,
        step=1.0
    )

    from_currency = st.selectbox("From Currency", currencies, index=currencies.index("USD"))
    to_currency = st.selectbox("To Currency", currencies, index=currencies.index("INR"))

    if st.button("Convert"):
        if from_currency == to_currency:
            result = amount
        else:
            usd_amount = amount / rates[from_currency]
            result = usd_amount * rates[to_currency]

        st.success(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")

else:
    st.error("Unable to fetch exchange rates.")

    import streamlit as st
from currency_converter import CurrencyConverter

st.title("💱 Currency Converter")

c = CurrencyConverter()

amount = st.number_input("Enter Amount", min_value=0.0, value=1.0)

currencies = c.currencies

from_currency = st.selectbox("From", currencies)
to_currency = st.selectbox("To", currencies)

if st.button("Convert", key="convert_button"):
    result = c.convert(amount, from_currency, to_currency)
    st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")