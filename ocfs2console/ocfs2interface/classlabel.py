# OCFS2Console - GUI frontend for OCFS2 management and debugging
# Copyright (C) 2005 Oracle.  All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA.

import re

caps = re.compile('(?!\A)[A-Z][a-z]')

def make_title(m):
    return ' ' + m.group()

class class_label(object):
    def __get__(self, obj, cls):
        return caps.sub(make_title, cls.__name__)

class_label = class_label()

def main():
    import sys

    cls = type(sys.argv[1], (), {'label': class_label})
    print cls.label

if __name__ == '__main__':
    main()
