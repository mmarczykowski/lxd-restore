import argparse

from pylxd import Client
from pylxd.exceptions import NotFound


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("container", help="Name of container to restore")
    return parser.parse_args()


def _restore_container(container_name: str):
    client = Client()
    container = client.containers.get(container_name)
    last_snap = container.snapshots.all()[-1]
    container.restore(last_snap)


if __name__ == "__main__":
    args = _parse_args()
    try:
        _restore_container(args.container)
    except NotFound:
        print(f"Container {args.container} not found!")
        exit(1)
