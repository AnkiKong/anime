import os
import subprocess
import argparse

def get_config_path():
    out = subprocess.check_output(["rclone", "config", "file"])
    return out

def get_config_dirname():
    return os.path.dirname(get_config_path())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("token", help="rclone api token", type=str)
    args = parser.parse_args()

    os.makedirs(get_config_dirname())
    with open(get_config_path(), "w", encoding="utf8") as out:
        out.write(args.token)
