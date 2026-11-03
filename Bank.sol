// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// BCT3 - Bank account of a customer: Deposit, Withdraw, Show balance
contract Bank {

    // Each customer's address -> their balance (in wei)
    mapping(address => uint256) private balances;

    // Events: log entries visible in the transaction details
    event Deposited(address indexed customer, uint256 amount);
    event Withdrawn(address indexed customer, uint256 amount);

    // 1. Deposit money
    // "payable" lets the function receive ETH. Enter the value in the VALUE box in Remix.
    function deposit() public payable {
        require(msg.value > 0, "Send some ether");
        balances[msg.sender] += msg.value;
        emit Deposited(msg.sender, msg.value);
    }

    // 2. Withdraw money (amount is in wei)
    function withdraw(uint256 amount) public {
        require(amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;   // update balance first (safe practice)

        (bool sent, ) = payable(msg.sender).call{value: amount}("");
        require(sent, "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // 3. Show balance of the caller (in wei)
    function showBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
}
