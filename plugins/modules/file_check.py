# -*- coding: utf-8 -*-
# Copyright (c) 2025-present Dorence Deng. All rights reserved.
import os
from typing import Callable, TypedDict

from ansible.module_utils.basic import AnsibleModule

## ansible-doc -t module dx.file_check
DOCUMENTATION = r"""
---
module: file_check
author: Dorence Deng (@Dorence)
short_description: Check if files exist on remote
description: Gathers facts about files/directories/symlinks exist on remote.
options:
  directories:
    description: Check if these are existing directories.
    required: false
    type: list
    elements: path
    alias: [ dir ]
  executables:
    description: Check if these are existing executable files.
    required: false
    type: list
    elements: path
    alias: [ exec ]
  regulars:
    description: Check if these are existing regular files.
    required: false
    type: list
    elements: path
    alias: [ reg ]
version_added: 0.0.1
"""

EXAMPLES = r"""
- name: Check if files exist
  file_check:
    regulars:
    - ~/.ssh/config
"""

RETURN = r"""
all:
  description: Number of entries checked.
  type: int
ok:
  description: Number of entries that exist.
  type: int
missed:
  description: List of entries that do not exist.
  type: list
"""


class Result(TypedDict):
    all: int
    ok: int
    missed: list[str]


def check(paths, judge: Callable[[str], bool]):
    all = 0
    ok = 0
    missed = []
    for path in paths:
        for root, dirs, files in os.walk(path):
            all += 1
            if judge(path):
                ok += 1
            else:
                missed.append(path)
    return all, ok, missed


def main():
    global module

    def path_list_arg(*, alias: list[str] | None = None, required: bool = False):
        return dict(type="list", elements="path", required=required, alias=alias)

    module = AnsibleModule(
        argument_spec=dict(
            directory=path_list_arg(alias=["dir"]),
            executable=path_list_arg(alias=["exec"]),
            regular=path_list_arg(alias=["reg"]),
        ),
        supports_check_mode=True,
    )
    result: Result = {"all": 0, "ok": 0, "missed": []}
    try:
        if module.params["regular"]:
            all, ok, missed = check(module.params["regular"], os.path.isfile)
            result["all"] += all
            result["ok"] += ok
            result["missed"].extend(missed)
    except Exception as e:
        module.fail_json(msg=str(e))
    module.exit_json(changed=False, **result)
    pass


if __name__ == "__main__":
    main()
