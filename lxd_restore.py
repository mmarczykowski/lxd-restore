import argparse


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("container", help="Name of container to restore")
    return parser.parse_args()


def _restore_container(container: str):
    print(f"restoring container: {container}")


if __name__ == "__main__":
    args = _parse_args()
    _restore_container(args.container)
