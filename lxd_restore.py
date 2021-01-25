import argparse

from pylxd import Client


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
    _restore_container(args.container)
