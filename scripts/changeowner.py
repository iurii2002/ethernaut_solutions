from ape import project, accounts
from scripts.helpful_scripts import get_account


def sent_tx():
    account = accounts.load("ethernaut")
    contract = project.ChangeOwner.at("0x52ecC1EABd4874eC14EB30cdc237579F0ae0678E")
    # contract.changeOwner()
    contract.invoke_transaction(
        "changeOwner",
        "0x2Cd71C554354781333019FcD78Ddccc9CEFC7F63",
        max_priority_fee="0.1 gwei",
        max_fee="0.2 gwei",
        sender=account,
    )


def main():
    sent_tx()
