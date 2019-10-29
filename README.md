ansible-vars
============

Define `ansible_vars` dict to access all other ansible variables.

Requirements
------------

Ansible version 2.2 or later.

Role Variables
--------------

```yaml
# This role has no user-configurable defaults.  These "defaults" are here
# solely to demonstrate the types of the variables available when depending on
# this role.

# dict containing variable names mapped to variable values
ansible_vars: {}
# a list of the available ansible variables
ansible_vars_keys: []
# list of values of each ansible variable in the same order as ansible_vars_keys
ansible_vars_values: []

# an alias to ansible_vars_keys, ostensibly identical to `q('varnames', '.')`
ansible_vars_varnames: "{{ ansible_vars_keys }}"
```

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: servers
  vars:
    myindirectvar: thatvar
    thatvar: Magical Value
  roles:
  - ansible-vars
  tasks:
  - name: print value of thatvar
    debug:
      msg: "{{ ansible_vars[myindirectvar] }}"
```

License
-------

(Apache-2.0 or MIT or BSD-3-Clause) and GPL-3.0-or-later

Author Information
------------------

[James Cassell](https://github.com/jamescassell)
