import platform
import ctypes
import math
import logging
import random
import time
import os

import pyglet

pyglet.options["shadow_window"] = False
pyglet.options["debug_gl"] = False
pyglet.options["search_local_libs"] = True
pyglet.options["audio"] = ("openal", "pulse", "directsound", "xaudio2", "silent")

import pyglet.gl as gl
import player
import texture_manager

from skybox import Skybox
from clouds import Clouds

import world

import options
import time

import joystick
import keyboard_mouse
from collections import deque


def main():
	init_logger()
	game = Game()
	game.run()

if __name__ == "__main__":
	main()
