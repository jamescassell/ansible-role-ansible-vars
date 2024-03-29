# -*- coding: utf-8 -*-

# Copyright: (c) 2019, James Cassell (@jamescassell)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

class FilterModule(object):
    ''' Ansible compatibility jinja2 filters '''

    def filters(self):
        return {
            'dict': dict
        }
