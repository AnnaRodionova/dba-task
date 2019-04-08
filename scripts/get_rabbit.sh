#!/bin/bash

sudo apt-get update &&
sudo apt-get install -y dirmngr apt-transport-https &&
sudo apt-key adv --keyserver "hkps.pool.sks-keyservers.net" --recv-keys "0x6B73A36E6026DFCA" &&
echo 'deb http://dl.bintray.com/rabbitmq-erlang/debian stretch erlang' | sudo tee /etc/apt/sources.list.d/bintray.erlang.list &&
echo 'deb https://dl.bintray.com/rabbitmq/debian stretch main' | sudo tee /etc/apt/sources.list.d/bintray.rabbitmq.list &&
sudo apt-get update &&
sudo apt-get install -y erlang-nox rabbitmq-server &&
sudo service rabbitmq-server start
