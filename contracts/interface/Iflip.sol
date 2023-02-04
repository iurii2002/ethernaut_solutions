// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IFlip {
    function flip(bool _guess) external returns (bool);
}
