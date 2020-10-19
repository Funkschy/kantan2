from platform import system


def get_os_name() -> str:
    return system()
