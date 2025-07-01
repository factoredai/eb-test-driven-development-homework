[template-version]: # (0.0.1)
# Engineering Lab Template

**Tools**: Bash, Python, Pytest
<br>
**Topics**: Test Driven Development

## Introduction

From [BrowserStack](https://www.browserstack.com/guide/what-is-test-driven-development#:~:text=Test%2Ddriven%20development%20(TDD)%20is%20a%20software%20development%20method,safe%2C%20incremental%20changes%20throughout%20development.)

>Test-Driven Development (TDD) is a software development process in which tests are written before the actual code. It ensures the code fulfills defined behaviors through short feedback cycles.

Although the above description is useful, but there are some cases where it is not enough. In particular:

* We have found that writing test cases before *any* other code is impractical, it is sometimes handy to have some boilerplate code beforehand.
* When there are pieces of code that call each other, it is hard to know how should we test each piece in a way that maximizes the productivity of the team.

The purpose of this Lab is to help you understand how to apply TDD when building real and useful software, by (partially) build some sample applications that a lot of people is familiar with already.

## Instructions

Below you will find some tasks, where each represents a piece of real software to build. Each will be useful to highlight some particular aspect of the practice of TDD that we believe it is useful for you to keep in mind. 

**NOTE:** the lab is heavily dependant on a mentor, because it is hard to come up with good automatic feedback.

### Task 1: Building a JSON Parser

Very few people in the world will need to build a JSON parser from scratch; in fact, a language like python have it built in already. However; most people with a bare minimum of programming experience have needed to use one, it is very likely that you are familiar with it. It is useful to use it as an example, because the requirements we will need to satisfy are known to a good extend by most people.

Specifically, we will build a command line tool that takes a file as a parameter and:
1. Returns `0` if it is a valid JSON file.
2. Returns `1` if it is an invalid JSON file.
3. Returns `2` if the file doesn't exist.

You are provided with some boilerplate code inside `task 1`, your task is to build the tool to satisfy the above requirements. From. the boilerplate, you will notice:

* There is a `_cli` function in `src/main.py`, which handles the interaction with the terminal. It defines the file parameter, calls the `main` function with the file as argument and exists the program with the exit code provided by the `main` function. 
* There is already a test case for one of the requirements of the system: returning 2 if the file doesn't exist. 

Notice how we the `_cli` code was written before any test for it; moreover, we don't plan to write tests for it. This is because:
1. There is not much value in doing so, what it does is straight forward and we decided to trust completely its functionality (makes sense only for extremely simple code).
2. Writing tests that interact with the command line is not trivial in Python (in Rust is straight forward), it may make them run slower, which affects productivity.
3. The core of functionality of our tool will be in the `main` function and that is what we will be working with. 

You goal then is to add code to `tests/test_main.py` and `src/main.py` so that it satisfy all of the requirements. One of the nice qualities of this task is that you can add the functionality incrementally, which is a critical aspect of the TDD approach. Now do the rest of the code on your own, follow [Build Your Own JSON Parser](https://codingchallenges.fyi/challenges/challenge-json-parser/) as a guide to add complexity incrementally. Feel free to add any additional modules you think you need, but you can add all test cases from to `test_main.py` using `pytest.mark.paramtrize`. Try to implement everything from scratch!

### Task 2: Building a Compresison Tool

In the example above we wrote all test cases to to the same function. That highlights an approach that is great for productivity: if we only test the API, we can change the implementation any time we want and we wouldn't need to modify the tests. However, it is sometimes harder to think of the edge cases of our solutions in this case. We will see one case here.

We will build a compression tool based on a [Huffman Tree](https://opendsa-server.cs.vt.edu/ODSA/Books/CS3/html/Huffman.html#huffman-coding-trees). We will again build a command line tool, that takes a file as input, but this time produces another file as output, together with some exit codes. The process to achieve this is as follows:
1. Read the input file.
2. Count the number of occurrences of each character in the file.
3. Build a huffman tree based on the character counts.
4. Build a table to map each character to its corresponding code.
5. Build a header that can help you restore the huffman tree.
6. Serialize the contents of the file in #1.
7. Put the header and the output from #6 into a new file.

We won't do all of it here. You will be given some code and your job is to add missing test cases and implementation. In particular, we will be focusing on step #3.



### Task 3: Building a Web App