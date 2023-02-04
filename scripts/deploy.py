from ape import project, accounts
from scripts.helpful_scripts import get_account


def deploy():
    account = accounts.load("ethernaut")
    contract = account.deploy(
        project.ChangeOwner,
        max_priority_fee="0.5 gwei",
        max_fee="1 gwei",
        sender=account,
        publish=True,
    )
    return contract


def main():
    deploy()
