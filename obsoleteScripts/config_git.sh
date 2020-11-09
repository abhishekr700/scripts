#!/bin/bash

echo -e "GIT Initial Setup for Abhishek Ranjan"

echo -e "Setting Up Name & Email"

git config --global user.name "Abhishek Ranjan"
git config --global user.email "abhishekr700@gmail.com"

echo Name:$(git config --global user.name )
echo Email:$(git config --global user.email )
