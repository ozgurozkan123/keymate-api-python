"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from keymateapi import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BrowsewithProxyResultItem:
    UNSET='__SPEAKEASY_UNSET__'
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    r"""The title of the search result"""
    link: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link'), 'exclude': lambda f: f is None }})
    r"""The URL of the search result"""
    summary: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('summary'), 'exclude': lambda f: f is None }})
    r"""A summary of the HTML content of the search result"""
    full_content: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('full_content'), 'exclude': lambda f: f is None }})
    r"""Full content of the HTML content of the search result"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

