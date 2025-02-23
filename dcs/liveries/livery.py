from __future__ import annotations

import logging
import os.path
import re
from typing import Optional, Set
from zipfile import ZipFile, BadZipFile


def _attempt_read_from_filestream(filestream: bytes) -> Optional[str]:
    encodes = ["utf-8", "ansi"]
    for enc in encodes:
        try:
            code = filestream.decode(enc)
        except UnicodeDecodeError:
            continue
        return code
    return None


def _regex_group_extractor(regex: str, text: str, fallback=None):
    match = re.search(regex, text, re.MULTILINE)
    if match is not None:
        return match.group(1)
    else:
        return fallback


def _clear_comments(code: str) -> str:
    pattern = re.compile(r'--\[\[.*?(?:]]--|--]])', re.MULTILINE | re.DOTALL)
    code = re.sub(pattern, "", code)
    code = re.sub(r'^--.*?$', "", code, flags=re.MULTILINE)
    return code


class Livery:
    def __init__(
        self, path_id: str, name: str, order: int, countries: Optional[Set[str]]
    ) -> None:
        # ID to be used in the miz.
        self.id = path_id
        # Display name.
        self.name = name
        # UI sort order.
        self.order = order
        # List of countries that may use this livery. If None, all countries may use the
        # livery. The elements in this list are short names for countries, e.g. "USA"
        # or "RUS".
        self.countries = countries

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def __lt__(self, other) -> bool:
        if self.order == other.order:
            return self.name < other.name
        if self.order is None:
            return True
        return False if other.order is None else self.order < other.order

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def valid_for_country(self, country: str) -> bool:
        return self.countries is None or country in self.countries

    @staticmethod
    def from_lua(code: str, path: str) -> Optional[Livery]:
        """
        Scans the given code (expecting contents from a description.lua file)
        to extract the name of the livery together with the countries for which the livery is applicable.
        If no name is found, it defaults to the folder-name like DCS would.
        If no countries are found, it means the livery is valid for all countries.
        Finally we also attempt to extract the order to sort liveries like DCS.
        If no order is found, we use a default value of 0.

        :param code: The contents of description.lua for the livery in question
        :param path: The path of the livery in question
        """
        path_id = path.split("\\")[-1].replace(".zip", "")
        if path_id == "placeholder":
            return None

        code = _clear_comments(code)

        livery_name = _regex_group_extractor(r'^name\s*=\s*"(.*)"\s*(?:--.*)?$', code, path_id)

        regex = r'^countries\s*=\s*(\{\s*"[A-Z]+"\s*(?:,\s*"[A-Z]+"\s*)*\s*,?\s*\})\s*(?:--.*)?$'
        countries = _regex_group_extractor(regex, code)
        if countries is not None:
            exec(f"country_list = {countries}")
            countries = set(filter(lambda x: x != "", locals()['country_list']))

        order = _regex_group_extractor(r'^order\s*=\s*(-?[0-9]+)\s*(?:--.*)?$', code, 0)
        order = None if path_id == "default" else order
        if order is not None and not isinstance(order, int):
            try:
                order = int(order)
            except ValueError:
                order = 0

        return Livery(path_id.lower(), livery_name, order, countries)

    @staticmethod
    def from_path(path: str) -> Optional[Livery]:
        if os.path.isdir(path):
            return Livery.from_directory(path)
        elif path.endswith(".zip"):
            try:
                return Livery.from_zip(path)
            except BadZipFile:
                logging.warning(
                    f"Bad zipfile skipped at path: {path} "
                    "(this may indicate a corrupted DCS installation)"
                )
        return None

    @staticmethod
    def from_directory(path: str) -> Optional[Livery]:
        """
        Verifies a description file exists and reads its contents,
        passing it to 'scan_lua_code'.

        :param path: The path of the livery in question
        """
        description_path = os.path.join(path, "description.lua")
        if not os.path.exists(description_path):
            return None

        # Known encodings used for description.lua files
        with open(description_path, "rb") as file:
            code = _attempt_read_from_filestream(file.read())

        if code is None:
            logging.warning(f" Unknown encoding found in '{description_path}'")
            return None

        try:
            return Livery.from_lua(code, path)
        except Exception:
            logging.getLogger("pydcs").exception(
                "Failed to parse Lua code in %s", description_path
            )
            print("Failed to parse Lua code in {}".format(description_path))
            raise

    @staticmethod
    def from_zip(path: str) -> Optional[Livery]:
        """
        Some liveries are zipped, this does the same as 'scan_lua_description',
        except for the fact it needs to "open the zip" first.

        :param path: The path of the livery in question
        """
        if not os.path.exists(path):
            return None
        with ZipFile(path, "r") as zf:
            try:
                with zf.open("description.lua", "r") as file:
                    code = _attempt_read_from_filestream(file.read())
            except KeyError:
                return None

        if code is None:
            logging.warning(f" Unknown encoding found in '{path}/description.lua'")
            return None

        try:
            return Livery.from_lua(code, path)
        except Exception:
            error_path = "!".join([path, "description.lua"])
            logging.getLogger("pydcs").exception(
                "Failed to parse Lua code in %s", error_path
            )
            raise
