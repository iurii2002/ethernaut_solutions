from ape import accounts, chain, config

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account(index=None, id=None):
    """This function will load:
        - if no argument:
                    if local envoironment: first account of local envoironment;
                    if non-local envoironment: load wallets from config file "from_key";
        - if index argument: index account of local envoironment;
        - if id argument: loads account according to the id. The following account should be
                            stored in config file;

    Args:
        index (int): optional
        id (string): optional

    Returns:
        account
    """

    # if index:
    #     return accounts[index]
    # if id:
    #     return accounts.load(id)
    return accounts.load(config.get_config("wallets").account)


def main():
    pass
