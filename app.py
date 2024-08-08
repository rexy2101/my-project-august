import streamlit as st

def main():
    st.title("Hotel Menu")
    menu = {
        "Burger": 5.99,
        "Pizza": 12.99,
        "Salad": 7.99,
        "Fries": 3.99,
        "Drink": 2.99}

    order = {}

    for item, price in menu.items():
        quantity = st.number_input(f"{item} (${price:.2f})", min_value=0)
        if quantity > 0:
            order[item] = quantity

    if order:
        total = sum(quantity * price for item, price in menu.items() for quantity in [order.get(item, 0)])
        st.subheader("Order Summary")
        for item, quantity in order.items():
            st.write(f"{quantity} x {item} = ${quantity * menu[item]:.2f}")
        st.write(f"Total: ${total:.2f}")

if __name__ == "__main__":
    main()
