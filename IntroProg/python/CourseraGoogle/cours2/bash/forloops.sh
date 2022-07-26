#!/bin/bash
fruits=()
for fruit in apple banana watermelon; do
    echo "I like $fruit!"
    fruits+=($fruit)
done;
for fru in ${fruits[@]}; do
    echo "this is a $fru"
done