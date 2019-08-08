#!/usr/bin/python3
from Strategy import UpLeftStrategy
from Game import Standard2048Game

Standard2048Game( UpLeftStrategy() ).play()
