"""
Dynamic weapon settings management for DCS weapons.

This module provides classes to manage weapon settings with automatic visibility
handling based on VisibilityCondition rules.
"""

from typing import Any, Dict, List, Optional
from copy import deepcopy


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
        
        # Handle different control types
        if self.control == "comboList":
            self.values: List[Dict[str, Any]] = setting_dict.get("values", [])
            self.def_value: int = setting_dict.get("defValue", 0)
            self.min_value: Optional[float] = None
            self.max_value: Optional[float] = None
        elif self.control == "spinbox":
            self.values = []
            self.def_value: float = setting_dict.get("defValue", 0)
            self.min_value: Optional[float] = setting_dict.get("min")
            self.max_value: Optional[float] = setting_dict.get("max")
        else:
            self.values = []
            self.def_value = setting_dict.get("defValue")
            self.min_value = None
            self.max_value = None
        
        # Visibility conditions
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
        """
        Set the current value with validation.
        
        Args:
            value: The new value to set
            
        Raises:
            ValueError: If the value is invalid for this setting
        """
        if self.read_only:
            # Allow setting read-only values programmatically, but users shouldn't modify them
            pass
        
        if self.control == "comboList":
            # Validate against available values
            valid_ids = [v["id"] for v in self.values]
            if value not in valid_ids:
                raise ValueError(
                    f"Invalid value {value} for {self.id}. "
                    f"Must be one of {valid_ids}"
                )
        elif self.control == "spinbox":
            # Validate numeric range
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
            # No visibility condition means always visible
            return True
        
        # Parse visibility condition which can include AND/OR operators
        # Format: [{"id": "x", "value": 1}, "and", {"id": "y", "value": 2}]
        conditions = []
        operators = []
        
        for item in self.visibility_condition:
            if isinstance(item, str):
                # This is an operator (and/or)
                operators.append(item.lower())
            elif isinstance(item, dict):
                # This is a condition
                required_id = item["id"]
                required_value = item["value"]
                current_value = settings_values.get(required_id)
                conditions.append(current_value == required_value)
        
        if not conditions:
            return True
        
        # If no operators, all conditions must be true (implicit AND)
        if not operators:
            return all(conditions)
        
        # Evaluate conditions with operators
        # For now, support simple AND/OR chains
        result = conditions[0]
        for i, operator in enumerate(operators):
            if i + 1 < len(conditions):
                if operator == "and":
                    result = result and conditions[i + 1]
                elif operator == "or":
                    result = result or conditions[i + 1]
        
        return result
    
    def get_display_name(self) -> str:
        """Get the display name for the current value (for comboList controls)."""
        if self.control == "comboList":
            for value_dict in self.values:
                if value_dict["id"] == self._current_value:
                    return value_dict.get("dispName", str(self._current_value))
        return str(self._current_value)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert this setting back to a dictionary representation."""
        result = {
            "id": self.id,
            "label": self.label,
            "control": self.control,
            "baseDim": self.base_dim,
        }
        
        if self.dimension:
            result["dimension"] = self.dimension
        
        if self.read_only:
            result["readOnly"] = self.read_only
        
        if self.control == "comboList":
            result["values"] = self.values
            result["defValue"] = self.def_value
        elif self.control == "spinbox":
            result["defValue"] = self.def_value
            if self.min_value is not None:
                result["min"] = self.min_value
            if self.max_value is not None:
                result["max"] = self.max_value
        
        if self.visibility_condition:
            result["VisibilityCondition"] = self.visibility_condition
        
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
        # Use object.__setattr__ to bypass our custom __setattr__
        object.__setattr__(self, '_settings', {})
        
        # Create WeaponSetting objects for each setting
        for setting_dict in settings_list:
            setting = WeaponSetting(setting_dict)
            self._settings[setting.id] = setting
        
        # Initialize with default values
        self._update_visibility()
    
    def __getattr__(self, name: str) -> Any:
        """
        Allow attribute-style access to settings.
        
        Example:
            ws.NFP_fuze_type_nose  # instead of ws.get_value("NFP_fuze_type_nose")
        
        Args:
            name: The setting ID as an attribute name
            
        Returns:
            The current value of the setting
            
        Raises:
            AttributeError: If the setting doesn't exist
        """
        # Avoid infinite recursion for internal attributes
        if name.startswith('_'):
            return object.__getattribute__(self, name)
        
        # Check if this is a valid setting
        if name in self._settings:
            return self.get_value(name)
        
        raise AttributeError(f"WeaponSettings has no setting '{name}'")
    
    def __setattr__(self, name: str, value: Any) -> None:
        """
        Allow attribute-style setting of values.
        
        Example:
            ws.NFP_fuze_type_nose = 2  # instead of ws.set_value("NFP_fuze_type_nose", 2)
        
        Args:
            name: The setting ID as an attribute name
            value: The new value to set
            
        Raises:
            AttributeError: If the setting doesn't exist
            ValueError: If the value is invalid for this setting
        """
        # Internal attributes use normal attribute setting
        if name.startswith('_'):
            object.__setattr__(self, name, value)
            return
        
        # Check if this is a valid setting
        if name in self._settings:
            self.set_value(name, value)
        else:
            raise AttributeError(f"WeaponSettings has no setting '{name}'")
    
    def __getitem__(self, key: str) -> Any:
        """
        Allow dictionary-style access to settings.
        
        Example:
            ws["NFP_fuze_type_nose"]  # alternative syntax
        
        Args:
            key: The setting ID
            
        Returns:
            The current value of the setting
        """
        return self.get_value(key)
    
    def __setitem__(self, key: str, value: Any) -> None:
        """
        Allow dictionary-style setting of values.
        
        Example:
            ws["NFP_fuze_type_nose"] = 2  # alternative syntax
        
        Args:
            key: The setting ID
            value: The new value to set
        """
        self.set_value(key, value)
    
    def __dir__(self) -> List[str]:
        """
        Return list of available settings for autocomplete.
        
        This makes dir(ws) show all available setting IDs along with methods.
        """
        # Get default attributes/methods
        default_attrs = object.__dir__(self)
        # Add all setting IDs
        setting_ids = list(self._settings.keys())
        return sorted(default_attrs + setting_ids)
    
    def get_setting(self, setting_id: str) -> Optional[WeaponSetting]:
        """
        Get a setting object by ID.
        
        Args:
            setting_id: The ID of the setting to retrieve
            
        Returns:
            The WeaponSetting object, or None if not found
        """
        return self._settings.get(setting_id)
    
    def get_value(self, setting_id: str) -> Any:
        """
        Get the current value of a setting.
        
        Args:
            setting_id: The ID of the setting
            
        Returns:
            The current value of the setting
            
        Raises:
            KeyError: If the setting ID doesn't exist
        """
        if setting_id not in self._settings:
            raise KeyError(f"Setting '{setting_id}' not found")
        return self._settings[setting_id].current_value
    
    def set_value(self, setting_id: str, value: Any) -> None:
        """
        Set the value of a setting and update visibility of dependent settings.
        
        Args:
            setting_id: The ID of the setting to modify
            value: The new value to set
            
        Raises:
            KeyError: If the setting ID doesn't exist
            ValueError: If the value is invalid for this setting
        """
        if setting_id not in self._settings:
            raise KeyError(f"Setting '{setting_id}' not found")
        
        # Set the new value
        self._settings[setting_id].current_value = value
        
        # Update visibility of all settings
        self._update_visibility()
    
    def _update_visibility(self) -> None:
        """Update visibility state for all settings based on current values."""
        # Get current values for all settings
        current_values = {
            setting_id: setting.current_value
            for setting_id, setting in self._settings.items()
        }
        
        # Update visibility for each setting
        for setting in self._settings.values():
            setting._is_visible = setting.is_visible(current_values)
    
    def get_visible_settings(self) -> List[WeaponSetting]:
        """
        Get all currently visible settings.
        
        Returns:
            List of WeaponSetting objects that are currently visible
        """
        return [
            setting for setting in self._settings.values()
            if getattr(setting, '_is_visible', True)
        ]
    
    def get_adjustable_settings(self) -> List[WeaponSetting]:
        """
        Get all currently visible and adjustable (non-read-only) settings.
        
        Returns:
            List of WeaponSetting objects that are visible and adjustable
        """
        return [
            setting for setting in self.get_visible_settings()
            if not setting.read_only
        ]
    
    def is_visible(self, setting_id: str) -> bool:
        """
        Check if a setting is currently visible.
        
        Args:
            setting_id: The ID of the setting to check
            
        Returns:
            True if the setting is visible, False otherwise
        """
        setting = self._settings.get(setting_id)
        if not setting:
            return False
        return getattr(setting, '_is_visible', True)
    
    def is_adjustable(self, setting_id: str) -> bool:
        """
        Check if a setting is currently adjustable (visible and not read-only).
        
        Args:
            setting_id: The ID of the setting to check
            
        Returns:
            True if the setting is adjustable, False otherwise
        """
        if not self.is_visible(setting_id):
            return False
        setting = self._settings.get(setting_id)
        return setting and not setting.read_only
    
    def to_lua_table(self) -> Dict[str, Any]:
        """
        Serialize to Lua table format (for mission file).
        
        Only includes visible settings with non-default values or all settings
        depending on requirements.
        
        Returns:
            Dictionary suitable for Lua table serialization
        """
        result = {}
        for setting_id, setting in self._settings.items():
            # Include all settings that are visible
            if getattr(setting, '_is_visible', True):
                result[setting_id] = setting.current_value
        return result
    
    def from_lua_table(self, lua_table: Dict[str, Any]) -> None:
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
                    print(f"Warning: Could not set {setting_id} to {value}: {e}")
    
    def reset_to_defaults(self) -> None:
        """Reset all settings to their default values."""
        for setting in self._settings.values():
            setting.current_value = setting.def_value
        self._update_visibility()
    
    def to_dict_list(self) -> List[Dict[str, Any]]:
        """
        Convert back to original dictionary list format.
        
        Returns:
            List of setting dictionaries
        """
        return [setting.to_dict() for setting in self._settings.values()]
