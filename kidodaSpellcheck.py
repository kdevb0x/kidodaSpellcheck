#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kSpellcheck.py
#  
#  Copyright 2017 KiDoDa <kdevb0x@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
""" 
/* some initial ideas(psuedoc0de?) */
 
some func(monitors  keyboard input) returns filtered intpu. 
 looks for duplicate letters (except ee, oo, and zz)
 
  keyboard input: seperate into words, pass to compare function.

  parse english dictionary
  load as linked list
  
  compare func(word) return bool
   binary tree search dictionary alphabetically
   if True: return wordas is
   if False: output closest spelling to ask func
   
   ask func(posssible spelling)
   user confirms with enter key: return possible spelling
   if delete key delete word up to closest match from tree search:
        if delete repeat
        else pass to compare func
        
output corrected word to system keyboard in interface

"""
 

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    import arg
    sys.exit(main(sys.argv))
