// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// BCT4 - Student data using Structure, Array and Fallback
contract StudentData {

    // Structure: a custom data type grouping student details
    struct Student {
        uint256 id;
        string name;
        uint256 age;
        string course;
    }

    // Array of structures: stores all students
    Student[] public students;

    event StudentAdded(uint256 id, string name);
    event FallbackCalled(address sender, uint256 value, bytes data);

    // Add a new student
    function addStudent(
        uint256 _id,
        string memory _name,
        uint256 _age,
        string memory _course
    ) public {
        students.push(Student(_id, _name, _age, _course));
        emit StudentAdded(_id, _name);
    }

    // Get a student by index (0 for the first student)
    function getStudent(uint256 index)
        public
        view
        returns (uint256, string memory, uint256, string memory)
    {
        require(index < students.length, "Invalid index");
        Student memory s = students[index];
        return (s.id, s.name, s.age, s.course);
    }

    // Total number of students stored
    function getTotalStudents() public view returns (uint256) {
        return students.length;
    }

    // Fallback: runs when someone calls a function that does not exist
    // (calldata is not empty and matches no function)
    fallback() external payable {
        emit FallbackCalled(msg.sender, msg.value, msg.data);
    }

    // Receive: runs when plain ETH is sent with empty calldata
    receive() external payable {
        emit FallbackCalled(msg.sender, msg.value, "");
    }
}
