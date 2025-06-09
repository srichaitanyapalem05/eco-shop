import streamlit as st

PRODUCTS = [
    {
        "name": "Shampoo Bottle",
        "price": 18.49,
        "eco": False,
        "emoji": "🧴",
        "alt": {"name": "Flutter Refill Shampoo", "price": 15.97},
    },
    {
        "name": "All-Purpose Cleaner",
        "price": 4.29,
        "eco": True,
        "emoji": "🧼",
        "alt": None,
    },
    {
        "name": "Plastic Water Bottle",
        "price": 2.49,
        "eco": False,
        "emoji": "🥤",
        "alt": {"name": "Reusable Steel Bottle", "price": 12.99},
    },
    {
        "name": "Bamboo Toothbrush",
        "price": 3.99,
        "eco": True,
        "emoji": "🎋",
        "alt": None,
    },
    {
        "name": "Leather Wallet",
        "price": 39.99,
        "eco": False,
        "emoji": "👛",
        "alt": {"name": "Cork Wallet", "price": 29.99},
    },
    {
        "name": "Organic Cotton Shirt",
        "price": 25.00,
        "eco": True,
        "emoji": "👕",
        "alt": None,
    },
    {
        "name": "Plastic Bag Pack",
        "price": 1.99,
        "eco": False,
        "emoji": "🛍️",
        "alt": {"name": "Reusable Tote Bag", "price": 3.49},
    },
    {
        "name": "Refillable Soap Pouch",
        "price": 6.50,
        "eco": True,
        "emoji": "🧴",
        "alt": None,
    },
    {
        "name": "Paper Towels",
        "price": 3.75,
        "eco": False,
        "emoji": "🧻",
        "alt": {"name": "Reusable Cloth Towels", "price": 8.50},
    },
    {
        "name": "LED Light Bulb",
        "price": 5.25,
        "eco": True,
        "emoji": "💡",
        "alt": None,
    },
]

if "cart" not in st.session_state:
    st.session_state.cart = {}

def add_to_cart(name):
    st.session_state.cart[name] = st.session_state.cart.get(name, 0) + 1

def calculate_ecopoints():
    points = 0
    for name, qty in st.session_state.cart.items():
        product = next(p for p in PRODUCTS if p["name"] == name)
        if product["eco"]:
            points += qty * 10
    return points

def sustainability_score():
    total = 0
    eco_count = 0
    for name, qty in st.session_state.cart.items():
        p = next(p for p in PRODUCTS if p["name"] == name)
        total += qty
        if p["eco"]:
            eco_count += qty
    return round((eco_count / total) * 100) if total > 0 else 0

# UI
st.set_page_config(page_title="EcoCart+", page_icon="🛒", layout="centered")
st.markdown("## 🛍️ EcoCart+")

# Score
score = sustainability_score()
st.markdown(f"### ♻️ Sustainability Score: **{score} / 100**")

# Suggestions
for name, qty in st.session_state.cart.items():
    product = next(p for p in PRODUCTS if p["name"] == name)
    if not product["eco"] and product["alt"]:
        alt = product["alt"]
        st.markdown("---")
        st.markdown("#### 🌱 Try this eco-friendlier alternative:")
        st.image("https://via.placeholder.com/80", width=80)  # Placeholder image
        st.write(f"**{alt['name']}** - ${alt['price']}")
        if st.button(f"Swap for {alt['name']}", key=f"swap_{name}"):
            del st.session_state.cart[name]
            add_to_cart(alt["name"])

# Cart
st.markdown("---")
st.markdown("### 🧾 Your Cart")
total = 0
for product in PRODUCTS:
    name = product["name"]
    qty = st.session_state.cart.get(name, 0)
    if qty > 0:
        st.write(f"{product['emoji']} **{name}** x{qty} — ${product['price']*qty:.2f}")
        total += product["price"] * qty

ecopoints = calculate_ecopoints()
st.markdown("---")
st.markdown(f"✅ You have **{ecopoints} EcoPoints**")
st.markdown(f"### 💳 Total: **${total:.2f}**")
st.button("🛒 Checkout")

# Add products
st.markdown("---")
st.markdown("### ➕ Add More Products")
for product in PRODUCTS:
    if st.button(f"Add {product['emoji']} {product['name']}", key=product["name"]):
        add_to_cart(product["name"])
