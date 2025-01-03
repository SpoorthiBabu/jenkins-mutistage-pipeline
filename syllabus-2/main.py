from network_manager import create_network, create_and_run_container, inspect_network
import requests

# Define the network and container details
network_name = "custom_bridge_network4"
image_name = "web_app_container"
container_name = "web_app_container2"

# Step 1: Create the custom Docker network
network = create_network(network_name)

# Step 2: Start the web app container
if network:
    web_container = create_and_run_container(
        image_name,
        container_name,
        network_name,
        {"5000/tcp": 5000},  # Port mapping
    )

    # Step 3: Inspect the network
    if web_container:
        inspect_network(network_name)

        # Step 4: Test the web app connectivity
        try:
            response = requests.get("http://localhost:5000")
            print("Response from web app:", response.text)
        except Exception as e:
            print("Error connecting to web app:", e)
