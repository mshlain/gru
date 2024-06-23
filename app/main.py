import streamlit as st
from ping_utils import run_ping

def main():
    st.title("Destination Address Ping with Console Output")
    
    destination_address = st.text_input("Enter your destination address:")
    
    console_output = st.empty()
    
    if st.button('Run Ping'):
        if destination_address:
            status = st.warning(f"Pinging {destination_address}...")
            console_output.text_area("Console Output", value="", height=400)
            success = run_ping(destination_address, console_output)
            
            if success:
                status.success(f"Successfully pinged {destination_address}")
            else:
                status.error(f"Failed to ping {destination_address}")
        else:
            status.warning("Please enter a destination address before running the ping.")

if __name__ == "__main__":
    main()
