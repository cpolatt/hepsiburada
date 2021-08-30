## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [ScreenShot](#screen)

## General info
This project is hepsiburada case study.

## Technologies
Project is created with:
* Apache Maven version: 3.6.3
* java version: 11.0.12
* Gauge version: 1.1.7

## Setup
To run this project, using cmd:

```
$ mvn.cmd -q clean compile test-compile gauge:execute -Dflags=--hide-suggestion,--simple-console -DspecsDir=specs\CaseStudy.spec:25
```
You need to use gauge run -p or gauge run --parallel to tell gauge to run specs in parallel.

## ScreenShot
![image](https://user-images.githubusercontent.com/11458835/131298198-cfb05f9f-e01f-4dbf-bab0-83ff7ebea90f.png)





