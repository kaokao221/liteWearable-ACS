'''
Warnings: the code only wokes on Windows and only wokes on consoles.
It only designed for console at Windows.

It based on curses and wokes by LWACS APIs.
Need a network connection to launch.

Opened sources.

Network test links are from:
- cloudflare.com
- github.com
- google.com #unaviliable in China mainland.
- azure.com
- especially tested in \
'''

import requests, os, threading, curses

console = curses.initscr()
console.erase()

def in_key(level_count: int | None = None, *suggestions, path : str = "main") -> str:
    curses.curs_set(2)
    console.clear()