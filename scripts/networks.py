from ape import accounts, chain, config, compilers, convert, networks, project


def main():
    print(networks.active_provider)
    # print(config.dict())
    print(convert("1 gwei", int))
