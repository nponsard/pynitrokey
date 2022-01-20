# -*- coding: utf-8 -*-
#
# Copyright 2022 Nitrokey Developers
#
# Licensed under the Apache License, Version 2.0, <LICENSE-APACHE or
# http://apache.org/licenses/LICENSE-2.0> or the MIT license <LICENSE-MIT or
# http://opensource.org/licenses/MIT>, at your option. This file may not be
# copied, modified, or distributed except according to those terms.

import re

from pynitrokey.updates import FirmwareUpdate, Repository

REPOSITORY_OWNER = "Nitrokey"
REPOSITORY_NAME = "nitrokey-3-firmware"
UPDATE_PATTERN = re.compile("\\.sb2$")


def _get_repo() -> Repository:
    return Repository(
        owner=REPOSITORY_OWNER, name=REPOSITORY_NAME, update_pattern=UPDATE_PATTERN
    )


def get_latest_update() -> FirmwareUpdate:
    return _get_repo().get_latest_update()


def get_update(tag: str) -> FirmwareUpdate:
    return _get_repo().get_update(tag)
