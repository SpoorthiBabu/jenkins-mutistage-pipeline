import docker

client = docker.from_env()

def create_network(network_name):
    try:
        network = client.networks.create(network_name, driver="bridge")
        print(f"Network '{network_name}' created successfully.")
        return network
    except Exception as e:
        print(f"Error creating network: {e}")
        return None

def create_and_run_container(image_name, container_name, network_name, ports):
    try:
        container = client.containers.run(
            image_name,
            name=container_name,
            network=network_name,
            detach=True,
            ports=ports,
        )
        print(f"Container '{container_name}' started successfully.")
        return container
    except Exception as e:
        print(f"Error running container: {e}")
        return None

def inspect_network(network_name):
    try:
        network = client.networks.get(network_name)
        print("Network Details:", network.attrs)
        print("Connected Containers:")
        for container in network.containers:
            print(container.name)
    except Exception as e:
        print(f"Error inspecting network: {e}")
