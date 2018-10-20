import docker

def conCount():
    client = docker.from_env()
    return len(client.containers.list())