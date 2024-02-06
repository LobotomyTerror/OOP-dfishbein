# CI/CD Badge

![test](https://github.com/LobotomyTerror/OOP-dfishbein/actions/workflows/ci-test.yml/badge.svg)

# Course Description


| __Course__          | CSCI 375 - OOP Design                             | 
| ------------------- | ------------------------------------------------- |
| __Section__         | 1                                                 | 
| __Semester__        | Spring 2024                                       |
| __Student__         | Daniel Fishbein                                   | 
| __Mav Username__    | dfishbein                                         | 
| __GitHub Username__ | LobotomyTerror                                    |
| __Repository__      | https://github.com/LobotomyTerror/OOP-dfishbein   |


# Assignments


## Assignment #0


| __Assignment Details__ | __Info__                                       |
|------------------------|------------------------------------------------|
| __Name__               | Sort Two Numbers                               |
| __Description__        | Solving a simple Kattis problem [sorttwonumber](https://open.kattis.com/problems/sorttwonumbers) and getting Environment setup    |
| __Due__                | 02/06/2024                                     |
| __Difficulty__         | 1.4 as of 01/29/2024                           |
| __Status__             | Completed                                      |
| __Location__           | https://github.com/LobotomyTerror/OOP-dfishbein/tree/main/assignments/assingment_one/sorttwonumbers                           |
| __Self Grade__         | 100/100                                        |
| __Notes__ | Had a little trouble figuring out the kattis cli but was able to figure it out. Everything is working as of now and submitted              |



## PlantUML CLI project

Simply project that I have added to my list of stuff. All I wanted to be able to do was run the plantuml program through the command line which makes it a lot faster when wanting to output the uml diagram. So far I have gotten a little head way done with this project. I have gotten it to be downloaded into the container and set an environment variable so that it can be used as a variable instead of using the entire absolute path to run the jar file. Next I need to get it aliased so that it can simply be a variable typed in that runs the jar script in the background and outputs a uml file from the acceptable files that work with the jar command.

So far this is what I have:
```
java -jar $PLANT test.txt
```
This works for the moment but I want to continue to improve this by adding an alias to this environment variable, so it would look like this:

```
plantuml test.txt
```
Other information about how this works is pretty striaght forward. It requires specific file types that it can convert to a png file that displays the actual uml diagram.

I created a .txt file for this and put this in the file itself:
```
@startuml
Alice -> Bob: test
@enduml
```
Once that is created you can run the above commmand and it will output:

![uml diagram](https://github.com/LobotomyTerror/OOP-dfishbein/blob/main/assignments/assingment0/sorttwonumbers/uml/test.png)
