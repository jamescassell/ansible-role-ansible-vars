# Copyright 2014, Brian Coca <bcoca@ansible.com>
# Copyright 2017, Ken Celenza <ken@networktocode.com>
# Copyright 2017, Jason Edelman <jason@networktocode.com>
# Copyright 2017, Ansible Project
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


#import itertools
#import math
#
#from jinja2.filters import environmentfilter
#
#from ansible.errors import AnsibleFilterError
#from ansible.module_utils.common.text import formatters
#from ansible.module_utils.six import binary_type, text_type
from ansible.module_utils.six.moves import zip, zip_longest
#from ansible.module_utils.common._collections_compat import Hashable, Mapping, Iterable
#from ansible.module_utils._text import to_native, to_text
#from ansible.utils.display import Display




class FilterModule(object):
    ''' Ansible math jinja2 filters '''

    def filters(self):
        return {
            'zip': zip,
            'zip_longest': zip_longest,
        }
