
import docker

client = docker.from_env()

# List all containers
print("Listing all containers:")
for container in client.containers.list(all=True):
    print(f"ID: {container.short_id}, Status: {container.status}")

# Start a stopped container
stopped_containers = [c for c in client.containers.list(all=True) if c.status == "exited"]
if stopped_containers:
    print(f"Starting container {stopped_containers[0].short_id}...")
    stopped_containers[0].start()

# Stop a running container
running_containers = client.containers.list()
if running_containers:
    print(f"Stopping container {running_containers[0].short_id}...")
    running_containers[0].stop()
