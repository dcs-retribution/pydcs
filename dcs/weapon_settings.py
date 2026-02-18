import logging
from typing import Any, Dict, List, Optional


class WeaponSetting:
    """Represents a single weapon setting with its properties and constraints."""
    
    def __init__(self, setting_dict: Dict[str, Any]):
        """
        Initialize a weapon setting from a dictionary.
        
        Args:
            setting_dict: Dictionary containing setting properties (id, label, control, etc.)
        """
        self.id: str = setting_dict["id"]
        self.label: str = setting_dict["label"]
        self.control: str = setting_dict["control"]
        self.base_dim: str = setting_dict.get("baseDim", "")
        self.dimension: str = setting_dict.get("dimension", "")
        self.read_only: bool = setting_dict.get("readOnly", False)
        self.values: List[Dict[str, Any]]
        self.def_value: Any
        self.min_value: Optional[float]
        self.max_value: Optional[float]

        if self.control == "comboList":
            self.values = setting_dict.get("values", [])
            self.def_value = setting_dict.get("defValue", 0)
            self.min_value = None
            self.max_value = None
        elif self.control == "spinbox":
            self.values = []
            self.def_value = setting_dict.get("defValue", 0)
            self.min_value = setting_dict.get("min")
            self.max_value = setting_dict.get("max")
        else:
            self.values = []
            self.def_value = setting_dict.get("defValue")
            self.min_value = None
            self.max_value = None

        self.visibility_condition: Optional[List[Dict[str, Any]]] = setting_dict.get(
            "VisibilityCondition"
        )
        
        # Current value
        self._current_value = self.def_value
    
    @property
    def current_value(self) -> Any:
        """Get the current value of this setting."""
        return self._current_value
    
    @current_value.setter
    def current_value(self, value: Any) -> None:
        if self.read_only:
            pass
        
        if self.control == "comboList":
            valid_ids = [v["id"] for v in self.values]
            if value not in valid_ids:
                raise ValueError(
                    f"Invalid value {value} for {self.id}. "
                    f"Must be one of {valid_ids}"
                )
        elif self.control == "spinbox":
            if self.min_value is not None and value < self.min_value:
                raise ValueError(
                    f"Value {value} for {self.id} is below minimum {self.min_value}"
                )
            if self.max_value is not None and value > self.max_value:
                raise ValueError(
                    f"Value {value} for {self.id} exceeds maximum {self.max_value}"
                )
        
        self._current_value = value
    
    def is_visible(self, settings_values: Dict[str, Any]) -> bool:
        """
        Check if this setting should be visible given current settings values.
        
        Args:
            settings_values: Dictionary of current setting ID -> value mappings
            
        Returns:
            True if this setting should be visible, False otherwise
        """
        if not self.visibility_condition:
            return True
        
        # Parse visibility condition which can include AND/OR operators
        # Format: [{"id": "x", "value": 1}, "and", {"id": "y", "value": 2}]
        conditions = []
        operators: List[str] = []
        
        for item in self.visibility_condition:
            if isinstance(item, str):
                operators.append(item.lower())
            elif isinstance(item, dict):
                required_id = item["id"]
                required_value = item["value"]
                current_value = settings_values.get(required_id)
                conditions.append(current_value == required_value)
        
        if not conditions:
            return True

        if not operators:
            return all(conditions)

        result = conditions[0]
        for i, operator in enumerate(operators):
            if i + 1 < len(conditions):
                if operator == "and":
                    result = result and conditions[i + 1]
                elif operator == "or":
                    result = result or conditions[i + 1]
        
        return result


class WeaponSettings:
    """
    Manages a collection of weapon settings with automatic visibility handling.
    
    This class automatically updates which settings are visible/adjustable based on
    visibility conditions when setting values are changed.
    """
    
    def __init__(self, settings_list: List[Dict[str, Any]]):
        """
        Initialize weapon settings from a settings list.
        
        Args:
            settings_list: List of setting dictionaries (from weapon definition)
        """
        self._settings: Dict[str, WeaponSetting] = {}
        
        # Create WeaponSetting objects for each setting
        for setting_dict in settings_list:
            setting = WeaponSetting(setting_dict)
            self._settings[setting.id] = setting
    
    def __getitem__(self, key: str) -> Any:
        """
        Allow dictionary-style access to settings.
        """
        return self.get_value(key)
    
    def __setitem__(self, key: str, value: Any) -> None:
        """
        Allow dictionary-style setting of values.
        """
        self.set_value(key, value)
    
    def get_value(self, setting_id: str) -> Any:
        if setting_id not in self._settings:
            raise KeyError(f"Setting '{setting_id}' not found")
        return self._settings[setting_id].current_value
    
    def set_value(self, setting_id: str, value: Any) -> None:
        if setting_id not in self._settings:
            raise KeyError(f"Setting '{setting_id}' not found")
        self._settings[setting_id].current_value = value
    
    def _get_current_values(self) -> Dict[str, Any]:
        """
        Get a dictionary of current setting values.
        
        Returns:
            Dictionary mapping setting IDs to their current values
        """
        return {
            setting_id: setting.current_value
            for setting_id, setting in self._settings.items()
        }
    
    def get_visible_settings(self) -> List[WeaponSetting]:
        """
        Get all currently visible settings.
        
        Returns:
            List of WeaponSetting objects that are currently visible
        """
        current_values = self._get_current_values()
        return [
            setting for setting in self._settings.values()
            if setting.is_visible(current_values)
        ]
    
    def list_settings(self) -> List[str]:
        """
        Get list of all available setting IDs.
        
        Returns:
            List of setting IDs that can be accessed via get_value() or set_value()
        """
        return sorted(self._settings.keys())
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Serialize to dictionary format (for mission file).

        Only includes visible settings with non-default values or all settings
        depending on requirements.
        
        Returns:
            Dictionary suitable for Lua table serialization
        """
        current_values = self._get_current_values()
        result = {}
        for setting in self._settings.values():
            # Include all settings that are visible
            if setting.is_visible(current_values):
                result[setting.id] = setting.current_value
        return result
    
    def from_dict(self, lua_table: Dict[str, Any]) -> None:
        """
        Load settings from a Lua table (from mission file).
        
        Args:
            lua_table: Dictionary with setting ID -> value mappings
        """
        for setting_id, value in lua_table.items():
            if setting_id in self._settings:
                try:
                    self.set_value(setting_id, value)
                except ValueError as e:
                    # Log warning but continue loading other settings
                    logging.error(f"Warning: Could not set {setting_id} to {value}: {e}")
    
    def reset_to_defaults(self) -> None:
        """Reset all settings to their default values."""
        for setting in self._settings.values():
            setting.current_value = setting.def_value

def has_settings(weapon_def: Dict[str, Any]) -> bool:
    return "settings" in weapon_def and isinstance(weapon_def["settings"], list)


def create_settings(weapon_def: Dict[str, Any]) -> Optional[WeaponSettings]:
    if not has_settings(weapon_def):
        return None
    return WeaponSettings(weapon_def["settings"])