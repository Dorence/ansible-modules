# Ansible Modules

A collection of Ansible modules for personal use.

Based on [ansible-community 10.7](https://docs.ansible.com/projects/ansible/10/), ansible-core 2.17, python 3.10-3.12.

Remote executor's python version is in 3.7-3.12.

## Installation

- Add to your ansible as library or collection.
- As a library (name might conflict):
  - Clone this repo at `repo-path`
  - Change ansible config:
    - In config file: `[default] library=<repo-path>/plugins/modules`
    - Environment variable: `ANSIBLE_LIBRARY=<repo-path>/plugins/modules`
  - Call module `xyz.py` as `xyz`
  - `ansible-config dump | grep DEFAULT_MODULE_PATH` to inspect if loaded.
- As a collection (recommended):
  - Make a collection path `<collection-path>/my_namespace/my_collection` (e.g. `~/.ansible/collections/dorence/core`)
  - Clone this repo into the collection directory
  - Change ansible config:
    - In config file: `[default] collections_paths=<collection-path>`
    - Environment variable: `ANSIBLE_COLLECTIONS_PATH=<collection-path>`
  - Call module `xyz.py` as `my_namespace.my_collection.xyz` (e.g. `dorence.core.xyz`)
  - `ansible-config dump | grep COLLECTIONS_PATH` to inspect if loaded.

## Modules

Use `ansible-doc -t module <module_name>` to inspect detailed usage.

- `file_check`: Check if files/directories/symlinks exist on remote.
