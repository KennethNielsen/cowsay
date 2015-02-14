#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python version of the cowsay program. The cows are nicked from the
cow files from the original program. All credits for those go to the
authors of the original cowsay.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

from __future__ import print_function, unicode_literals
from textwrap import wrap
import glob
import os


DATA_DIR = '/usr/share/cowsay/cows'
OWN_COWS = {}
CACHED_COWS = OWN_COWS.copy()


def pythonify_cow(cow, cowname):
    """Pythonifies the cow string"""

    # Replace escapes
    cow = cow.replace('\\\\', '\\')
    cow = cow.replace('\@', '@')

    # Escape {}s
    for replacement in ('{', '}'):
        cow = cow.replace(replacement, replacement * 2)

    # Replace existing placeholders with python placements
    for replacement in ('thoughts', 'eyes','tongue'):
        cow = cow.replace('${{' + replacement + '}}', '{' + replacement + '}')
        cow = cow.replace('$' + replacement, '{' + replacement + '}')

    # Hack for the three-eyes cow
    if cowname == 'three-eyes':
        cow = cow.replace('{eyes}', '{three_eyes}')

    return cow


def parse_cow(filepath, cowname):
    """Returns raw cow from a cow file

    Look in one of the files in DATA_DIR for an example of how the cow files
    look.
    """
    cow = ''
    with open(filepath) as file_:
        start = False
        for line in file_:
            if line.startswith('EOC'):
                break
            if start:
                cow += line
            elif '<<' in line and 'EOC' in line:
                start = True

    return pythonify_cow(cow, cowname)


def get_cow(cowname):
    """Returns the desired cow"""
    if cowname not in CACHED_COWS:
        cowpath = os.path.join(DATA_DIR, cowname + '.cow')
        try:
            cow = parse_cow(cowpath, cowname)
        except IOError:
            message = 'No such cow: {}'.format(cowname)
            raise ValueError(message)
        CACHED_COWS[cowname] = cow

    return CACHED_COWS[cowname]


class Cowsay(object):
    """The illustriate Cowsay class"""

    def __init__(self, cow='default', eyes='oo', tongue='  ', thoughts='\\',
                 width=40):
        """Initialize the internal variables.

        Args:
            cow (str): The cow to use. Use the module functions list_cows to
                see which avatars can be used
            eyes (str): The eyes string, must be length 2
            tongue (str): The tongue string, must be length 2
            thoughts (str): The thoughts string, must be length 1
            width (int): The length to which the text will be wrapped. NOTE:
                that the cow in itself may be wider.

        Raises:
            ValueError: If the cow is unknown or if the strings have the wrong
                length

        """
        self.cows = None
        self.cow = get_cow(cow)

        if not isinstance(width, int) or width < 1:
            message = 'Width must be int > 0'
            raise ValueError(message)
        self.width = width

        self.replacements = {}
        for item, length in (('eyes', 2), ('tongue', 2), ('thoughts', 1)):
            self.replacements[item] = locals()[item]
            if len(self.replacements[item]) != length:
                message = '{} must be length {}'.format(item, length)
                raise ValueError(message)
            
        self.replacements['three_eyes'] = self.replacements['eyes'] + \
            self.replacements['eyes'][1]

    def say(self, text):
        """Returns a string with the cow saying some text"""
        wrapped_lines = wrap(text, self.width)
        text_width = max(len(line) for line in wrapped_lines)
        out = ' {}\n'.format('_' * (text_width + 2))
        template = '{{}} {{: <{}}} {{}}\n'.format(text_width)
        if len(wrapped_lines) == 1:
            out += template.format('<', wrapped_lines[0], '>')
        else:
            for line_num, line in enumerate(wrapped_lines):
                if line_num == 0:
                    left, right = '/', '\\'
                elif line_num == len(wrapped_lines) - 1:
                    left, right = '\\', '/'
                else:
                    left, right = '|', '|'
                out += template.format(left, line, right)

        out += ' {}\n'.format('-' * (text_width + 2))
        out += self.cow.format(**self.replacements)
        return out

    @property
    def list_cows(self):
        """Returns a list of all available cow avatars"""
        if self.cows is None:
            cows = OWN_COWS.keys()
            for filepath in glob.glob(os.path.join(DATA_DIR, '*.cow')):
                cowfilepath = os.path.basename(filepath)
                cows.append(os.path.splitext(cowfilepath)[0])
            self.cows = sorted(cows)
        return self.cows


if __name__ == '__main__':
    COW = Cowsay()
    print(COW.say('Live long and prosper'))
    #print(COW.list_cows)
