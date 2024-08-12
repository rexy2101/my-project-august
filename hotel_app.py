import streamlit as st


rooms = {
    "101": {"type": "Deluxe", "price": 100},
    "102": {"type": "Standard", "price": 80},
    "103": {"type": "Deluxe", "price": 100}
}

def main():
    st.title("Hotel Management System")


    if st.button("Home"):
        name = st.button("Hotel ha bhai")


    if st.button("Book a Room"):
        name = st.text_input("Name")
        checkin = st.date_input("Check-in")
        checkout = st.date_input("Check-out")
        room_type = st.selectbox("Room Type", ["Deluxe", "Standard"])

        if st.button("Book"):

            available_rooms = [room for room, details in rooms.items() if details["type"] == room_type]
            if available_rooms:
                room_number = available_rooms[0]
                st.success(f"Room {room_number} booked for {name} from {checkin} to {checkout}")
            else:
                st.error("No rooms available of the selected type")


    if st.button("Check Availability"):
        checkin = st.date_input("Check-in")
        checkout = st.date_input("Check-out")
        room_type = st.selectbox("Room Type", ["Deluxe", "Standard"])


        available_rooms = [room for room, details in rooms.items() if details["type"] == room_type]
        if available_rooms:
            st.success(f"{len(available_rooms)} rooms of type {room_type} available")
        else:
            st.error("No rooms available of the selected type")


    if st.button("View Room Details"):
        for room_number, details in rooms.items():
            st.write(f"Room {room_number}: {details['type']} - ${details['price']}/night")

if __name__ == "__main__":
    main()
