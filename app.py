import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="Fiza's Coffee Café", page_icon="☕", layout="wide")

st.markdown("""
<style>
    .stApp { background: linear-gradient(180deg,#FFF8F0,#FFF7EE); }
    .card { padding: 18px; border-radius:18px; background: #fff; box-shadow: 0 6px 20px rgba(0,0,0,0.06); }
    .title { color:#6F4E37; font-weight:800; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>☕ Fiza's Premium Coffee Café</h1>", unsafe_allow_html=True)
st.write("Choose a drink and place your order!")

menu = {
    "Coffee": 200,
    "Latte": 350,
    "Cappuccino": 300,
    "Mocha": 400,
    "Hot Chocolate": 250,
    "Cold Coffee": 330,
    "Espresso": 270
}

images = {
    "Coffee": "https://i.imgur.com/5v0zR9L.png",
    "Latte": "https://i.imgur.com/QYxgUoN.png",
    "Cappuccino": "https://i.imgur.com/0QJZQ6n.png",
    "Mocha": "https://i.imgur.com/5v0zR9L.png",
    "Hot Chocolate": "https://i.imgur.com/uX2Jxjw.png",
    "Cold Coffee": "https://i.imgur.com/bQ6R2fU.png",
    "Espresso": "https://i.imgur.com/jvK7t4x.png"
}

st.sidebar.header("Customize your order")
name = st.sidebar.text_input("Name")
selected = st.sidebar.selectbox("Drink", list(menu.keys()))
qty = st.sidebar.number_input("Quantity", 1, 10)

price = menu[selected]
total = price * qty

col1, col2 = st.columns([1,1])

with col1:
    st.image(images[selected], width=300)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader(f"{selected} — Rs. {price}")
    st.write(f"Quantity: {qty}")
    st.write(f"Total: Rs. {total}")
    
    if st.button("Place Order"):
        st.success("Order placed!")
        st.write(f"Name: {name}")
        st.write(f"Drink: {selected}")
        st.write(f"Quantity: {qty}")
        st.write(f"Total: Rs. {total}")

    st.markdown("</div>", unsafe_allow_html=True)
