import streamlit as st

# Sample products data: name, price, eco-friendly?
PRODUCTS = [
    {"name": "Organic Cotton Shirt", "price": 25, "eco": True},
    {"name": "Plastic Bottle", "price": 5, "eco": False},
    {"name": "Bamboo Toothbrush", "price": 3, "eco": True},
    {"name": "Leather Wallet", "price": 45, "eco": False},
    {"name": "Reusable Shopping Bag", "price": 2, "eco": True},
]

# Initialize cart in session state
if "cart" not in st.session_state:
    st.session_state.cart = {}

def add_to_cart(product_name):
    if product_name in st.session_state.cart:
        st.session_state.cart[product_name] += 1
    else:
        st.session_state.cart[product_name] = 1

def remove_from_cart(product_name):
    if product_name in st.session_state.cart:
        if st.session_state.cart[product_name] > 1:
            st.session_state.cart[product_name] -= 1
        else:
            del st.session_state.cart[product_name]

def calculate_total():
    total = 0
    for item, qty in st.session_state.cart.items():
        price = next(p["price"] for p in PRODUCTS if p["name"] == item)
        total += price * qty
    return total

def calculate_ecopoints():
    points = 0
    for item, qty in st.session_state.cart.items():
        eco = next(p["eco"] for p in PRODUCTS if p["name"] == item)
        if eco:
            points += 10 * qty  # 10 eco points per eco-friendly item
    return points

st.title("🌿 Eco-Friendly Shop Demo")

st.header("Available Products")
cols = st.columns(len(PRODUCTS))
for idx, product in enumerate(PRODUCTS):
    with cols[idx]:
        st.write(f"**{product['name']}**")
        st.write(f"Price: ${product['price']}")
        st.write("🌱 Eco-friendly" if product['eco'] else "❌ Not eco-friendly")
        if st.button(f"Add to Cart", key=f"add_{idx}"):
            add_to_cart(product['name'])

st.header("Your Cart")
if not st.session_state.cart:
    st.write("Cart is empty.")
else:
    for item, qty in st.session_state.cart.items():
        st.write(f"{item} x {qty}  ", end="")
        if st.button(f"➖ Remove one", key=f"remove_{item}"):
            remove_from_cart(item)

total_price = calculate_total()
st.write(f"**Total Price:** ${total_price}")

ecopoints = calculate_ecopoints()
st.write(f"🌟 **EcoPoints Earned:** {ecopoints}")

st.header("Suggestions for You")
# Suggest products not in cart
suggestions = [p for p in PRODUCTS if p["name"] not in st.session_state.cart]
for s in suggestions:
    st.write(f"- {s['name']} (${s['price']}) {'🌱' if s['eco'] else ''}")

