from typing import List, Type

from src.components.base import UIComponent

from .json_component import JsonWidget
from .guid_component import GUUIDWidget

COMPONENTS: List[Type[UIComponent]] = [
    JsonWidget,
    GUUIDWidget
]
