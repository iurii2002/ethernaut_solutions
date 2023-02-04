import pytest
from ape import accounts, project


def deploy_elevator():
    account = accounts.test_accounts[0]
    elevator_contract = account.deploy(
        project.Elevator,
    )
    return elevator_contract


def deploy_elevator_atack(address):
    account = accounts.test_accounts[0]
    elevator_atack_contract = account.deploy(
        project.ElevatorAtack,
        address,
    )
    return elevator_atack_contract


def test_my_method():
    account = accounts.test_accounts[0]
    elevator = deploy_elevator()
    elevator_atack = deploy_elevator_atack(elevator.address)

    print("elevator address ", elevator_atack.elevator())
    print("elevator attack used ", elevator_atack.used())

    print("elevator top ", elevator.top())
    print("elevator floor ", elevator.floor())

    elevator_atack.invoke_transaction(
        "useElevator",
        5,
        max_priority_fee="1 gwei",
        max_fee="2 gwei",
        sender=account,
    )
    print("after")
    print("elevator top ", elevator.top())
    print("elevator floor ", elevator.floor())

    assert elevator.top() is True
    assert 1 == 0
