"""App file.

Main file that runs the app.

~ モーヴィシウス•と•アナイス"""

import streamlit as st
import pandas as pd
from data import CLASSROOMS_LIST
from logic import generate_qr_string, create_qr_image

# --- Initial settings ---
st.set_page_config(
    page_title="Classroom QR Generator",
    page_icon="☠️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- State Management for Session ---
# Initializes non-existent state
if "selected_room" not in st.session_state:
    st.session_state.selected_room = None
if "qr_data_string" not in st.session_state:
    st.session_state.qr_data_string = None


# --- Función para Resetear el Estado y Volver a la Página Principal ---
def reset_state():
    st.session_state.selected_room = None
    st.session_state.qr_data_string = None


# --- Page content, classroom selection ---
if st.session_state.selected_room is None:
    st.title("Classroom QR Generator")
    st.markdown("---")
    st.write("Selecciona un salon para generar "
             "el código QR de registro de asistencia.")

    # Convert classroom list as dataframe table
    df_classrooms = pd.DataFrame(CLASSROOMS_LIST)

    # Show table
    st.dataframe(df_classrooms, hide_index=True, use_container_width=True)

    st.markdown("---")
    st.subheader("Generate QR Code")

    # Classroom selector
    room_options = [
        f"{row['Building']} - {row['Room Number']}"
        for index,
        row in df_classrooms.iterrows()
    ]
    selected_option = st.selectbox("Choose a classroom:", room_options)

    # Configure classroom selection and QR generation
    if st.button("Generate QR"):
        if selected_option:
            # Get room number from selected option
            chosen_building, chosen_room_number = selected_option.split(" - ")

            # Search room code
            selected_room_data = next(
                (room for room in CLASSROOMS_LIST
                 if room["Building"] == chosen_building and room[
                     "Room Number"] == chosen_room_number),
                None
            )

            if selected_room_data:
                r_value_for_qr = selected_room_data["R_Value"]

                # Generate key-string
                final_qr_string = generate_qr_string(r_value_for_qr)

                # Save session state for next screen
                st.session_state.selected_room = chosen_room_number
                st.session_state.qr_data_string = final_qr_string
                st.rerun()  # Force page reloading to show QR
            else:
                st.error("Error: Classroom data not found. "
                         "Please select a valid classroom.")
        else:
            st.warning("Please select a classroom before generating the QR.")


# --- QR page content ---
else:
    st.title(f"QR Code for Classroom {st.session_state.selected_room}")
    st.markdown("---")

    if st.session_state.qr_data_string:
        st.write(f"Here is your QR code for "
                 f"{st.session_state.selected_room} for today.")
        st.write(f"Data: `{st.session_state.qr_data_string}`")

        # Generate and show QR picture
        qr_image = create_qr_image(st.session_state.qr_data_string)
        st.image(
            qr_image,
            caption=f"QR Code for {st.session_state.selected_room}",
            width=300)
    else:
        st.error("Error: No QR data available. "
                 "Please go back and select a classroom.")

    st.markdown("---")
    st.button("↩ Go Back to Select Classroom", on_click=reset_state)
