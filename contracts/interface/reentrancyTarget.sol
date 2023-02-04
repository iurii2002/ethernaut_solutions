// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract IReentrance {
    function donate(address _to) public payable {}

    function balanceOf(address _who) public view returns (uint256 balance) {}

    function withdraw(uint256 _amount) public {}
}
