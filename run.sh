#!/usr/bin/bash

HELPER_PATH=./helpers/helpers.cpp

function compile() {
    echo "Compiling $1/main.cpp with $HELPER_PATH"
    g++ "$1/main.cpp" $HELPER_PATH -o $1/a.out
}

function run() {
    echo "Running $1" ; echo
    ./$1/a.out $2
    rm -f ./$1/a.out
}

# read arguments
if [ $# -ne 2 ]
then
    echo "usage: ./run.sh day_xx [test/input]"
    exit 1
fi

day=$1
input_type=$2

compile $day

BASE_PATH=`pwd`

if [ "$input_type" = "test" ]
then
    run $day "$BASE_PATH/$day/test.txt"
elif [ "$input_type" = "input" ]
then 
    run $day "$BASE_PATH/$day/input.txt"
else
    echo "usage: ./run.sh day_xx [test/input]"
fi