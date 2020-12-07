import platform


def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
    print(f'arch{platform.architecture()}, machine {platform.machine()}')
    print(f'{platform.version()}')