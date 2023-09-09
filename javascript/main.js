"use strict";

var d, input, Grades;

d = document;

Grades = [
    "3rd",
    "4th",
    "5th",
    "6th",
    "7th",
    "8th",
    "9th",
    "10th",
    "11th",
    "12th",
];

input = d.querySelector(".input").value;

function check() {
    switch(input) {
        case Grades[0]:
            gradethree();
        break;
        case Grades[1]:
            gradefour();
        break;
        case Grades[2]:
            gradefive();
        break;
        case Grades[3]:
            gradesix();
        break;
        case Grades[4]:
            gradeseven();
        break;
        case Grades[5]:
            gradeeight();
        break;
        case Grades[6]:
            gradenine();
        break;
        case Grades[7]:
            gradeten();
        break;
        case Grades[8]:
            gradeeleven();
        break;
        case Grades[9]:
            gradetweleve();
        break;
        default:
            // do nothing
        break;
    }
}

function gradethree() {
    d.querySelector(".helper").innerHTML = `<iframe src='3rd.html'></iframe>`;
}

function gradefour() {
    d.querySelector(".helper").innerHTML = `<iframe src='4th.html'></iframe>`;
}

function gradefive() {
    d.querySelector(".helper").innerHTML = `<iframe src='5th.html'></iframe>`;
}

function gradesix() {
    d.querySelector(".helper").innerHTML = `<iframe src='6th.html'></iframe>`;
}

function gradeseven() {
    d.querySelector(".helper").innerHTML = `<iframe src='7th.html'></iframe>`;
}

function gradeeight() {
    d.querySelector(".helper").innerHTML = `<iframe src='8th.html'></iframe>`;
}

function gradenine() {
    d.querySelector(".helper").innerHTML = `<iframe src='9th.html'></iframe>`;
}

function gradeten() {
    d.querySelector(".helper").innerHTML = `<iframe src='10th.html'></iframe>`;
}

function gradeeleven() {
    d.querySelector(".helper").innerHTML = `<iframe src='11th.html'></iframe>`;
}

function gradetweleve() {
    d.querySelector(".helper").innerHTML = `<iframe src='12th.html'></iframe>`;
}
