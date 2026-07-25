# This file is generated from pydcs_export.lua
# Contains deduplicated weapon settings data referenced by hash


weapon_settings_registry = {
    # Used by 1 weapon(s): AB_500_1___34_x_SD_10A__500kg_CBU_with_10kg_Frag_HE_submunitions
    "01c38ded": [
        {
            "id": "NFP_fuze_type",
            "label": "Fuze Type",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Zünder 69E"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_function_delay_ctrl_oV_Z69E",
            "label": "oV Mode Function Delay",
            "control": "spinbox",
            "defValue": 4,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        },
        {
            "id": "02_prfx_function_delay_ctrl_mV_Z69E",
            "label": "mV Mode Function Delay",
            "control": "spinbox",
            "defValue": 5.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_Strz_Z69E",
            "label": "Sturz Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        },
        {
            "id": "02_prfx_arm_delay_ctrl_Wgrcht_Z69E",
            "label": "Wagerecht Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        },
        {
            "id": "NFP_subm_fuze_type",
            "label": "Submunition Fuze Type",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Zünder 3"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "04_prfx_subm_arm_delay_ctrl_Z3",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 2.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_subm_fuze_type", "value": 1}],
        },
        {
            "id": "04_prfx_subm_func_delay_ctrl_Z3",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 6,
                    "dispName": "6"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_subm_fuze_type", "value": 1}],
        }
    ],
    # Used by 12 weapon(s): _250_lb_GP_Mk_IV, _250_lb_GP_Mk_IV_, _250_lb_MC_Mk_I, _250_lb_MC_Mk_II, _250_lb_MC_Mk_II_
    # ... and 7 more
    "0352ac12": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Nose Pistol No. 27 Mk II"
                },
                {
                    "id": "EMPTY_NOSE",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_NP27MkII",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 7,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_NP27MkII",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 1,
                    "dispName": "1"
                },
                {
                    "id": 11,
                    "dispName": "11"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Tail Pistol No. 30 Mk III"
                },
                {
                    "id": "EMPTY_TAIL",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_vane_rev_threshold_ctrl_TP30MkIII",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 13,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_TP30MkIII",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.12,
                    "dispName": "0.12"
                },
                {
                    "id": 1,
                    "dispName": "1"
                },
                {
                    "id": 11,
                    "dispName": "11"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        }
    ],
    # Used by 2 weapon(s): AN_M65___1000lb_GP_Bomb_LD, AN_M66___2000lb_GP_Bomb_LD
    "05bf1d4c": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "AN-M103A1"
                },
                {
                    "id": 2,
                    "dispName": "Mk 243 Mod 0"
                },
                {
                    "id": 3,
                    "dispName": "Mk 244 Mod 1"
                },
                {
                    "id": 4,
                    "dispName": "M135A1"
                },
                {
                    "id": 5,
                    "dispName": "M136A1"
                },
                {
                    "id": 6,
                    "dispName": "AN-M139A1"
                },
                {
                    "id": 7,
                    "dispName": "AN-M140A1"
                },
                {
                    "id": "EMPTY_NOSE",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_M136A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 260,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 5}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_M135A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 260,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 4}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_FD_0_ANM139A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 330,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 6}, "and", {"id": "00_prfx_function_delay_ctrl_ANM139A1", "value": 0}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_FD_0.025_ANM140A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 220,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 7}, "and", {"id": "00_prfx_function_delay_ctrl_ANM140A1", "value": 0.025}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_FD_0_ANM140A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 330,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 7}, "and", {"id": "00_prfx_function_delay_ctrl_ANM140A1", "value": 0}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_Mk244Mod1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 130,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 3}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_FD_0.01_ANM139A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 220,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 6}, "and", {"id": "00_prfx_function_delay_ctrl_ANM139A1", "value": 0.01}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_FD_0.1_ANM103A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 180,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}, "and", {"id": "00_prfx_function_delay_ctrl_ANM103A1", "value": 0.1}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_FD_0_ANM103A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 300,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}, "and", {"id": "00_prfx_function_delay_ctrl_ANM103A1", "value": 0}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_Mk243Mod0",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 130,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 2}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_Mk244Mod1",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 4,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 3}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_ANM140A1",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 7}],
        },
        {
            "id": "00_prfx_self_destruct_delay_ctrl_M135A1",
            "label": "Airburst Delay",
            "control": "spinbox",
            "defValue": 5,
            "min": 5,
            "max": 92,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 4}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_ANM139A1",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 6}],
        },
        {
            "id": "00_prfx_self_destruct_delay_ctrl_M136A1",
            "label": "Airburst Delay",
            "control": "spinbox",
            "defValue": 5,
            "min": 5,
            "max": 30.6,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 5}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_Mk243Mod0",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 0.025,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "ms",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 2}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_ANM103A1",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "AN-M102A2"
                },
                {
                    "id": 2,
                    "dispName": "AN-M117"
                },
                {
                    "id": 3,
                    "dispName": "AN-M125A1"
                },
                {
                    "id": 4,
                    "dispName": "AN-M134"
                },
                {
                    "id": 5,
                    "dispName": "M162"
                },
                {
                    "id": "EMPTY_TAIL",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_vane_rev_threshold_ctrl_M162",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 720,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 5}],
        },
        {
            "id": "01_prfx_vane_rev_threshold_ctrl_ANM117",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 160,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 2}],
        },
        {
            "id": "01_prfx_vane_rev_threshold_ctrl_ANM134",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 72,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 4}],
        },
        {
            "id": "01_prfx_vane_rev_threshold_ctrl_ANM102A2",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 160,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        },
        {
            "id": "01_prfx_vane_rev_threshold_ctrl_ANM125A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 6,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 3}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_ANM134",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 600,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "min",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 4}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_ANM125A1",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 3600,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "h",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 3}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_ANM117",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 5,
            "values": [
                {
                    "id": 5,
                    "dispName": "5"
                },
                {
                    "id": 11,
                    "dispName": "11"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 2}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_M162",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 5}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_ANM102A2",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        }
    ],
    # Used by 5 weapon(s): British_GP_250LBS_Bomb_MK4_on_LH_Spitfire_Wing_Carrier, British_GP_250LBS_Bomb_MK4_on_RH_Spitfire_Wing_Carrier, British_GP_500LBS_Bomb_MK4_on_British_UniversalBC_MK3, _250_lb_GP_Mk_I, _500_lb_GP_Mk_I
    "0731cf13": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Nose Pistol No. 19"
                },
                {
                    "id": "EMPTY_NOSE",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_NP19",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 6,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_NP19",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 1,
                    "dispName": "1"
                },
                {
                    "id": 2.5,
                    "dispName": "2.5"
                },
                {
                    "id": 12,
                    "dispName": "12"
                },
                {
                    "id": 15,
                    "dispName": "15"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Tail Pistol No. 17 Mk I"
                },
                {
                    "id": "EMPTY_TAIL",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_vane_rev_threshold_ctrl_TP17MkI",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 8,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_TP17MkI",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 1800,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "h",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        }
    ],
    # Used by 2 weapon(s): AN_M64___500lb_GP_Bomb_LD, AN_M64___500lb_GP_Bomb_LD_
    "0f63aa9d": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "AN-M103A1"
                },
                {
                    "id": 2,
                    "dispName": "Mk 243 Mod 0"
                },
                {
                    "id": 3,
                    "dispName": "Mk 244 Mod 1"
                },
                {
                    "id": 4,
                    "dispName": "M135A1"
                },
                {
                    "id": 5,
                    "dispName": "M136A1"
                },
                {
                    "id": 6,
                    "dispName": "AN-M139A1"
                },
                {
                    "id": 7,
                    "dispName": "AN-M140A1"
                },
                {
                    "id": "EMPTY_NOSE",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_M136A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 260,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 5}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_M135A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 260,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 4}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_FD_0_ANM139A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 330,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 6}, "and", {"id": "00_prfx_function_delay_ctrl_ANM139A1", "value": 0}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_FD_0.025_ANM140A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 220,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 7}, "and", {"id": "00_prfx_function_delay_ctrl_ANM140A1", "value": 0.025}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_FD_0_ANM140A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 330,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 7}, "and", {"id": "00_prfx_function_delay_ctrl_ANM140A1", "value": 0}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_Mk244Mod1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 130,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 3}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_FD_0.01_ANM139A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 220,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 6}, "and", {"id": "00_prfx_function_delay_ctrl_ANM139A1", "value": 0.01}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_FD_0.1_ANM103A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 180,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}, "and", {"id": "00_prfx_function_delay_ctrl_ANM103A1", "value": 0.1}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_FD_0_ANM103A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 300,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}, "and", {"id": "00_prfx_function_delay_ctrl_ANM103A1", "value": 0}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_Mk243Mod0",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 130,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 2}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_Mk244Mod1",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 4,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 3}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_ANM140A1",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 7}],
        },
        {
            "id": "00_prfx_self_destruct_delay_ctrl_M135A1",
            "label": "Airburst Delay",
            "control": "spinbox",
            "defValue": 5,
            "min": 5,
            "max": 92,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 4}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_ANM139A1",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 6}],
        },
        {
            "id": "00_prfx_self_destruct_delay_ctrl_M136A1",
            "label": "Airburst Delay",
            "control": "spinbox",
            "defValue": 5,
            "min": 5,
            "max": 30.6,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 5}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_Mk243Mod0",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 0.025,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "ms",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 2}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_ANM103A1",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "AN-M101A2"
                },
                {
                    "id": 2,
                    "dispName": "AN-M116"
                },
                {
                    "id": 3,
                    "dispName": "AN-M124A1"
                },
                {
                    "id": 4,
                    "dispName": "AN-M133"
                },
                {
                    "id": 5,
                    "dispName": "M161"
                },
                {
                    "id": "EMPTY_TAIL",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_vane_rev_threshold_ctrl_M161",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 720,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 5}],
        },
        {
            "id": "01_prfx_vane_rev_threshold_ctrl_ANM116",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 160,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 2}],
        },
        {
            "id": "01_prfx_vane_rev_threshold_ctrl_ANM133",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 72,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 4}],
        },
        {
            "id": "01_prfx_vane_rev_threshold_ctrl_ANM101A2",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 160,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        },
        {
            "id": "01_prfx_vane_rev_threshold_ctrl_ANM124A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 6,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 3}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_ANM133",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 600,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "min",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 4}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_ANM124A1",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 3600,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "h",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 3}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_ANM116",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 5,
            "values": [
                {
                    "id": 5,
                    "dispName": "5"
                },
                {
                    "id": 11,
                    "dispName": "11"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 2}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_M161",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 5}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_ANM101A2",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        }
    ],
    # Used by 2 weapon(s): AN_M30A1___100lb_GP_Bomb_LD, AN_M57___250lb_GP_Bomb_LD
    "190837ee": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "AN-M103A1"
                },
                {
                    "id": 2,
                    "dispName": "Mk 243 Mod 0"
                },
                {
                    "id": 3,
                    "dispName": "Mk 244 Mod 1"
                },
                {
                    "id": 4,
                    "dispName": "M135A1"
                },
                {
                    "id": 5,
                    "dispName": "M136A1"
                },
                {
                    "id": 6,
                    "dispName": "AN-M139A1"
                },
                {
                    "id": 7,
                    "dispName": "AN-M140A1"
                },
                {
                    "id": "EMPTY_NOSE",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_M136A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 260,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 5}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_M135A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 260,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 4}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_FD_0_ANM139A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 330,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 6}, "and", {"id": "00_prfx_function_delay_ctrl_ANM139A1", "value": 0}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_FD_0.025_ANM140A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 220,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 7}, "and", {"id": "00_prfx_function_delay_ctrl_ANM140A1", "value": 0.025}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_FD_0_ANM140A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 330,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 7}, "and", {"id": "00_prfx_function_delay_ctrl_ANM140A1", "value": 0}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_Mk244Mod1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 130,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 3}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_FD_0.01_ANM139A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 220,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 6}, "and", {"id": "00_prfx_function_delay_ctrl_ANM139A1", "value": 0.01}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_FD_0.1_ANM103A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 180,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}, "and", {"id": "00_prfx_function_delay_ctrl_ANM103A1", "value": 0.1}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_FD_0_ANM103A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 300,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}, "and", {"id": "00_prfx_function_delay_ctrl_ANM103A1", "value": 0}],
        },
        {
            "id": "00_prfx_vane_rev_threshold_ctrl_Mk243Mod0",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 130,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 2}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_Mk244Mod1",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 4,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 3}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_ANM140A1",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 7}],
        },
        {
            "id": "00_prfx_self_destruct_delay_ctrl_M135A1",
            "label": "Airburst Delay",
            "control": "spinbox",
            "defValue": 5,
            "min": 5,
            "max": 92,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 4}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_ANM139A1",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 6}],
        },
        {
            "id": "00_prfx_self_destruct_delay_ctrl_M136A1",
            "label": "Airburst Delay",
            "control": "spinbox",
            "defValue": 5,
            "min": 5,
            "max": 30.6,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 5}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_Mk243Mod0",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 0.025,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "ms",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 2}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_ANM103A1",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "AN-M100A2"
                },
                {
                    "id": 2,
                    "dispName": "AN-M115"
                },
                {
                    "id": 3,
                    "dispName": "AN-M123A1"
                },
                {
                    "id": 4,
                    "dispName": "AN-M132"
                },
                {
                    "id": 5,
                    "dispName": "M160"
                },
                {
                    "id": "EMPTY_TAIL",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_vane_rev_threshold_ctrl_M160",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 720,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 5}],
        },
        {
            "id": "01_prfx_vane_rev_threshold_ctrl_ANM115",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 160,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 2}],
        },
        {
            "id": "01_prfx_vane_rev_threshold_ctrl_ANM132",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 72,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 4}],
        },
        {
            "id": "01_prfx_vane_rev_threshold_ctrl_ANM100A2",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 160,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        },
        {
            "id": "01_prfx_vane_rev_threshold_ctrl_ANM123A1",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 6,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 3}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_ANM132",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 600,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "min",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 4}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_ANM123A1",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 3600,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "h",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 3}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_ANM115",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 5,
            "values": [
                {
                    "id": 5,
                    "dispName": "5"
                },
                {
                    "id": 11,
                    "dispName": "11"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 2}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_M160",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 5}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_ANM100A2",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        }
    ],
    # Used by 4 weapon(s): ER_4_SC50, SC_250_Type_1_L2___250kg_GP_Bomb_LD, SC_250_Type_3_J___250kg_GP_Bomb_LD, SC_501_SC250
    "265ba940": [
        {
            "id": "NFP_fuze_type",
            "label": "Fuze Type",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Zünder 25C"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "NFP_fuze_operation_mode",
            "label": "Function Delay Mode",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Variable"
                },
                {
                    "id": 2,
                    "dispName": "Fixed"
                }
            ],
            "baseDim": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_oV_VFD_Z25C",
            "label": "oV Mode Function Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 1}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_oV_FFD_Z25C",
            "label": "oV Mode Function Delay",
            "control": "spinbox",
            "defValue": 8.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 2}],
        },
        {
            "id": "02_prfx_function_delay_ctrl_mV_FFD_Z25C",
            "label": "mV Mode Function Delay",
            "control": "spinbox",
            "defValue": 8.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 2}],
        },
        {
            "id": "02_prfx_function_delay_ctrl_mV_VFD_Z25C",
            "label": "mV Mode Function Delay",
            "control": "spinbox",
            "defValue": 0.08,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "ms",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 1}],
        },
        {
            "id": "03_prfx_function_delay_ctrl_Vz_FFD_Z25C",
            "label": "Vz Mode Function Delay",
            "control": "spinbox",
            "defValue": 8.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 2}],
        },
        {
            "id": "03_prfx_function_delay_ctrl_Vz_VFD_Z25C",
            "label": "Vz Mode Function Delay",
            "control": "spinbox",
            "defValue": 8.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 1}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_Strz_VFD_Z25C",
            "label": "Sturz Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0.08,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "ms",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 1}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_Strz_FFD_Z25C",
            "label": "Sturz Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0.08,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "ms",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 2}],
        },
        {
            "id": "02_prfx_arm_delay_ctrl_Wgrcht_FFD_Z25C",
            "label": "Wagerecht Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0.08,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "ms",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 2}],
        },
        {
            "id": "02_prfx_arm_delay_ctrl_Wgrcht_VFD_Z25C",
            "label": "Wagerecht Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0.08,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "ms",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 1}],
        }
    ],
    # Used by 9 weapon(s): B_1B_Mk_84_8, MK_82_28, _1x_Mk_81___250lb_GP_Bomb_LD__TER_, _1x_Mk_82___500lb_GP_Bomb_LD__TER_, _27_x_Mk_82___500lb_GP_Bomb_LD
    # ... and 4 more
    "2abf3266": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": "M904E4",
            "values": [
                {
                    "id": "M904E4",
                    "dispName": "M904E4"
                },
                {
                    "id": "DSU33",
                    "dispName": "DSU-33"
                },
                {
                    "id": "EMPTY_NOSE",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "NFP_VIS_DrawArgNo_56",
            "label": "Plug",
            "control": "comboList",
            "defValue": 0.5,
            "values": [
                {
                    "id": 0.1,
                    "dispName": "Long Conical"
                },
                {
                    "id": 0.4,
                    "dispName": "Short Conical"
                },
                {
                    "id": 0.5,
                    "dispName": "MXU-735"
                }
            ],
            "baseDim": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "bNot": True, "value": "DSU33"}, "and", {"id": "NFP_fuze_type_nose", "bNot": True, "value": "M904E4"}],
        },
        {
            "id": "00_prfx_function_altitude_ctrl_DSU33",
            "label": "Airburst Height",
            "control": "spinbox",
            "defValue": 6.096,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "ft",
            "dimension": "ft",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "DSU33"}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_M904E4",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 4,
            "min": 2,
            "max": 18,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "M904E4"}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_M904E4",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.05,
                    "dispName": "0.05"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.25,
                    "dispName": "0.25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "M904E4"}],
        },
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": "M905",
            "values": [
                {
                    "id": "M905",
                    "dispName": "M905"
                },
                {
                    "id": "FMU139CB_LD",
                    "dispName": "FMU-139"
                },
                {
                    "id": "FMU152AB_LD",
                    "dispName": "FMU-152"
                },
                {
                    "id": "EMPTY_TAIL",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU152AB_LD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 5,
                    "dispName": "5"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 7,
                    "dispName": "7"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 14,
                    "dispName": "14"
                },
                {
                    "id": 21,
                    "dispName": "21"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU139CB_LD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 7,
                    "dispName": "7"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 14,
                    "dispName": "14"
                },
                {
                    "id": 20,
                    "dispName": "20"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_LD"}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_M905",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 12,
                    "dispName": "12"
                },
                {
                    "id": 16,
                    "dispName": "16"
                },
                {
                    "id": 20,
                    "dispName": "20"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "M905"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_M905",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.05,
                    "dispName": "0.05"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.25,
                    "dispName": "0.25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "M905"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU139CB_LD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.06,
                    "dispName": "0.06"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_LD"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU152AB_LD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.005,
                    "dispName": "5 ms"
                },
                {
                    "id": 0.025,
                    "dispName": "25 ms"
                },
                {
                    "id": 0.06,
                    "dispName": "60 ms"
                },
                {
                    "id": 0.18,
                    "dispName": "180 ms"
                },
                {
                    "id": 900,
                    "dispName": "15 min"
                },
                {
                    "id": 14400,
                    "dispName": "4 h"
                },
                {
                    "id": 86400,
                    "dispName": "24 h"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        }
    ],
    # Used by 13 weapon(s): CSRL___8_x_GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb, CSRL___8_x_GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb, GBU_31_8, GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb, GBU_38_16
    # ... and 8 more
    "2d91936f": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": "EMPTY_NOSE",
            "values": [
                {
                    "id": "DSU33",
                    "dispName": "DSU-33"
                },
                {
                    "id": "EMPTY_NOSE",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "NFP_VIS_DrawArgNo_56",
            "label": "Plug",
            "control": "comboList",
            "defValue": 0.5,
            "values": [
                {
                    "id": 0.1,
                    "dispName": "Long Conical"
                },
                {
                    "id": 0.4,
                    "dispName": "Short Conical"
                },
                {
                    "id": 0.5,
                    "dispName": "MXU-735"
                }
            ],
            "baseDim": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "bNot": True, "value": "DSU33"}, "and", {"id": "NFP_fuze_type_nose", "bNot": True, "value": "M904E4"}],
        },
        {
            "id": "00_prfx_function_altitude_ctrl_DSU33",
            "label": "Airburst Height",
            "control": "spinbox",
            "defValue": 6.096,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "ft",
            "dimension": "ft",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "DSU33"}],
        },
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": "FMU139CB_LD",
            "values": [
                {
                    "id": "FMU139CB_LD",
                    "dispName": "FMU-139"
                },
                {
                    "id": "FMU152AB_LD",
                    "dispName": "FMU-152"
                },
                {
                    "id": "EMPTY_TAIL",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU152AB_LD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 5,
                    "dispName": "5"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 7,
                    "dispName": "7"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 14,
                    "dispName": "14"
                },
                {
                    "id": 21,
                    "dispName": "21"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU139CB_LD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 7,
                    "dispName": "7"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 14,
                    "dispName": "14"
                },
                {
                    "id": 20,
                    "dispName": "20"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_LD"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU139CB_LD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.06,
                    "dispName": "0.06"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_LD"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU152AB_LD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.005,
                    "dispName": "5 ms"
                },
                {
                    "id": 0.025,
                    "dispName": "25 ms"
                },
                {
                    "id": 0.06,
                    "dispName": "60 ms"
                },
                {
                    "id": 0.18,
                    "dispName": "180 ms"
                },
                {
                    "id": 900,
                    "dispName": "15 min"
                },
                {
                    "id": 14400,
                    "dispName": "4 h"
                },
                {
                    "id": 86400,
                    "dispName": "24 h"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        }
    ],
    # Used by 8 weapon(s): BL_755_CBU___450kg__147_Frag_Pen_bomblets, _1x_BL_755___147_Frag_Pen_bomblets__TER_, _1x_BL_755___147_Frag_Pen_bomblets__TER__, _2x_BL_755___147_Frag_Pen_bomblets__TER_, _2x_BL_755___147_Frag_Pen_bomblets__TER__
    # ... and 3 more
    "3e8e39b5": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Integral Fuze Mk 1"
                },
                {
                    "id": 2,
                    "dispName": "Integral Fuze Mk 2"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "00_prfx_function_delay_ctrl_BL755_IF_Mk1",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 1.13,
            "values": [
                {
                    "id": 1.13,
                    "dispName": "1.13"
                },
                {
                    "id": 1.38,
                    "dispName": "1.38"
                },
                {
                    "id": 1.64,
                    "dispName": "1.64"
                },
                {
                    "id": 2,
                    "dispName": "2"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_BL755_IF_Mk2",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0.68,
            "values": [
                {
                    "id": 0.68,
                    "dispName": "0.68"
                },
                {
                    "id": 0.8,
                    "dispName": "0.8"
                },
                {
                    "id": 0.94,
                    "dispName": "0.94"
                },
                {
                    "id": 1.13,
                    "dispName": "1.13"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 2}],
        }
    ],
    # Used by 2 weapon(s): SAB_100MN___100_kg_Illumination_Bomb, SAB_250_200___200_kg_Illumination_Bomb
    "48994ad3": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "ATM-E"
                },
                {
                    "id": 2,
                    "dispName": "AT-E"
                },
                {
                    "id": 3,
                    "dispName": "TM-24 + MDV-4"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "00_prfx_arm_delay_ctrl_ATE",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 7.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 2}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_ATME",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 2,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_TM24",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 2.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 3}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_ATME",
            "label": "Airburst Delay",
            "control": "spinbox",
            "defValue": 4,
            "min": 4,
            "max": 150,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_TM24",
            "label": "Airburst Delay",
            "control": "spinbox",
            "defValue": 6,
            "min": 6,
            "max": 60,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 3}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_ATE",
            "label": "Airburst Delay",
            "control": "spinbox",
            "defValue": 10,
            "min": 10,
            "max": 150,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 2}],
        }
    ],
    # Used by 2 weapon(s): GBU_24, GBU_24B_B_Paveway_III___2000lb_Laser_Guided_Bomb
    "4a65f01a": [
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": "FMU143",
            "values": [
                {
                    "id": "FMU143",
                    "dispName": "FMU-143"
                },
                {
                    "id": "FMU152AB_LD",
                    "dispName": "FMU-152"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU152AB_LD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 5,
                    "dispName": "5"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 7,
                    "dispName": "7"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 14,
                    "dispName": "14"
                },
                {
                    "id": 21,
                    "dispName": "21"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU143",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 5.5,
            "values": [
                {
                    "id": 5.5,
                    "dispName": "5.5"
                },
                {
                    "id": 12,
                    "dispName": "12"
                },
                {
                    "id": 21,
                    "dispName": "21"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU143"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU152AB_LD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.005,
                    "dispName": "5 ms"
                },
                {
                    "id": 0.025,
                    "dispName": "25 ms"
                },
                {
                    "id": 0.06,
                    "dispName": "60 ms"
                },
                {
                    "id": 0.18,
                    "dispName": "180 ms"
                },
                {
                    "id": 900,
                    "dispName": "15 min"
                },
                {
                    "id": 14400,
                    "dispName": "4 h"
                },
                {
                    "id": 86400,
                    "dispName": "24 h"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU143",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0.03,
            "values": [
                {
                    "id": 0.03,
                    "dispName": "30 ms"
                },
                {
                    "id": 0.06,
                    "dispName": "60 ms"
                },
                {
                    "id": 0.12,
                    "dispName": "120 ms"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU143"}],
        },
        {
            "id": "laser_code",
            "label": "Laser Designator PRF Code",
            "control": "laserCode",
            "defValue": 1688,
        },
        {
            "id": "NFP_VIS_DrawArgNo_57",
            "label": "Appearance",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "USN"
                }
            ],
            "baseDim": "",
        }
    ],
    # Used by 10 weapon(s): BRU_57_with_2_x_CBU_105___10_x_SFW__CBU_with_WCMD, CBU97_10, CBU_105___10_x_SFW__CBU_with_WCMD, CBU_97___10_x_SFW_Cluster_Bomb, HSAB___8_x_CBU_105___10_x_SFW__CBU_with_WCMD
    # ... and 5 more
    "567459a6": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": "FZU39",
            "values": [
                {
                    "id": "FZU39",
                    "dispName": "Integral Fuze + FZU-39"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "function_delay_ctrl_FZU39_SUU65_SFW",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 2.23,
            "values": [
                {
                    "id": 0.63,
                    "dispName": "0.63"
                },
                {
                    "id": 0.95,
                    "dispName": "0.95"
                },
                {
                    "id": 1.28,
                    "dispName": "1.28"
                },
                {
                    "id": 1.6,
                    "dispName": "1.6"
                },
                {
                    "id": 1.92,
                    "dispName": "1.92"
                },
                {
                    "id": 2.23,
                    "dispName": "2.23"
                },
                {
                    "id": 2.55,
                    "dispName": "2.55"
                },
                {
                    "id": 2.87,
                    "dispName": "2.87"
                },
                {
                    "id": 3.19,
                    "dispName": "3.19"
                },
                {
                    "id": 3.51,
                    "dispName": "3.51"
                },
                {
                    "id": 3.83,
                    "dispName": "3.83"
                },
                {
                    "id": 4.15,
                    "dispName": "4.15"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "FZU39"}],
        },
        {
            "id": "function_altitude_ctrl_FZU39_SUU65_SFW",
            "label": "Airburst Height",
            "control": "comboList",
            "defValue": 1500,
            "values": [
                {
                    "id": 900,
                    "dispName": "900"
                },
                {
                    "id": 1200,
                    "dispName": "1200"
                },
                {
                    "id": 1500,
                    "dispName": "1500"
                },
                {
                    "id": 1800,
                    "dispName": "1800"
                },
                {
                    "id": 2200,
                    "dispName": "2200"
                },
                {
                    "id": 2600,
                    "dispName": "2600"
                },
                {
                    "id": 3000,
                    "dispName": "3000"
                }
            ],
            "baseDim": "ft",
            "dimension": "ft",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "FZU39"}],
        }
    ],
    # Used by 6 weapon(s): Mk_83_AIR__BSU_85____1000_lb_GP_Chute_Retarded_Bomb_HD, Mk_84_AIR__BSU_50____2000_lb_GP_Chute_Retarded_Bomb_HD, _1x_Mk_82_Snakeye___500lb_GP_Bomb_HD__TER_, _27_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD, _2x_Mk_82_Snakeye___500lb_GP_Bomb_HD__TER___
    # ... and 1 more
    "57a5cd57": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": "M904E4",
            "values": [
                {
                    "id": "M904E4",
                    "dispName": "M904E4"
                },
                {
                    "id": "DSU33",
                    "dispName": "DSU-33"
                },
                {
                    "id": "EMPTY_NOSE",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "NFP_VIS_DrawArgNo_56",
            "label": "Plug",
            "control": "comboList",
            "defValue": 0.5,
            "values": [
                {
                    "id": 0.1,
                    "dispName": "Long Conical"
                },
                {
                    "id": 0.4,
                    "dispName": "Short Conical"
                },
                {
                    "id": 0.5,
                    "dispName": "MXU-735"
                }
            ],
            "baseDim": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "bNot": True, "value": "DSU33"}, "and", {"id": "NFP_fuze_type_nose", "bNot": True, "value": "M904E4"}],
        },
        {
            "id": "00_prfx_function_altitude_ctrl_DSU33",
            "label": "Airburst Height",
            "control": "spinbox",
            "defValue": 6.096,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "ft",
            "dimension": "ft",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "DSU33"}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_M904E4",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 4,
            "min": 2,
            "max": 18,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "M904E4"}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_M904E4",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.05,
                    "dispName": "0.05"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.25,
                    "dispName": "0.25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "M904E4"}],
        },
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": "M905",
            "values": [
                {
                    "id": "M905",
                    "dispName": "M905"
                },
                {
                    "id": "FMU139CB_HD",
                    "dispName": "FMU-139"
                },
                {
                    "id": "FMU152AB_HD",
                    "dispName": "FMU-152"
                },
                {
                    "id": "EMPTY_TAIL",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU139CB_HD_FD_0.025",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 2.6,
            "values": [
                {
                    "id": 2.6,
                    "dispName": "2.6"
                },
                {
                    "id": 4,
                    "dispName": "4"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_HD"}, "and", {"id": "01_prfx_function_delay_ctrl_FMU139CB_HD", "value": 0.025}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU139CB_HD_FD_0.01",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 2.6,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_HD"}, "and", {"id": "01_prfx_function_delay_ctrl_FMU139CB_HD", "value": 0.01}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_M905",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 12,
                    "dispName": "12"
                },
                {
                    "id": 16,
                    "dispName": "16"
                },
                {
                    "id": 20,
                    "dispName": "20"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "M905"}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU152AB_HD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 2,
            "values": [
                {
                    "id": 2,
                    "dispName": "2"
                },
                {
                    "id": 2.6,
                    "dispName": "2.6"
                },
                {
                    "id": 3,
                    "dispName": "3"
                },
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 5,
                    "dispName": "5"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_HD"}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU139CB_HD_FD_0.06",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 2.6,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_HD"}, "and", {"id": "01_prfx_function_delay_ctrl_FMU139CB_HD", "value": 0.06}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU139CB_HD_FD_0",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 2,
            "values": [
                {
                    "id": 2,
                    "dispName": "2"
                },
                {
                    "id": 2.6,
                    "dispName": "2.6"
                },
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 5,
                    "dispName": "5"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_HD"}, "and", {"id": "01_prfx_function_delay_ctrl_FMU139CB_HD", "value": 0}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU152AB_HD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.005,
                    "dispName": "5 ms"
                },
                {
                    "id": 0.025,
                    "dispName": "25 ms"
                },
                {
                    "id": 0.06,
                    "dispName": "60 ms"
                },
                {
                    "id": 0.18,
                    "dispName": "180 ms"
                },
                {
                    "id": 900,
                    "dispName": "15 min"
                },
                {
                    "id": 14400,
                    "dispName": "4 h"
                },
                {
                    "id": 86400,
                    "dispName": "24 h"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_HD"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_M905",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.05,
                    "dispName": "0.05"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.25,
                    "dispName": "0.25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "M905"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU139CB_HD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.06,
                    "dispName": "0.06"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_HD"}],
        }
    ],
    # Used by 2 weapon(s): SC_500_L2___500kg_GP_Bomb_LD, SC_501_SC500
    "64840f71": [
        {
            "id": "NFP_fuze_type",
            "label": "Fuze Type",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Zünder 38"
                },
                {
                    "id": 2,
                    "dispName": "Zünder 17"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "NFP_fuze_operation_mode",
            "label": "Function Delay Mode",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Variable"
                },
                {
                    "id": 2,
                    "dispName": "Fixed"
                }
            ],
            "baseDim": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_oV_VFD_Z38",
            "label": "oV Mode Function Delay",
            "control": "spinbox",
            "defValue": 0.05,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "ms",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 1}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_oV_Z17",
            "label": "oV Mode Function Delay",
            "control": "spinbox",
            "defValue": 180,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "min",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 2}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_oV_FFD_Z38",
            "label": "oV Mode Function Delay",
            "control": "spinbox",
            "defValue": 5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 2}],
        },
        {
            "id": "02_prfx_function_delay_ctrl_mV_FFD_Z38",
            "label": "mV Mode Function Delay",
            "control": "spinbox",
            "defValue": 5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 2}],
        },
        {
            "id": "02_prfx_function_delay_ctrl_mV_VFD_Z38",
            "label": "mV Mode Function Delay",
            "control": "spinbox",
            "defValue": 0.2,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "ms",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 1}],
        },
        {
            "id": "02_prfx_function_delay_ctrl_mV_Z17",
            "label": "mV Mode Function Delay",
            "control": "spinbox",
            "defValue": 180,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "min",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 2}],
        },
        {
            "id": "03_prfx_function_delay_ctrl_Vz_FFD_Z38",
            "label": "Vz Mode Function Delay",
            "control": "spinbox",
            "defValue": 5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 2}],
        },
        {
            "id": "03_prfx_function_delay_ctrl_Vz_Z17",
            "label": "Vz Mode Function Delay",
            "control": "spinbox",
            "defValue": 180,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "min",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 2}],
        },
        {
            "id": "03_prfx_function_delay_ctrl_Vz_VFD_Z38",
            "label": "Vz Mode Function Delay",
            "control": "spinbox",
            "defValue": 5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 1}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_Strz_FFD_Z38",
            "label": "Sturz Mode Arm Delay",
            "control": "spinbox",
            "defValue": 1,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 2}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_Strz_Z17",
            "label": "Sturz Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 2}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_Strz_VFD_Z38",
            "label": "Sturz Mode Arm Delay",
            "control": "spinbox",
            "defValue": 3,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 1}],
        },
        {
            "id": "02_prfx_arm_delay_ctrl_Wgrcht_VFD_Z38",
            "label": "Wagerecht Mode Arm Delay",
            "control": "spinbox",
            "defValue": 7.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 1}],
        },
        {
            "id": "02_prfx_arm_delay_ctrl_Wgrcht_FFD_Z38",
            "label": "Wagerecht Mode Arm Delay",
            "control": "spinbox",
            "defValue": 2,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 2}],
        },
        {
            "id": "02_prfx_arm_delay_ctrl_Wgrcht_Z17",
            "label": "Wagerecht Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 2}],
        }
    ],
    # Used by 2 weapon(s): BetAB_500ShP___500_kg_Concrete_Piercing_Bomb_HD_w_booster, BetAB_500ShP___500_kg_Concrete_Piercing_Bomb_HD_w_booster_
    "64ba4042": [
        {
            "id": "NFP_fuze_type",
            "label": "Fuze Type",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "AVU-589"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "arm_delay_ctrl_AVU589",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 4.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        },
        {
            "id": "function_delay_ctrl_AVU589",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 26,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        }
    ],
    # Used by 1 weapon(s): AB_250_2___144_x_SD_2__250kg_CBU_with_HE_submunitions
    "67c66429": [
        {
            "id": "NFP_fuze_type",
            "label": "Fuze Type",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Zünder 69D"
                },
                {
                    "id": 2,
                    "dispName": "Zünder 69E"
                },
                {
                    "id": 3,
                    "dispName": "Zünder 79"
                },
                {
                    "id": 4,
                    "dispName": "Zünder 79A"
                },
                {
                    "id": 5,
                    "dispName": "Zünder 89B"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "arm_delay_ctrl_Z89B",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 5}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_oV_Z69D",
            "label": "oV Mode Function Delay",
            "control": "spinbox",
            "defValue": 0.7,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_oV_Z79",
            "label": "oV Mode Function Delay",
            "control": "spinbox",
            "defValue": 3,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 3}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_oV_Z79A",
            "label": "oV Mode Function Delay",
            "control": "spinbox",
            "defValue": 3,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 4}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_oV_Z69E",
            "label": "oV Mode Function Delay",
            "control": "spinbox",
            "defValue": 4,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 2}],
        },
        {
            "id": "02_prfx_function_delay_ctrl_mV_Z79",
            "label": "mV Mode Function Delay",
            "control": "spinbox",
            "defValue": 30,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 3}],
        },
        {
            "id": "function_delay_ctrl_Z89B",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 4,
            "min": 3,
            "max": 60,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 5}],
        },
        {
            "id": "02_prfx_function_delay_ctrl_mV_Z79A",
            "label": "mV Mode Function Delay",
            "control": "spinbox",
            "defValue": 10,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 4}],
        },
        {
            "id": "02_prfx_function_delay_ctrl_mV_Z69E",
            "label": "mV Mode Function Delay",
            "control": "spinbox",
            "defValue": 5.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 2}],
        },
        {
            "id": "02_prfx_function_delay_ctrl_mV_Z69D",
            "label": "mV Mode Function Delay",
            "control": "spinbox",
            "defValue": 1.2,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_Strz_Z79",
            "label": "Sturz Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 3}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_Strz_Z79A",
            "label": "Sturz Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 4}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_Strz_Z69E",
            "label": "Sturz Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 2}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_Strz_Z69D",
            "label": "Sturz Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        },
        {
            "id": "02_prfx_arm_delay_ctrl_Wgrcht_Z79",
            "label": "Wagerecht Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 3}],
        },
        {
            "id": "02_prfx_arm_delay_ctrl_Wgrcht_Z79A",
            "label": "Wagerecht Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 4}],
        },
        {
            "id": "02_prfx_arm_delay_ctrl_Wgrcht_Z69D",
            "label": "Wagerecht Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        },
        {
            "id": "02_prfx_arm_delay_ctrl_Wgrcht_Z69E",
            "label": "Wagerecht Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 2}],
        },
        {
            "id": "NFP_subm_fuze_type",
            "label": "Submunition Fuze Type",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Zünder 41"
                },
                {
                    "id": 2,
                    "dispName": "Zünder 67"
                },
                {
                    "id": 3,
                    "dispName": "Zünder 70B"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "04_prfx_subm_arm_delay_ctrl_Z67",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_subm_fuze_type", "value": 2}],
        },
        {
            "id": "04_prfx_subm_arm_delay_ctrl_Z41",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 3.2,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_subm_fuze_type", "value": 1}],
        },
        {
            "id": "04_prfx_subm_arm_delay_ctrl_Z70B",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_subm_fuze_type", "value": 3}],
        },
        {
            "id": "04_prfx_subm_func_delay_ctrl_Z67",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 30,
            "baseDim": "min",
            "dimension": "min",
            "VisibilityCondition": [{"id": "NFP_subm_fuze_type", "value": 2}],
        },
        {
            "id": "04_prfx_subm_func_delay_ctrl_Z41",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_subm_fuze_type", "value": 1}],
        }
    ],
    # Used by 6 weapon(s): BRU_42_with_2_x_GBU_27___2000lb_Laser_Guided_Penetrator_Bombs, GBU_24A_B_Paveway_III___2000lb_Laser_Guided_Bomb, GBU_27___2000lb_Laser_Guided_Penetrator_Bomb, GBU_28___5000lb_Laser_Guided_Penetrator_Bomb, HSAB___2_x_GBU_28___5000lb_Laser_Guided_Penetrator_Bomb
    # ... and 1 more
    "6e51f8dc": [
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": "FMU143",
            "values": [
                {
                    "id": "FMU143",
                    "dispName": "FMU-143"
                },
                {
                    "id": "FMU152AB_LD",
                    "dispName": "FMU-152"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU143",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 5.5,
            "values": [
                {
                    "id": 5.5,
                    "dispName": "5.5"
                },
                {
                    "id": 12,
                    "dispName": "12"
                },
                {
                    "id": 21,
                    "dispName": "21"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU143"}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU152AB_LD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 5,
                    "dispName": "5"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 7,
                    "dispName": "7"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 14,
                    "dispName": "14"
                },
                {
                    "id": 21,
                    "dispName": "21"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU143",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0.03,
            "values": [
                {
                    "id": 0.03,
                    "dispName": "30 ms"
                },
                {
                    "id": 0.06,
                    "dispName": "60 ms"
                },
                {
                    "id": 0.12,
                    "dispName": "120 ms"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU143"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU152AB_LD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.005,
                    "dispName": "5 ms"
                },
                {
                    "id": 0.025,
                    "dispName": "25 ms"
                },
                {
                    "id": 0.06,
                    "dispName": "60 ms"
                },
                {
                    "id": 0.18,
                    "dispName": "180 ms"
                },
                {
                    "id": 900,
                    "dispName": "15 min"
                },
                {
                    "id": 14400,
                    "dispName": "4 h"
                },
                {
                    "id": 86400,
                    "dispName": "24 h"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        },
        {
            "id": "laser_code",
            "label": "Laser Designator PRF Code",
            "control": "laserCode",
            "defValue": 1688,
        }
    ],
    # Used by 14 weapon(s): MBD3_U6_68___6_x_RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP, RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag, RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag_, RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP, RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP_
    # ... and 9 more
    "73f4b923": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "ATM-E"
                },
                {
                    "id": 2,
                    "dispName": "AT-E"
                },
                {
                    "id": 3,
                    "dispName": "ATK-10E"
                },
                {
                    "id": 4,
                    "dispName": "TM-24 + MDV-4"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "00_prfx_arm_delay_ctrl_ATK10E",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 0.6,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 3}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_ATME",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 2,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_ATE",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 7.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 2}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_TM24",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 2.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 4}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_ATE",
            "label": "Airburst Delay",
            "control": "spinbox",
            "defValue": 10,
            "min": 10,
            "max": 150,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 2}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_ATME",
            "label": "Airburst Delay",
            "control": "spinbox",
            "defValue": 4,
            "min": 4,
            "max": 150,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_ATK10E",
            "label": "Airburst Delay",
            "control": "spinbox",
            "defValue": 1.2,
            "min": 1.2,
            "max": 10.2,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 3}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_TM24",
            "label": "Airburst Delay",
            "control": "spinbox",
            "defValue": 6,
            "min": 6,
            "max": 60,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 4}],
        }
    ],
    # Used by 20 weapon(s): DIS_BOMB_250_2, DIS_BOMB_250_3, DIS_H6_250_2_N12, DIS_H6_250_2_N24, DIS_MER6_250_2_N6
    # ... and 15 more
    "770158f1": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "AVU-E"
                },
                {
                    "id": 2,
                    "dispName": "BNV-1E"
                },
                {
                    "id": 3,
                    "dispName": "BRV-2"
                },
                {
                    "id": 4,
                    "dispName": "AMV"
                },
                {
                    "id": 5,
                    "dispName": "AV-2E"
                },
                {
                    "id": 6,
                    "dispName": "AVShE"
                },
                {
                    "id": 7,
                    "dispName": "AVT-E"
                },
                {
                    "id": "EMPTY_NOSE",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "00_prfx_arm_delay_ctrl_AMV",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 1.9,
            "values": [
                {
                    "id": 1.9,
                    "dispName": "1.9"
                },
                {
                    "id": 11.5,
                    "dispName": "11.5"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 4}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_AV2E_NOSE",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 1.8,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 5}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_AVTE_NOSE",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 4.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 7}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_BRV2",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 14,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 3}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_AVShE_NOSE",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 3.8,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 6}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_BNV1E",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 14.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 2}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_AVUE_NOSE",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4.5,
            "values": [
                {
                    "id": 4.5,
                    "dispName": "4.5"
                },
                {
                    "id": 11.5,
                    "dispName": "11.5"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "00_prfx_function_altitude_ctrl_BNV1E",
            "label": "Airburst Height",
            "control": "spinbox",
            "defValue": 10,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "m",
            "dimension": "m",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 2}],
        },
        {
            "id": "00_prfx_function_altitude_ctrl_BRV2",
            "label": "Airburst Height",
            "control": "spinbox",
            "defValue": 15,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "m",
            "dimension": "m",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 3}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_AMV",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 4}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_AVShE_NOSE",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 12,
            "values": [
                {
                    "id": 12,
                    "dispName": "12 s"
                },
                {
                    "id": 25,
                    "dispName": "25 s"
                },
                {
                    "id": 70,
                    "dispName": "70 s"
                },
                {
                    "id": 200,
                    "dispName": "3' 20\""
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 6}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_AV2E_NOSE",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 25,
            "values": [
                {
                    "id": 12,
                    "dispName": "12"
                },
                {
                    "id": 25,
                    "dispName": "25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 5}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_AVTE_NOSE",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0.04,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.04,
                    "dispName": "40 ms"
                },
                {
                    "id": 0.35,
                    "dispName": "0.35 s"
                },
                {
                    "id": 0.8,
                    "dispName": "0.8 s"
                },
                {
                    "id": 26,
                    "dispName": "26 s"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 7}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_AVUE_NOSE",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.025,
                    "dispName": "25 ms"
                },
                {
                    "id": 0.075,
                    "dispName": "75 ms"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": "EMPTY_TAIL",
            "values": [
                {
                    "id": 1,
                    "dispName": "AVU-E"
                },
                {
                    "id": 2,
                    "dispName": "AV-2E"
                },
                {
                    "id": 3,
                    "dispName": "AVShE"
                },
                {
                    "id": 4,
                    "dispName": "AVT-E"
                },
                {
                    "id": 5,
                    "dispName": "VDV"
                },
                {
                    "id": "EMPTY_TAIL",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_arm_delay_ctrl_VDV_TAIL",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 6.8,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 5}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_AV2E_TAIL",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 1.8,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 2}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_AVTE_TAIL",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 4.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 4}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_AVUE_TAIL",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4.5,
            "values": [
                {
                    "id": 4.5,
                    "dispName": "4.5"
                },
                {
                    "id": 11.5,
                    "dispName": "11.5"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_AVShE_TAIL",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 3.8,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 3}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_AVTE_TAIL",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0.04,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.04,
                    "dispName": "40 ms"
                },
                {
                    "id": 0.35,
                    "dispName": "0.35 s"
                },
                {
                    "id": 0.8,
                    "dispName": "0.8 s"
                },
                {
                    "id": 26,
                    "dispName": "26 s"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 4}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_AVShE_TAIL",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 12,
            "values": [
                {
                    "id": 12,
                    "dispName": "12 s"
                },
                {
                    "id": 25,
                    "dispName": "25 s"
                },
                {
                    "id": 70,
                    "dispName": "70 s"
                },
                {
                    "id": 200,
                    "dispName": "3' 20\""
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 3}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_AV2E_TAIL",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 25,
            "values": [
                {
                    "id": 12,
                    "dispName": "12"
                },
                {
                    "id": 25,
                    "dispName": "25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 2}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_VDV_TAIL",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.2,
                    "dispName": "0.2"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 5}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_AVUE_TAIL",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.025,
                    "dispName": "25 ms"
                },
                {
                    "id": 0.075,
                    "dispName": "75 ms"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        }
    ],
    # Used by 41 weapon(s): BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets, BRU_42___3_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets, DIS_MK_20, DIS_MK_20_DUAL_GDJ_II19_L, DIS_MK_20_DUAL_GDJ_II19_R
    # ... and 36 more
    "77ac9721": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": "Mk339Mod1",
            "values": [
                {
                    "id": "Mk339Mod1",
                    "dispName": "Mk 339 Mod 1"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "function_delay_ctrl_00_Mk339Mod1",
            "label": "Function Delay PRI",
            "control": "spinbox",
            "defValue": 1.2,
            "min": 1.2,
            "max": 100,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "Mk339Mod1"}],
        },
        {
            "id": "function_delay_ctrl_01_Mk339Mod1",
            "label": "Function Delay OPT",
            "control": "spinbox",
            "defValue": 4,
            "min": 1.2,
            "max": 100,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "Mk339Mod1"}],
        }
    ],
    # Used by 3 weapon(s): _250_lb_GP_Mk_V, _250_lb_GP_Mk_V_, _500_lb_GP_Mk_V
    "78930b4e": [
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Tail Pistol No. 17 Mk I"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_vane_rev_threshold_ctrl_TP17MkI",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 8,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_TP17MkI",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 1800,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "h",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        }
    ],
    # Used by 10 weapon(s): FAB_250M_62___250_kg_GP_Bomb_LD, FAB_250M_62___250_kg_GP_Bomb_LD_, FAB_500M_62___500_kg_GP_Bomb_LD, FAB_500M_62___500_kg_GP_Bomb_LD_, MBD3_U2T_1_with_2_x_FAB_250M_62___250_kg_GP_Bomb_LD
    # ... and 5 more
    "8045551b": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "AVU-E"
                },
                {
                    "id": 2,
                    "dispName": "AV-1 + MDV-5"
                },
                {
                    "id": 3,
                    "dispName": "AV-139E"
                },
                {
                    "id": 4,
                    "dispName": "AV-2E"
                },
                {
                    "id": 5,
                    "dispName": "AVShE"
                },
                {
                    "id": 6,
                    "dispName": "AVT-E"
                },
                {
                    "id": 7,
                    "dispName": "VDV"
                },
                {
                    "id": "EMPTY_NOSE",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "00_prfx_arm_delay_ctrl_AV2E_NOSE",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 1.8,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 4}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_AVShE_NOSE",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 3.8,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 5}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_AVTE_NOSE",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 4.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 6}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_AV139E_NOSE",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 20.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 3}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_VDV_NOSE",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 6.8,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 7}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_AV1_NOSE",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 1.9,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 2}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_AVUE_NOSE",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4.5,
            "values": [
                {
                    "id": 4.5,
                    "dispName": "4.5"
                },
                {
                    "id": 11.5,
                    "dispName": "11.5"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_AV1_NOSE",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 27,
            "values": [
                {
                    "id": 13.5,
                    "dispName": "13.5"
                },
                {
                    "id": 27,
                    "dispName": "27"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 2}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_AVUE_NOSE",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.025,
                    "dispName": "25 ms"
                },
                {
                    "id": 0.075,
                    "dispName": "75 ms"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_VDV_NOSE",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.2,
                    "dispName": "0.2"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 7}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_AVTE_NOSE",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0.04,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.04,
                    "dispName": "40 ms"
                },
                {
                    "id": 0.35,
                    "dispName": "0.35 s"
                },
                {
                    "id": 0.8,
                    "dispName": "0.8 s"
                },
                {
                    "id": 26,
                    "dispName": "26 s"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 6}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_AVShE_NOSE",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 12,
            "values": [
                {
                    "id": 12,
                    "dispName": "12 s"
                },
                {
                    "id": 25,
                    "dispName": "25 s"
                },
                {
                    "id": 70,
                    "dispName": "70 s"
                },
                {
                    "id": 200,
                    "dispName": "3' 20\""
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 5}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_AV139E_NOSE",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0.75,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.03,
                    "dispName": "30 ms"
                },
                {
                    "id": 0.75,
                    "dispName": "0.75 s"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 3}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_AV2E_NOSE",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 25,
            "values": [
                {
                    "id": 12,
                    "dispName": "12"
                },
                {
                    "id": 25,
                    "dispName": "25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 4}],
        },
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": "EMPTY_TAIL",
            "values": [
                {
                    "id": 1,
                    "dispName": "AVU-E"
                },
                {
                    "id": 2,
                    "dispName": "AV-1 + MDV-5"
                },
                {
                    "id": 3,
                    "dispName": "AV-139E"
                },
                {
                    "id": 4,
                    "dispName": "AV-2E"
                },
                {
                    "id": 5,
                    "dispName": "AVDM"
                },
                {
                    "id": 6,
                    "dispName": "AVShE"
                },
                {
                    "id": 7,
                    "dispName": "AVT-E"
                },
                {
                    "id": 8,
                    "dispName": "VDV"
                },
                {
                    "id": "EMPTY_TAIL",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_arm_delay_ctrl_VDV_TAIL",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 6.8,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 8}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_AVDM",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 5}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_AVShE_TAIL",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 3.8,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 6}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_AVTE_TAIL",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 4.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 7}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_AV139E_TAIL",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 20.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 3}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_AV2E_TAIL",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 1.8,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 4}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_AV1_TAIL",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 1.9,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 2}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_AVUE_TAIL",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4.5,
            "values": [
                {
                    "id": 4.5,
                    "dispName": "4.5"
                },
                {
                    "id": 11.5,
                    "dispName": "11.5"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_AV2E_TAIL",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 25,
            "values": [
                {
                    "id": 12,
                    "dispName": "12"
                },
                {
                    "id": 25,
                    "dispName": "25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 4}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_AVTE_TAIL",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0.04,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.04,
                    "dispName": "40 ms"
                },
                {
                    "id": 0.35,
                    "dispName": "0.35 s"
                },
                {
                    "id": 0.8,
                    "dispName": "0.8 s"
                },
                {
                    "id": 26,
                    "dispName": "26 s"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 7}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_AV1_TAIL",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 27,
            "values": [
                {
                    "id": 13.5,
                    "dispName": "13.5"
                },
                {
                    "id": 27,
                    "dispName": "27"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 2}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_AVShE_TAIL",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 12,
            "values": [
                {
                    "id": 12,
                    "dispName": "12 s"
                },
                {
                    "id": 25,
                    "dispName": "25 s"
                },
                {
                    "id": 70,
                    "dispName": "70 s"
                },
                {
                    "id": 200,
                    "dispName": "3' 20\""
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 6}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_AVDM",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 1800,
            "values": [
                {
                    "id": 1800,
                    "dispName": "0.5 h"
                },
                {
                    "id": 2880,
                    "dispName": "0.8 h"
                },
                {
                    "id": 3600,
                    "dispName": "1 h"
                },
                {
                    "id": 7200,
                    "dispName": "2 h"
                },
                {
                    "id": 10800,
                    "dispName": "3 h"
                },
                {
                    "id": 14400,
                    "dispName": "4 h"
                },
                {
                    "id": 18000,
                    "dispName": "5 h"
                },
                {
                    "id": 21600,
                    "dispName": "6 h"
                },
                {
                    "id": 28800,
                    "dispName": "8 h"
                },
                {
                    "id": 43200,
                    "dispName": "12 h"
                },
                {
                    "id": 64800,
                    "dispName": "18 h"
                },
                {
                    "id": 86400,
                    "dispName": "24 h"
                },
                {
                    "id": 129600,
                    "dispName": "1.5 d"
                },
                {
                    "id": 172800,
                    "dispName": "2 d"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 5}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_AV139E_TAIL",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0.75,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.03,
                    "dispName": "30 ms"
                },
                {
                    "id": 0.75,
                    "dispName": "0.75 s"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 3}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_VDV_TAIL",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.2,
                    "dispName": "0.2"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 8}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_AVUE_TAIL",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.025,
                    "dispName": "25 ms"
                },
                {
                    "id": 0.075,
                    "dispName": "75 ms"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        }
    ],
    # Used by 18 weapon(s): BRU_57_with_2_x_CBU_103___202_x_CEM__CBU_with_WCMD, CBU87_10, CBU_103___202_x_CEM__CBU_with_WCMD, CBU_87___202_x_CEM_Cluster_Bomb, HSAB___8_x_CBU_103___202_x_CEM__CBU_with_WCMD
    # ... and 13 more
    "8fc57508": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": "FZU39",
            "values": [
                {
                    "id": "FZU39",
                    "dispName": "Integral Fuze + FZU-39"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "function_delay_ctrl_FZU39_SUU65",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 2.23,
            "values": [
                {
                    "id": 0.63,
                    "dispName": "0.63"
                },
                {
                    "id": 0.95,
                    "dispName": "0.95"
                },
                {
                    "id": 1.28,
                    "dispName": "1.28"
                },
                {
                    "id": 1.6,
                    "dispName": "1.6"
                },
                {
                    "id": 1.92,
                    "dispName": "1.92"
                },
                {
                    "id": 2.23,
                    "dispName": "2.23"
                },
                {
                    "id": 2.55,
                    "dispName": "2.55"
                },
                {
                    "id": 2.87,
                    "dispName": "2.87"
                },
                {
                    "id": 3.19,
                    "dispName": "3.19"
                },
                {
                    "id": 3.51,
                    "dispName": "3.51"
                },
                {
                    "id": 3.83,
                    "dispName": "3.83"
                },
                {
                    "id": 4.15,
                    "dispName": "4.15"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "FZU39"}],
        },
        {
            "id": "function_altitude_ctrl_FZU39_SUU65",
            "label": "Airburst Height",
            "control": "comboList",
            "defValue": 1500,
            "values": [
                {
                    "id": 300,
                    "dispName": "300"
                },
                {
                    "id": 500,
                    "dispName": "500"
                },
                {
                    "id": 700,
                    "dispName": "700"
                },
                {
                    "id": 900,
                    "dispName": "900"
                },
                {
                    "id": 1200,
                    "dispName": "1200"
                },
                {
                    "id": 1500,
                    "dispName": "1500"
                },
                {
                    "id": 1800,
                    "dispName": "1800"
                },
                {
                    "id": 2200,
                    "dispName": "2200"
                },
                {
                    "id": 2600,
                    "dispName": "2600"
                },
                {
                    "id": 3000,
                    "dispName": "3000"
                }
            ],
            "baseDim": "ft",
            "dimension": "ft",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "FZU39"}],
        },
        {
            "id": "ang_vel_x",
            "label": "Spin Rate",
            "control": "spinbox",
            "defValue": 1000,
            "min": 0,
            "max": 2500,
            "baseDim": "RPM",
            "dimension": "RPM",
        }
    ],
    # Used by 6 weapon(s): AGM_45A_Shrike_ARM, AGM_45A_Shrike_ARM__LAU_34_, AGM_45B_Shrike_ARM, LAU_118A___AGM_45A_Shrike_ARM, LAU_118A___AGM_45B_Shrike_ARM
    # ... and 1 more
    "905ae409": [
        {
            "id": "NFP_rfgu_type",
            "label": "RF Guidance Unit",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Mk 22 (band G) - SNR-75 (Fan Song)"
                },
                {
                    "id": 2,
                    "dispName": "Mk 23 (complete E-F bands) - SON-9 (Fire Can), ST-68U (Tin Shield)"
                },
                {
                    "id": 3,
                    "dispName": "Mk 24 Mod 5 (narrow E-F bands) - SON-9 (Fire Can), ST-68U (Tin Shield)"
                },
                {
                    "id": 4,
                    "dispName": "Mk 24 Mod 34 (broad E-F bands) - SON-9 (Fire Can), ST-68U (Tin Shield)"
                },
                {
                    "id": 5,
                    "dispName": "Mk 25 (band G) - SNR-75 (Fan Song)"
                },
                {
                    "id": 6,
                    "dispName": "Mk 36 (band I) - SNR-125 (Low Blow)"
                },
                {
                    "id": 7,
                    "dispName": "Mk 37 (band C) - P-15 (Flat Face)"
                },
                {
                    "id": 8,
                    "dispName": "Mk 49 Mod 0 (bands H-I) - SNR-125 (Low Blow), 1S91 (Straight Flush)"
                },
                {
                    "id": 9,
                    "dispName": "Mk 49 Mod 1 (bands H-I), G-bias - SNR-125 (Low Blow), 1S91 (Straight Flush)"
                },
                {
                    "id": 10,
                    "dispName": "Mk 50 (bands E-H) - Various Radar Installations"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "EAS_bypass_ctrl",
            "label": "Attack Profile",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 0,
                    "dispName": "Loft Attack"
                },
                {
                    "id": 1,
                    "dispName": "Direct Attack"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "rf_lower_limit_ctrl_Mk37",
            "label": "Lower RF Limit",
            "control": "spinbox",
            "defValue": 800000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "MHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 7}],
        },
        {
            "id": "rf_lower_limit_ctrl_Mk25",
            "label": "Lower RF Limit",
            "control": "spinbox",
            "defValue": 4000000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 5}],
        },
        {
            "id": "rf_lower_limit_ctrl_Mk49Mod0",
            "label": "Lower RF Limit",
            "control": "spinbox",
            "defValue": 6000000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 8}],
        },
        {
            "id": "rf_lower_limit_ctrl_Mk50",
            "label": "Lower RF Limit",
            "control": "spinbox",
            "defValue": 2000000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 10}],
        },
        {
            "id": "rf_lower_limit_ctrl_Mk49Mod1",
            "label": "Lower RF Limit",
            "control": "spinbox",
            "defValue": 6000000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 9}],
        },
        {
            "id": "rf_lower_limit_ctrl_Mk24Mod34",
            "label": "Lower RF Limit",
            "control": "spinbox",
            "defValue": 2500000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 4}],
        },
        {
            "id": "rf_lower_limit_ctrl_Mk36",
            "label": "Lower RF Limit",
            "control": "spinbox",
            "defValue": 7900000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 6}],
        },
        {
            "id": "rf_lower_limit_ctrl_Mk23",
            "label": "Lower RF Limit",
            "control": "spinbox",
            "defValue": 2000000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 2}],
        },
        {
            "id": "rf_lower_limit_ctrl_Mk24Mod5",
            "label": "Lower RF Limit",
            "control": "spinbox",
            "defValue": 2650000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 3}],
        },
        {
            "id": "rf_lower_limit_ctrl_Mk22Mod2",
            "label": "Lower RF Limit",
            "control": "spinbox",
            "defValue": 4800000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 1}],
        },
        {
            "id": "rf_upper_limit_ctrl_Mk22Mod2",
            "label": "Upper RF Limit",
            "control": "spinbox",
            "defValue": 5200000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 1}],
        },
        {
            "id": "rf_upper_limit_ctrl_Mk50",
            "label": "Upper RF Limit",
            "control": "spinbox",
            "defValue": 6000000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 10}],
        },
        {
            "id": "rf_upper_limit_ctrl_Mk49Mod1",
            "label": "Upper RF Limit",
            "control": "spinbox",
            "defValue": 10000000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 9}],
        },
        {
            "id": "rf_upper_limit_ctrl_Mk49Mod0",
            "label": "Upper RF Limit",
            "control": "spinbox",
            "defValue": 10000000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 8}],
        },
        {
            "id": "rf_upper_limit_ctrl_Mk24Mod5",
            "label": "Upper RF Limit",
            "control": "spinbox",
            "defValue": 3150000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 3}],
        },
        {
            "id": "rf_upper_limit_ctrl_Mk37",
            "label": "Upper RF Limit",
            "control": "spinbox",
            "defValue": 1000000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 7}],
        },
        {
            "id": "rf_upper_limit_ctrl_Mk25",
            "label": "Upper RF Limit",
            "control": "spinbox",
            "defValue": 6000000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 5}],
        },
        {
            "id": "rf_upper_limit_ctrl_Mk24Mod34",
            "label": "Upper RF Limit",
            "control": "spinbox",
            "defValue": 3500000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 4}],
        },
        {
            "id": "rf_upper_limit_ctrl_Mk36",
            "label": "Upper RF Limit",
            "control": "spinbox",
            "defValue": 9600000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 6}],
        },
        {
            "id": "rf_upper_limit_ctrl_Mk23",
            "label": "Upper RF Limit",
            "control": "spinbox",
            "defValue": 4000000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 2}],
        },
        {
            "id": "smoke_marker",
            "label": "WP Marker Charge",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "Not Installed"
                },
                {
                    "id": 1,
                    "dispName": "Installed"
                }
            ],
            "baseDim": "",
        }
    ],
    # Used by 2 weapon(s): SD_250_Stg___250kg_GP_Bomb_LD, SD_500_A___500kg_GP_Bomb_LD
    "97f24521": [
        {
            "id": "NFP_fuze_type",
            "label": "Fuze Type",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Zünder 38"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "NFP_fuze_operation_mode",
            "label": "Function Delay Mode",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Variable"
                },
                {
                    "id": 2,
                    "dispName": "Fixed"
                }
            ],
            "baseDim": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_oV_VFD_Z38",
            "label": "oV Mode Function Delay",
            "control": "spinbox",
            "defValue": 0.05,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "ms",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 1}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_oV_FFD_Z38",
            "label": "oV Mode Function Delay",
            "control": "spinbox",
            "defValue": 5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 2}],
        },
        {
            "id": "02_prfx_function_delay_ctrl_mV_FFD_Z38",
            "label": "mV Mode Function Delay",
            "control": "spinbox",
            "defValue": 5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 2}],
        },
        {
            "id": "02_prfx_function_delay_ctrl_mV_VFD_Z38",
            "label": "mV Mode Function Delay",
            "control": "spinbox",
            "defValue": 0.2,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "ms",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 1}],
        },
        {
            "id": "03_prfx_function_delay_ctrl_Vz_FFD_Z38",
            "label": "Vz Mode Function Delay",
            "control": "spinbox",
            "defValue": 5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 2}],
        },
        {
            "id": "03_prfx_function_delay_ctrl_Vz_VFD_Z38",
            "label": "Vz Mode Function Delay",
            "control": "spinbox",
            "defValue": 5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 1}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_Strz_VFD_Z38",
            "label": "Sturz Mode Arm Delay",
            "control": "spinbox",
            "defValue": 3,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 1}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_Strz_FFD_Z38",
            "label": "Sturz Mode Arm Delay",
            "control": "spinbox",
            "defValue": 1,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 2}],
        },
        {
            "id": "02_prfx_arm_delay_ctrl_Wgrcht_FFD_Z38",
            "label": "Wagerecht Mode Arm Delay",
            "control": "spinbox",
            "defValue": 2,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 2}],
        },
        {
            "id": "02_prfx_arm_delay_ctrl_Wgrcht_VFD_Z38",
            "label": "Wagerecht Mode Arm Delay",
            "control": "spinbox",
            "defValue": 7.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}, "and", {"id": "NFP_fuze_operation_mode", "bNot": False, "value": 1}],
        }
    ],
    # Used by 45 weapon(s): BDU_45, BDU_45B, BDU_45B___500lb_Practice_Bomb, BDU_50LD___500lb_Inert_Practice_Bomb_LD, BRU_33_with_2_x_BDU_45B___500lb_Practice_Bomb
    # ... and 40 more
    "9bd8acc1": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": "M904E4",
            "values": [
                {
                    "id": "M904E4",
                    "dispName": "M904E4"
                },
                {
                    "id": "DSU33",
                    "dispName": "DSU-33"
                },
                {
                    "id": "EMPTY_NOSE",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "NFP_VIS_DrawArgNo_56",
            "label": "Plug",
            "control": "comboList",
            "defValue": 0.5,
            "values": [
                {
                    "id": 0.1,
                    "dispName": "Long Conical"
                },
                {
                    "id": 0.4,
                    "dispName": "Short Conical"
                },
                {
                    "id": 0.5,
                    "dispName": "MXU-735"
                }
            ],
            "baseDim": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "bNot": True, "value": "DSU33"}, "and", {"id": "NFP_fuze_type_nose", "bNot": True, "value": "M904E4"}],
        },
        {
            "id": "NFP_00_prfx_function_altitude_ctrl_DSU33",
            "label": "Airburst Height",
            "control": "spinbox",
            "defValue": 6.096,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "ft",
            "dimension": "ft",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "DSU33"}],
        },
        {
            "id": "NFP_00_prfx_arm_delay_ctrl_M904E4",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 4,
            "min": 2,
            "max": 18,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "M904E4"}],
        },
        {
            "id": "NFP_00_prfx_function_delay_ctrl_M904E4",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.05,
                    "dispName": "0.05"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.25,
                    "dispName": "0.25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "M904E4"}],
        },
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": "M905",
            "values": [
                {
                    "id": "M905",
                    "dispName": "M905"
                },
                {
                    "id": "FMU139CB_LD",
                    "dispName": "FMU-139"
                },
                {
                    "id": "FMU152AB_LD",
                    "dispName": "FMU-152"
                },
                {
                    "id": "EMPTY_TAIL",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "NFP_01_prfx_arm_delay_ctrl_FMU152AB_LD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 5,
                    "dispName": "5"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 7,
                    "dispName": "7"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 14,
                    "dispName": "14"
                },
                {
                    "id": 21,
                    "dispName": "21"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        },
        {
            "id": "NFP_01_prfx_arm_delay_ctrl_FMU139CB_LD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 7,
                    "dispName": "7"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 14,
                    "dispName": "14"
                },
                {
                    "id": 20,
                    "dispName": "20"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_LD"}],
        },
        {
            "id": "NFP_01_prfx_arm_delay_ctrl_M905",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 12,
                    "dispName": "12"
                },
                {
                    "id": 16,
                    "dispName": "16"
                },
                {
                    "id": 20,
                    "dispName": "20"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "M905"}],
        },
        {
            "id": "NFP_01_prfx_function_delay_ctrl_M905",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.05,
                    "dispName": "0.05"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.25,
                    "dispName": "0.25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "M905"}],
        },
        {
            "id": "NFP_01_prfx_function_delay_ctrl_FMU139CB_LD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.06,
                    "dispName": "0.06"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_LD"}],
        },
        {
            "id": "NFP_01_prfx_function_delay_ctrl_FMU152AB_LD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.005,
                    "dispName": "5 ms"
                },
                {
                    "id": 0.025,
                    "dispName": "25 ms"
                },
                {
                    "id": 0.06,
                    "dispName": "60 ms"
                },
                {
                    "id": 0.18,
                    "dispName": "180 ms"
                },
                {
                    "id": 900,
                    "dispName": "15 min"
                },
                {
                    "id": 14400,
                    "dispName": "4 h"
                },
                {
                    "id": 86400,
                    "dispName": "24 h"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        }
    ],
    # Used by 5 weapon(s): RP_3_60lb_SAP_No2_Mk_I, _2_x_RP_3_60lb_SAP_No2_Mk_I, _2_x_RP_3_60lb_SAP_No2_Mk_I_, _4_x_RP_3_60lb_SAP_No2_Mk_I, _4_x_RP_3_60lb_SAP_No2_Mk_I_
    "9f7e7070": [
        {
            "id": "NFP_fuze_type",
            "label": "Fuze Type",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Base Fuze No. 878 Mk I"
                },
                {
                    "id": 2,
                    "dispName": "Base Fuze No. 865 Mk I"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "arm_delay_ctrl_BFNo878MkI",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 0.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        },
        {
            "id": "arm_delay_ctrl_BFNo865MkI",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 0.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 2}],
        },
        {
            "id": "function_delay_ctrl_BFNo878MkI",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        },
        {
            "id": "function_delay_ctrl_BFNo865MkI",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 0.005,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "ms",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 2}],
        }
    ],
    # Used by 1 weapon(s): AGM_78A_Standard_ARM
    "aac2b92d": [
        {
            "id": "NFP_rfgu_type",
            "label": "RF Guidance Unit",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Mk 24 Mod 5 (narrow E-F bands) - SON-9 (Fire Can), ST-68U (Tin Shield)"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "rf_lower_limit_ctrl_Mk24Mod5",
            "label": "Lower RF Limit",
            "control": "spinbox",
            "defValue": 2650000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 1}],
        },
        {
            "id": "rf_upper_limit_ctrl_Mk24Mod5",
            "label": "Upper RF Limit",
            "control": "spinbox",
            "defValue": 3150000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 1}],
        }
    ],
    # Used by 3 weapon(s): _250_lb_S_A_P_, _250_lb_S_A_P__, _500_lb_S_A_P_
    "b4bf57e5": [
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Tail Pistol No. 30 Mk III"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_vane_rev_threshold_ctrl_TP30MkIII",
            "label": "Arming Vane Revs. Required",
            "control": "spinbox",
            "defValue": 13,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "rev",
            "dimension": "rev",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_TP30MkIII",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.12,
                    "dispName": "0.12"
                },
                {
                    "id": 1,
                    "dispName": "1"
                },
                {
                    "id": 11,
                    "dispName": "11"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        }
    ],
    # Used by 4 weapon(s): BRU_55_with_2_x_GBU_38___JDAM__500lb_GPS_Guided_Bomb, BRU_57_with_2_x_GBU_38___JDAM__500lb_GPS_Guided_Bomb, GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb, GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb_
    "b7b6ef11": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": "EMPTY_NOSE",
            "values": [
                {
                    "id": "DSU33",
                    "dispName": "DSU-33"
                },
                {
                    "id": "EMPTY_NOSE",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "NFP_VIS_DrawArgNo_56",
            "label": "Plug",
            "control": "comboList",
            "defValue": 0.5,
            "values": [
                {
                    "id": 0.1,
                    "dispName": "Long Conical"
                },
                {
                    "id": 0.4,
                    "dispName": "Short Conical"
                },
                {
                    "id": 0.5,
                    "dispName": "MXU-735"
                }
            ],
            "baseDim": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "bNot": True, "value": "DSU33"}, "and", {"id": "NFP_fuze_type_nose", "bNot": True, "value": "M904E4"}],
        },
        {
            "id": "00_prfx_function_altitude_ctrl_DSU33",
            "label": "Airburst Height",
            "control": "spinbox",
            "defValue": 6.096,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "ft",
            "dimension": "ft",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "DSU33"}],
        },
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": "FMU139CB_LD",
            "values": [
                {
                    "id": "FMU139CB_LD",
                    "dispName": "FMU-139"
                },
                {
                    "id": "FMU152AB_LD",
                    "dispName": "FMU-152"
                },
                {
                    "id": "EMPTY_TAIL",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU139CB_LD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 7,
                    "dispName": "7"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 14,
                    "dispName": "14"
                },
                {
                    "id": 20,
                    "dispName": "20"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_LD"}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU152AB_LD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 5,
                    "dispName": "5"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 7,
                    "dispName": "7"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 14,
                    "dispName": "14"
                },
                {
                    "id": 21,
                    "dispName": "21"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU139CB_LD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.06,
                    "dispName": "0.06"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_LD"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU152AB_LD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.005,
                    "dispName": "5 ms"
                },
                {
                    "id": 0.025,
                    "dispName": "25 ms"
                },
                {
                    "id": 0.06,
                    "dispName": "60 ms"
                },
                {
                    "id": 0.18,
                    "dispName": "180 ms"
                },
                {
                    "id": 900,
                    "dispName": "15 min"
                },
                {
                    "id": 14400,
                    "dispName": "4 h"
                },
                {
                    "id": 86400,
                    "dispName": "24 h"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        },
        {
            "id": "NFP_VIS_DrawArgNo_57",
            "label": "Appearance",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "USAF"
                },
                {
                    "id": 1,
                    "dispName": "USN"
                }
            ],
            "baseDim": "",
        }
    ],
    # Used by 18 weapon(s): BDU_45_LG___500lb_Practice_Laser_Guided_Bomb, BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD, BRU_33_with_2_x_BDU_45_LG_500lb_Practice_Laser_Guided_Bomb, BRU_42_2_x_LAU_131___7_x_Laser_Guided_Rkts__70_mm_Hydra_70_M151_HE_APKWS, BRU_42_2_x_LAU_131___7_x_Laser_Guided_Rkts__70_mm_Hydra_70_M151_HE_APKWS_
    # ... and 13 more
    "bb285623": [
        {
            "id": "laser_code",
            "label": "Laser Designator PRF Code",
            "control": "laserCode",
            "defValue": 1688,
        }
    ],
    # Used by 13 weapon(s): BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets, CBU_99, CBU_99___490lbs__247_x_HEAT_Bomblets, MAK79_2_CBU_99, MAK79_2_CBU_99_
    # ... and 8 more
    "be63446e": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": "Mk339Mod1",
            "values": [
                {
                    "id": "Mk339Mod1",
                    "dispName": "Mk 339 Mod 1"
                },
                {
                    "id": "FMU140",
                    "dispName": "FMU-140"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "function_delay_ctrl_00_Mk339Mod1",
            "label": "Function Delay PRI",
            "control": "spinbox",
            "defValue": 1.2,
            "min": 1.2,
            "max": 100,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "Mk339Mod1"}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_FMU140",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 1.2,
            "values": [
                {
                    "id": 1.2,
                    "dispName": "1.2"
                },
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 10,
                    "dispName": "10"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "FMU140"}],
        },
        {
            "id": "00_prfx_function_altitude_ctrl_FMU140",
            "label": "Airburst Height",
            "control": "comboList",
            "defValue": 1500,
            "values": [
                {
                    "id": 300,
                    "dispName": "300"
                },
                {
                    "id": 500,
                    "dispName": "500"
                },
                {
                    "id": 700,
                    "dispName": "700"
                },
                {
                    "id": 900,
                    "dispName": "900"
                },
                {
                    "id": 1200,
                    "dispName": "1200"
                },
                {
                    "id": 1500,
                    "dispName": "1500"
                },
                {
                    "id": 1800,
                    "dispName": "1800"
                },
                {
                    "id": 2200,
                    "dispName": "2200"
                },
                {
                    "id": 2600,
                    "dispName": "2600"
                },
                {
                    "id": 3000,
                    "dispName": "3000"
                }
            ],
            "baseDim": "ft",
            "dimension": "ft",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "FMU140"}],
        },
        {
            "id": "function_delay_ctrl_01_Mk339Mod1",
            "label": "Function Delay OPT",
            "control": "spinbox",
            "defValue": 4,
            "min": 1.2,
            "max": 100,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "Mk339Mod1"}],
        }
    ],
    # Used by 52 weapon(s): AUF_2___2_x_GBU_12___500lb_Laser_Guided_Bomb, BOLT_117___750_lb_Laser_Guided_Bomb, BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb, BRU_33_with_2_x_GBU_16___1000lb_Laser_Guided_Bomb, BRU_42_3_GBU_12
    # ... and 47 more
    "c0be62e6": [
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": "FMU139CB_LD",
            "values": [
                {
                    "id": "FMU139CB_LD",
                    "dispName": "FMU-139"
                },
                {
                    "id": "FMU152AB_LD",
                    "dispName": "FMU-152"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU152AB_LD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 5,
                    "dispName": "5"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 7,
                    "dispName": "7"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 14,
                    "dispName": "14"
                },
                {
                    "id": 21,
                    "dispName": "21"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU139CB_LD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 7,
                    "dispName": "7"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 14,
                    "dispName": "14"
                },
                {
                    "id": 20,
                    "dispName": "20"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_LD"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU152AB_LD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.005,
                    "dispName": "5 ms"
                },
                {
                    "id": 0.025,
                    "dispName": "25 ms"
                },
                {
                    "id": 0.06,
                    "dispName": "60 ms"
                },
                {
                    "id": 0.18,
                    "dispName": "180 ms"
                },
                {
                    "id": 900,
                    "dispName": "15 min"
                },
                {
                    "id": 14400,
                    "dispName": "4 h"
                },
                {
                    "id": 86400,
                    "dispName": "24 h"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU139CB_LD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.06,
                    "dispName": "0.06"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_LD"}],
        },
        {
            "id": "laser_code",
            "label": "Laser Designator PRF Code",
            "control": "laserCode",
            "defValue": 1688,
        },
        {
            "id": "NFP_VIS_DrawArgNo_57",
            "label": "Appearance",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "USAF"
                },
                {
                    "id": 1,
                    "dispName": "USN"
                }
            ],
            "baseDim": "",
        }
    ],
    # Used by 99 weapon(s): AUF_2___2_x_Mk_82___500lb_GP_Bomb_LD, BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD, BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD, BRU_41A___6_x_Mk_82___500lb_GP_Bomb_LD, BRU_42_with_3_x_Mk_81___250lb_GP_Bombs_LD
    # ... and 94 more
    "c382a5a8": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": "M904E4",
            "values": [
                {
                    "id": "M904E4",
                    "dispName": "M904E4"
                },
                {
                    "id": "DSU33",
                    "dispName": "DSU-33"
                },
                {
                    "id": "EMPTY_NOSE",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "NFP_VIS_DrawArgNo_56",
            "label": "Plug",
            "control": "comboList",
            "defValue": 0.5,
            "values": [
                {
                    "id": 0.1,
                    "dispName": "Long Conical"
                },
                {
                    "id": 0.4,
                    "dispName": "Short Conical"
                },
                {
                    "id": 0.5,
                    "dispName": "MXU-735"
                }
            ],
            "baseDim": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "bNot": True, "value": "DSU33"}, "and", {"id": "NFP_fuze_type_nose", "bNot": True, "value": "M904E4"}],
        },
        {
            "id": "00_prfx_function_altitude_ctrl_DSU33",
            "label": "Airburst Height",
            "control": "spinbox",
            "defValue": 6.096,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "ft",
            "dimension": "ft",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "DSU33"}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_M904E4",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 4,
            "min": 2,
            "max": 18,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "M904E4"}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_M904E4",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.05,
                    "dispName": "0.05"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.25,
                    "dispName": "0.25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "M904E4"}],
        },
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": "M905",
            "values": [
                {
                    "id": "M905",
                    "dispName": "M905"
                },
                {
                    "id": "FMU139CB_LD",
                    "dispName": "FMU-139"
                },
                {
                    "id": "FMU152AB_LD",
                    "dispName": "FMU-152"
                },
                {
                    "id": "EMPTY_TAIL",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_arm_delay_ctrl_M905",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 12,
                    "dispName": "12"
                },
                {
                    "id": 16,
                    "dispName": "16"
                },
                {
                    "id": 20,
                    "dispName": "20"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "M905"}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU139CB_LD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 7,
                    "dispName": "7"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 14,
                    "dispName": "14"
                },
                {
                    "id": 20,
                    "dispName": "20"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_LD"}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU152AB_LD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 5,
                    "dispName": "5"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 7,
                    "dispName": "7"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 14,
                    "dispName": "14"
                },
                {
                    "id": 21,
                    "dispName": "21"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_M905",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.05,
                    "dispName": "0.05"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.25,
                    "dispName": "0.25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "M905"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU152AB_LD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.005,
                    "dispName": "5 ms"
                },
                {
                    "id": 0.025,
                    "dispName": "25 ms"
                },
                {
                    "id": 0.06,
                    "dispName": "60 ms"
                },
                {
                    "id": 0.18,
                    "dispName": "180 ms"
                },
                {
                    "id": 900,
                    "dispName": "15 min"
                },
                {
                    "id": 14400,
                    "dispName": "4 h"
                },
                {
                    "id": 86400,
                    "dispName": "24 h"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU139CB_LD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.06,
                    "dispName": "0.06"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_LD"}],
        },
        {
            "id": "NFP_VIS_DrawArgNo_57",
            "label": "Appearance",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "USAF"
                },
                {
                    "id": 1,
                    "dispName": "USN"
                }
            ],
            "baseDim": "",
        }
    ],
    # Used by 1 weapon(s): AGM_78B_Standard_ARM
    "c817f096": [
        {
            "id": "NFP_rfgu_type",
            "label": "RF Guidance Unit",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Maxson Electronics Broadband Seeker"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "NFP_01_rf_lower_limit_ctrl",
            "label": "Lower RF Limit, band 1",
            "control": "spinbox",
            "defValue": 2650000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 1}],
        },
        {
            "id": "NFP_01_rf_upper_limit_ctrl",
            "label": "Upper RF Limit, band 1",
            "control": "spinbox",
            "defValue": 3200000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 1}],
        },
        {
            "id": "NFP_02_rf_lower_limit_ctrl",
            "label": "Lower RF Limit, band 2",
            "control": "spinbox",
            "defValue": 4800000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 1}],
        },
        {
            "id": "NFP_02_rf_upper_limit_ctrl",
            "label": "Upper RF Limit, band 2",
            "control": "spinbox",
            "defValue": 5300000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 1}],
        },
        {
            "id": "NFP_03_rf_lower_limit_ctrl",
            "label": "Lower RF Limit, band 3",
            "control": "spinbox",
            "defValue": 8800000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 1}],
        },
        {
            "id": "NFP_03_rf_upper_limit_ctrl",
            "label": "Upper RF Limit, band 3",
            "control": "spinbox",
            "defValue": 9600000000,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "Hz",
            "dimension": "GHz",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_rfgu_type", "value": 1}],
        }
    ],
    # Used by 1 weapon(s): AB_250_2___17_x_SD_10A__250kg_CBU_with_10kg_Frag_HE_submunitions
    "cde9cff7": [
        {
            "id": "NFP_fuze_type",
            "label": "Fuze Type",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Zünder 69D"
                },
                {
                    "id": 2,
                    "dispName": "Zünder 69E"
                },
                {
                    "id": 3,
                    "dispName": "Zünder 79"
                },
                {
                    "id": 4,
                    "dispName": "Zünder 79A"
                },
                {
                    "id": 5,
                    "dispName": "Zünder 89B"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_function_delay_ctrl_oV_Z69D",
            "label": "oV Mode Function Delay",
            "control": "spinbox",
            "defValue": 0.7,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_oV_Z69E",
            "label": "oV Mode Function Delay",
            "control": "spinbox",
            "defValue": 4,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 2}],
        },
        {
            "id": "arm_delay_ctrl_Z89B",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 5}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_oV_Z79A",
            "label": "oV Mode Function Delay",
            "control": "spinbox",
            "defValue": 3,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 4}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_oV_Z79",
            "label": "oV Mode Function Delay",
            "control": "spinbox",
            "defValue": 3,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 3}],
        },
        {
            "id": "02_prfx_function_delay_ctrl_mV_Z69E",
            "label": "mV Mode Function Delay",
            "control": "spinbox",
            "defValue": 5.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 2}],
        },
        {
            "id": "function_delay_ctrl_Z89B",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 4,
            "min": 3,
            "max": 60,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 5}],
        },
        {
            "id": "02_prfx_function_delay_ctrl_mV_Z79A",
            "label": "mV Mode Function Delay",
            "control": "spinbox",
            "defValue": 10,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 4}],
        },
        {
            "id": "02_prfx_function_delay_ctrl_mV_Z69D",
            "label": "mV Mode Function Delay",
            "control": "spinbox",
            "defValue": 1.2,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        },
        {
            "id": "02_prfx_function_delay_ctrl_mV_Z79",
            "label": "mV Mode Function Delay",
            "control": "spinbox",
            "defValue": 30,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 3}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_Strz_Z79",
            "label": "Sturz Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 3}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_Strz_Z79A",
            "label": "Sturz Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 4}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_Strz_Z69E",
            "label": "Sturz Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 2}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_Strz_Z69D",
            "label": "Sturz Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        },
        {
            "id": "02_prfx_arm_delay_ctrl_Wgrcht_Z69E",
            "label": "Wagerecht Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 2}],
        },
        {
            "id": "02_prfx_arm_delay_ctrl_Wgrcht_Z69D",
            "label": "Wagerecht Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        },
        {
            "id": "02_prfx_arm_delay_ctrl_Wgrcht_Z79",
            "label": "Wagerecht Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 3}],
        },
        {
            "id": "02_prfx_arm_delay_ctrl_Wgrcht_Z79A",
            "label": "Wagerecht Mode Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 4}],
        },
        {
            "id": "NFP_subm_fuze_type",
            "label": "Submunition Fuze Type",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Zünder 3"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "04_prfx_subm_arm_delay_ctrl_Z3",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 2.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_subm_fuze_type", "value": 1}],
        },
        {
            "id": "04_prfx_subm_func_delay_ctrl_Z3",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 6,
                    "dispName": "6"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_subm_fuze_type", "value": 1}],
        }
    ],
    # Used by 2 weapon(s): GBU_31_V_4_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb, GBU_31_V_4_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb_
    "d05924c1": [
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": "FMU143",
            "values": [
                {
                    "id": "FMU143",
                    "dispName": "FMU-143"
                },
                {
                    "id": "FMU152AB_LD",
                    "dispName": "FMU-152"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU143",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 5.5,
            "values": [
                {
                    "id": 5.5,
                    "dispName": "5.5"
                },
                {
                    "id": 12,
                    "dispName": "12"
                },
                {
                    "id": 21,
                    "dispName": "21"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU143"}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU152AB_LD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 5,
                    "dispName": "5"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 7,
                    "dispName": "7"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 14,
                    "dispName": "14"
                },
                {
                    "id": 21,
                    "dispName": "21"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU143",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0.03,
            "values": [
                {
                    "id": 0.03,
                    "dispName": "30 ms"
                },
                {
                    "id": 0.06,
                    "dispName": "60 ms"
                },
                {
                    "id": 0.12,
                    "dispName": "120 ms"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU143"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU152AB_LD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.005,
                    "dispName": "5 ms"
                },
                {
                    "id": 0.025,
                    "dispName": "25 ms"
                },
                {
                    "id": 0.06,
                    "dispName": "60 ms"
                },
                {
                    "id": 0.18,
                    "dispName": "180 ms"
                },
                {
                    "id": 900,
                    "dispName": "15 min"
                },
                {
                    "id": 14400,
                    "dispName": "4 h"
                },
                {
                    "id": 86400,
                    "dispName": "24 h"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        },
        {
            "id": "NFP_VIS_DrawArgNo_57",
            "label": "Appearance",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "USN"
                }
            ],
            "baseDim": "",
        }
    ],
    # Used by 13 weapon(s): M117___750lb_GP_Bomb_LD, MER3_with_3_x_M117___750lb_GP_Bombs_LD, MER6_with_6_x_M117___750lb_GP_Bombs_LD, _1x_M117___750lb_GP_Bomb_LD__TER_, _27_x_M117___750lb_GP_Bombs_LD
    # ... and 8 more
    "d360e0f2": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "M904E1"
                },
                {
                    "id": "M904E4",
                    "dispName": "M904E4"
                },
                {
                    "id": 3,
                    "dispName": "FMU-26B"
                },
                {
                    "id": "EMPTY_NOSE",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "00_prfx_arm_delay_ctrl_M904E1",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 12,
                    "dispName": "12"
                },
                {
                    "id": 16,
                    "dispName": "16"
                },
                {
                    "id": 20,
                    "dispName": "20"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_FMU26B_NOSE",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 4,
            "min": 2,
            "max": 20,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 3}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_M904E4",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 4,
            "min": 2,
            "max": 18,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "M904E4"}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_FMU26B_NOSE",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.02,
                    "dispName": "0.02"
                },
                {
                    "id": 0.05,
                    "dispName": "0.05"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.25,
                    "dispName": "0.25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 3}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_M904E4",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.05,
                    "dispName": "0.05"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.25,
                    "dispName": "0.25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "M904E4"}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_M904E1",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.05,
                    "dispName": "0.05"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.25,
                    "dispName": "0.25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": "M905",
            "values": [
                {
                    "id": "M905",
                    "dispName": "M905"
                },
                {
                    "id": 2,
                    "dispName": "FMU-26B"
                },
                {
                    "id": "EMPTY_TAIL",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU26B_TAIL",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 4,
            "min": 2,
            "max": 20,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 2}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_M905",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 12,
                    "dispName": "12"
                },
                {
                    "id": 16,
                    "dispName": "16"
                },
                {
                    "id": 20,
                    "dispName": "20"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "M905"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_M905",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.05,
                    "dispName": "0.05"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.25,
                    "dispName": "0.25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "M905"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU26B_TAIL",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.02,
                    "dispName": "0.02"
                },
                {
                    "id": 0.05,
                    "dispName": "0.05"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.25,
                    "dispName": "0.25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 2}],
        }
    ],
    # Used by 10 weapon(s): CBU_52B___220_x_HE_Frag_bomblets, _1x_CBU_52B___220_x_HE_Frag_bomblets__TER_, _2x_CBU_52B___220_x_HE_Frag_bomblets__TER_, _2x_CBU_52B___220_x_HE_Frag_bomblets__TER__, _3x_CBU_52B___220_x_HE_Frag_bomblets__MER_
    # ... and 5 more
    "db1f274e": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "M907"
                },
                {
                    "id": 2,
                    "dispName": "FMU-26A"
                },
                {
                    "id": 3,
                    "dispName": "FMU-56"
                },
                {
                    "id": 4,
                    "dispName": "FMU-56A"
                },
                {
                    "id": 5,
                    "dispName": "FMU-110"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "00_prfx_arm_delay_ctrl_FMU56A",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 3,
            "values": [
                {
                    "id": 3,
                    "dispName": "3"
                },
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 5,
                    "dispName": "5"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 7,
                    "dispName": "7"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 9,
                    "dispName": "9"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 18,
                    "dispName": "18"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 4}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_FMU26A",
            "label": "Airburst Delay",
            "control": "spinbox",
            "defValue": 2,
            "min": 2,
            "max": 100,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 2}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_FMU56",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 2,
            "values": [
                {
                    "id": 2,
                    "dispName": "2"
                },
                {
                    "id": 3,
                    "dispName": "3"
                },
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 12,
                    "dispName": "12"
                },
                {
                    "id": 14,
                    "dispName": "14"
                },
                {
                    "id": 18,
                    "dispName": "18"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 3}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_FMU110",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 3,
            "values": [
                {
                    "id": 3,
                    "dispName": "3"
                },
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 5,
                    "dispName": "5"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 7,
                    "dispName": "7"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 9,
                    "dispName": "9"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 18,
                    "dispName": "18"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 5}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_M907",
            "label": "Airburst Delay",
            "control": "spinbox",
            "defValue": 4,
            "min": 4,
            "max": 92,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "00_prfx_function_altitude_ctrl_FMU56",
            "label": "Airburst Height",
            "control": "comboList",
            "defValue": 1500,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 250,
                    "dispName": "250"
                },
                {
                    "id": 500,
                    "dispName": "500"
                },
                {
                    "id": 800,
                    "dispName": "800"
                },
                {
                    "id": 1100,
                    "dispName": "1100"
                },
                {
                    "id": 1500,
                    "dispName": "1500"
                },
                {
                    "id": 1800,
                    "dispName": "1800"
                },
                {
                    "id": 2100,
                    "dispName": "2100"
                },
                {
                    "id": 2500,
                    "dispName": "2500"
                },
                {
                    "id": 3000,
                    "dispName": "3000"
                }
            ],
            "baseDim": "ft",
            "dimension": "ft",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 3}],
        },
        {
            "id": "00_prfx_function_altitude_ctrl_FMU56A",
            "label": "Airburst Height",
            "control": "comboList",
            "defValue": 1500,
            "values": [
                {
                    "id": 250,
                    "dispName": "250"
                },
                {
                    "id": 500,
                    "dispName": "500"
                },
                {
                    "id": 800,
                    "dispName": "800"
                },
                {
                    "id": 1100,
                    "dispName": "1100"
                },
                {
                    "id": 1500,
                    "dispName": "1500"
                },
                {
                    "id": 1800,
                    "dispName": "1800"
                },
                {
                    "id": 2000,
                    "dispName": "2000"
                },
                {
                    "id": 2200,
                    "dispName": "2200"
                },
                {
                    "id": 2500,
                    "dispName": "2500"
                },
                {
                    "id": 3000,
                    "dispName": "3000"
                }
            ],
            "baseDim": "ft",
            "dimension": "ft",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 4}],
        },
        {
            "id": "00_prfx_function_altitude_ctrl_FMU110",
            "label": "Airburst Height",
            "control": "comboList",
            "defValue": 1500,
            "values": [
                {
                    "id": 300,
                    "dispName": "300"
                },
                {
                    "id": 500,
                    "dispName": "500"
                },
                {
                    "id": 700,
                    "dispName": "700"
                },
                {
                    "id": 900,
                    "dispName": "900"
                },
                {
                    "id": 1200,
                    "dispName": "1200"
                },
                {
                    "id": 1500,
                    "dispName": "1500"
                },
                {
                    "id": 1800,
                    "dispName": "1800"
                },
                {
                    "id": 2200,
                    "dispName": "2200"
                },
                {
                    "id": 2600,
                    "dispName": "2600"
                },
                {
                    "id": 3000,
                    "dispName": "3000"
                }
            ],
            "baseDim": "ft",
            "dimension": "ft",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 5}],
        }
    ],
    # Used by 17 weapon(s): BDU_45___500lb_Practice_Bomb, BDU_50HD___500lb_Inert_Practice_Bomb_HD, BRU_33_with_2_x_BDU_45___500lb_Practice_Bomb, Mk_84_AIR__BSU_50____2000_lb_TP_Chute_Retarded_Bomb_HD, TER_9_A___3_x_BDU_50HD___500lb_Inert_Practice_Bomb_HD
    # ... and 12 more
    "dda439e7": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": "M904E4",
            "values": [
                {
                    "id": "M904E4",
                    "dispName": "M904E4"
                },
                {
                    "id": "DSU33",
                    "dispName": "DSU-33"
                },
                {
                    "id": "EMPTY_NOSE",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "NFP_VIS_DrawArgNo_56",
            "label": "Plug",
            "control": "comboList",
            "defValue": 0.5,
            "values": [
                {
                    "id": 0.1,
                    "dispName": "Long Conical"
                },
                {
                    "id": 0.4,
                    "dispName": "Short Conical"
                },
                {
                    "id": 0.5,
                    "dispName": "MXU-735"
                }
            ],
            "baseDim": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "bNot": True, "value": "DSU33"}, "and", {"id": "NFP_fuze_type_nose", "bNot": True, "value": "M904E4"}],
        },
        {
            "id": "NFP_00_prfx_function_altitude_ctrl_DSU33",
            "label": "Airburst Height",
            "control": "spinbox",
            "defValue": 6.096,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "ft",
            "dimension": "ft",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "DSU33"}],
        },
        {
            "id": "NFP_00_prfx_arm_delay_ctrl_M904E4",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 4,
            "min": 2,
            "max": 18,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "M904E4"}],
        },
        {
            "id": "NFP_00_prfx_function_delay_ctrl_M904E4",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.05,
                    "dispName": "0.05"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.25,
                    "dispName": "0.25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "M904E4"}],
        },
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": "M905",
            "values": [
                {
                    "id": "M905",
                    "dispName": "M905"
                },
                {
                    "id": "FMU139CB_HD",
                    "dispName": "FMU-139"
                },
                {
                    "id": "FMU152AB_HD",
                    "dispName": "FMU-152"
                },
                {
                    "id": "EMPTY_TAIL",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "NFP_01_prfx_arm_delay_ctrl_FMU139CB_HD_FD_0.025",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 2.6,
            "values": [
                {
                    "id": 2.6,
                    "dispName": "2.6"
                },
                {
                    "id": 4,
                    "dispName": "4"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_HD"}, "and", {"id": "NFP_01_prfx_function_delay_ctrl_FMU139CB_HD", "value": 0.025}],
        },
        {
            "id": "NFP_01_prfx_arm_delay_ctrl_FMU139CB_HD_FD_0.01",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 2.6,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_HD"}, "and", {"id": "NFP_01_prfx_function_delay_ctrl_FMU139CB_HD", "value": 0.01}],
        },
        {
            "id": "NFP_01_prfx_arm_delay_ctrl_M905",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 12,
                    "dispName": "12"
                },
                {
                    "id": 16,
                    "dispName": "16"
                },
                {
                    "id": 20,
                    "dispName": "20"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "M905"}],
        },
        {
            "id": "NFP_01_prfx_arm_delay_ctrl_FMU152AB_HD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 2,
            "values": [
                {
                    "id": 2,
                    "dispName": "2"
                },
                {
                    "id": 2.6,
                    "dispName": "2.6"
                },
                {
                    "id": 3,
                    "dispName": "3"
                },
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 5,
                    "dispName": "5"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_HD"}],
        },
        {
            "id": "NFP_01_prfx_arm_delay_ctrl_FMU139CB_HD_FD_0.06",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 2.6,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_HD"}, "and", {"id": "NFP_01_prfx_function_delay_ctrl_FMU139CB_HD", "value": 0.06}],
        },
        {
            "id": "NFP_01_prfx_arm_delay_ctrl_FMU139CB_HD_FD_0",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 2,
            "values": [
                {
                    "id": 2,
                    "dispName": "2"
                },
                {
                    "id": 2.6,
                    "dispName": "2.6"
                },
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 5,
                    "dispName": "5"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_HD"}, "and", {"id": "NFP_01_prfx_function_delay_ctrl_FMU139CB_HD", "value": 0}],
        },
        {
            "id": "NFP_01_prfx_function_delay_ctrl_FMU152AB_HD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.005,
                    "dispName": "5 ms"
                },
                {
                    "id": 0.025,
                    "dispName": "25 ms"
                },
                {
                    "id": 0.06,
                    "dispName": "60 ms"
                },
                {
                    "id": 0.18,
                    "dispName": "180 ms"
                },
                {
                    "id": 900,
                    "dispName": "15 min"
                },
                {
                    "id": 14400,
                    "dispName": "4 h"
                },
                {
                    "id": 86400,
                    "dispName": "24 h"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_HD"}],
        },
        {
            "id": "NFP_01_prfx_function_delay_ctrl_M905",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.05,
                    "dispName": "0.05"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.25,
                    "dispName": "0.25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "M905"}],
        },
        {
            "id": "NFP_01_prfx_function_delay_ctrl_FMU139CB_HD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.06,
                    "dispName": "0.06"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_HD"}],
        }
    ],
    # Used by 1 weapon(s): Werfer_Granate_21___21_cm_UnGd_air_to_air_rocket
    "e359a771": [
        {
            "id": "NFP_fuze_type",
            "label": "Fuze Type",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Zt. Zünder S/30"
                },
                {
                    "id": 2,
                    "dispName": "Hbgr. Zünder 35 D"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "arm_delay_ctrl_ZTZS30",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        },
        {
            "id": "arm_delay_ctrl_HBGRZ35D",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 2}],
        },
        {
            "id": "self_destruct_delay_ctrl_ZTZS30",
            "label": "Airburst Delay",
            "control": "spinbox",
            "defValue": 5.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 1}],
        },
        {
            "id": "function_delay_ctrl_HBGRZ35D",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type", "value": 2}],
        }
    ],
    # Used by 4 weapon(s): BRU_55_with_2_x_GBU_32_V_2_B___JDAM__1000lb_GPS_Guided_Bomb, GBU_31_V_2_B___JDAM__2000lb_GPS_Guided_Bomb, GBU_31_V_2_B___JDAM__2000lb_GPS_Guided_Bomb_, GBU_32_V_2_B___JDAM__1000lb_GPS_Guided_Bomb
    "e3d793ed": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": "EMPTY_NOSE",
            "values": [
                {
                    "id": "DSU33",
                    "dispName": "DSU-33"
                },
                {
                    "id": "EMPTY_NOSE",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "NFP_VIS_DrawArgNo_56",
            "label": "Plug",
            "control": "comboList",
            "defValue": 0.5,
            "values": [
                {
                    "id": 0.1,
                    "dispName": "Long Conical"
                },
                {
                    "id": 0.4,
                    "dispName": "Short Conical"
                },
                {
                    "id": 0.5,
                    "dispName": "MXU-735"
                }
            ],
            "baseDim": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "bNot": True, "value": "DSU33"}, "and", {"id": "NFP_fuze_type_nose", "bNot": True, "value": "M904E4"}],
        },
        {
            "id": "00_prfx_function_altitude_ctrl_DSU33",
            "label": "Airburst Height",
            "control": "spinbox",
            "defValue": 6.096,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "ft",
            "dimension": "ft",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "DSU33"}],
        },
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": "FMU139CB_LD",
            "values": [
                {
                    "id": "FMU139CB_LD",
                    "dispName": "FMU-139"
                },
                {
                    "id": "FMU152AB_LD",
                    "dispName": "FMU-152"
                },
                {
                    "id": "EMPTY_TAIL",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU139CB_LD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 7,
                    "dispName": "7"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 14,
                    "dispName": "14"
                },
                {
                    "id": 20,
                    "dispName": "20"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_LD"}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU152AB_LD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 5,
                    "dispName": "5"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 7,
                    "dispName": "7"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 14,
                    "dispName": "14"
                },
                {
                    "id": 21,
                    "dispName": "21"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU139CB_LD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.06,
                    "dispName": "0.06"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_LD"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU152AB_LD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.005,
                    "dispName": "5 ms"
                },
                {
                    "id": 0.025,
                    "dispName": "25 ms"
                },
                {
                    "id": 0.06,
                    "dispName": "60 ms"
                },
                {
                    "id": 0.18,
                    "dispName": "180 ms"
                },
                {
                    "id": 900,
                    "dispName": "15 min"
                },
                {
                    "id": 14400,
                    "dispName": "4 h"
                },
                {
                    "id": 86400,
                    "dispName": "24 h"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        },
        {
            "id": "NFP_VIS_DrawArgNo_57",
            "label": "Appearance",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "USN"
                }
            ],
            "baseDim": "",
        }
    ],
    # Used by 3 weapon(s): BetAB_500___500_kg_Concrete_Piercing_Bomb_LD, BetAB_500___500_kg_Concrete_Piercing_Bomb_LD_, MBD3_U2T_1_with_2_x_BetAB_500___500_kg_Concrete_Piercing_Bomb_LD
    "e61b3f21": [
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "AVT-E"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_arm_delay_ctrl_AVTE_TAIL",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 4.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_AVTE_TAIL",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0.04,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.04,
                    "dispName": "40 ms"
                },
                {
                    "id": 0.35,
                    "dispName": "0.35 s"
                },
                {
                    "id": 0.8,
                    "dispName": "0.8 s"
                },
                {
                    "id": 26,
                    "dispName": "26 s"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        }
    ],
    # Used by 5 weapon(s): RP_3_60lb_F_No1_Mk_I, _2_x_RP_3_60lb_F_No1_Mk_I, _2_x_RP_3_60lb_F_No1_Mk_I_, _4_x_RP_3_60lb_F_No1_Mk_I, _4_x_RP_3_60lb_F_No1_Mk_I_
    "ea8e0f41": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "Nose Fuze No. 899 Mk I"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "00_prfx_arm_delay_ctrl_NFNo899MkI",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 0.7,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_NFNo899MkI",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        }
    ],
    # Used by 76 weapon(s): BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD, BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD, BRU_33_with_2_x_Mk_83_AIR__BSU_85____1000_lb_GP_Chute_Retarded_Bomb_HD, BRU_42___1_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD, BRU_42___2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD
    # ... and 71 more
    "f5afc219": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": "M904E4",
            "values": [
                {
                    "id": "M904E4",
                    "dispName": "M904E4"
                },
                {
                    "id": "DSU33",
                    "dispName": "DSU-33"
                },
                {
                    "id": "EMPTY_NOSE",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "NFP_VIS_DrawArgNo_56",
            "label": "Plug",
            "control": "comboList",
            "defValue": 0.5,
            "values": [
                {
                    "id": 0.1,
                    "dispName": "Long Conical"
                },
                {
                    "id": 0.4,
                    "dispName": "Short Conical"
                },
                {
                    "id": 0.5,
                    "dispName": "MXU-735"
                }
            ],
            "baseDim": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "bNot": True, "value": "DSU33"}, "and", {"id": "NFP_fuze_type_nose", "bNot": True, "value": "M904E4"}],
        },
        {
            "id": "00_prfx_function_altitude_ctrl_DSU33",
            "label": "Airburst Height",
            "control": "spinbox",
            "defValue": 6.096,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "ft",
            "dimension": "ft",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "DSU33"}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_M904E4",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 4,
            "min": 2,
            "max": 18,
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "M904E4"}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_M904E4",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.05,
                    "dispName": "0.05"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.25,
                    "dispName": "0.25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": "M904E4"}],
        },
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": "M905",
            "values": [
                {
                    "id": "M905",
                    "dispName": "M905"
                },
                {
                    "id": "FMU139CB_HD",
                    "dispName": "FMU-139"
                },
                {
                    "id": "FMU152AB_HD",
                    "dispName": "FMU-152"
                },
                {
                    "id": "EMPTY_TAIL",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU139CB_HD_FD_0.06",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 2.6,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_HD"}, "and", {"id": "01_prfx_function_delay_ctrl_FMU139CB_HD", "value": 0.06}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU139CB_HD_FD_0",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 2,
            "values": [
                {
                    "id": 2,
                    "dispName": "2"
                },
                {
                    "id": 2.6,
                    "dispName": "2.6"
                },
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 5,
                    "dispName": "5"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_HD"}, "and", {"id": "01_prfx_function_delay_ctrl_FMU139CB_HD", "value": 0}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU152AB_HD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 2,
            "values": [
                {
                    "id": 2,
                    "dispName": "2"
                },
                {
                    "id": 2.6,
                    "dispName": "2.6"
                },
                {
                    "id": 3,
                    "dispName": "3"
                },
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 5,
                    "dispName": "5"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_HD"}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU139CB_HD_FD_0.01",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 2.6,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_HD"}, "and", {"id": "01_prfx_function_delay_ctrl_FMU139CB_HD", "value": 0.01}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU139CB_HD_FD_0.025",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 2.6,
            "values": [
                {
                    "id": 2.6,
                    "dispName": "2.6"
                },
                {
                    "id": 4,
                    "dispName": "4"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_HD"}, "and", {"id": "01_prfx_function_delay_ctrl_FMU139CB_HD", "value": 0.025}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_M905",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 12,
                    "dispName": "12"
                },
                {
                    "id": 16,
                    "dispName": "16"
                },
                {
                    "id": 20,
                    "dispName": "20"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "M905"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU139CB_HD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.06,
                    "dispName": "0.06"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU139CB_HD"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_M905",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.01,
                    "dispName": "0.01"
                },
                {
                    "id": 0.025,
                    "dispName": "0.025"
                },
                {
                    "id": 0.05,
                    "dispName": "0.05"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.25,
                    "dispName": "0.25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "M905"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU152AB_HD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.005,
                    "dispName": "5 ms"
                },
                {
                    "id": 0.025,
                    "dispName": "25 ms"
                },
                {
                    "id": 0.06,
                    "dispName": "60 ms"
                },
                {
                    "id": 0.18,
                    "dispName": "180 ms"
                },
                {
                    "id": 900,
                    "dispName": "15 min"
                },
                {
                    "id": 14400,
                    "dispName": "4 h"
                },
                {
                    "id": 86400,
                    "dispName": "24 h"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_HD"}],
        },
        {
            "id": "NFP_VIS_DrawArgNo_57",
            "label": "Appearance",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "USAF"
                },
                {
                    "id": 1,
                    "dispName": "USN"
                }
            ],
            "baseDim": "",
        }
    ],
    # Used by 5 weapon(s): CSRL___8_x_GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb, GBU_31V3B_8, GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb, HSAB___6_x_GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb, HSAB___6_x_GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb_
    "f937ac43": [
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": "FMU143",
            "values": [
                {
                    "id": "FMU143",
                    "dispName": "FMU-143"
                },
                {
                    "id": "FMU152AB_LD",
                    "dispName": "FMU-152"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU143",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 5.5,
            "values": [
                {
                    "id": 5.5,
                    "dispName": "5.5"
                },
                {
                    "id": 12,
                    "dispName": "12"
                },
                {
                    "id": 21,
                    "dispName": "21"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU143"}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_FMU152AB_LD",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4,
            "values": [
                {
                    "id": 4,
                    "dispName": "4"
                },
                {
                    "id": 5,
                    "dispName": "5"
                },
                {
                    "id": 6,
                    "dispName": "6"
                },
                {
                    "id": 7,
                    "dispName": "7"
                },
                {
                    "id": 8,
                    "dispName": "8"
                },
                {
                    "id": 10,
                    "dispName": "10"
                },
                {
                    "id": 14,
                    "dispName": "14"
                },
                {
                    "id": 21,
                    "dispName": "21"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU143",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0.03,
            "values": [
                {
                    "id": 0.03,
                    "dispName": "30 ms"
                },
                {
                    "id": 0.06,
                    "dispName": "60 ms"
                },
                {
                    "id": 0.12,
                    "dispName": "120 ms"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU143"}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_FMU152AB_LD",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.005,
                    "dispName": "5 ms"
                },
                {
                    "id": 0.025,
                    "dispName": "25 ms"
                },
                {
                    "id": 0.06,
                    "dispName": "60 ms"
                },
                {
                    "id": 0.18,
                    "dispName": "180 ms"
                },
                {
                    "id": 900,
                    "dispName": "15 min"
                },
                {
                    "id": 14400,
                    "dispName": "4 h"
                },
                {
                    "id": 86400,
                    "dispName": "24 h"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": "FMU152AB_LD"}],
        }
    ],
    # Used by 34 weapon(s): AIM_9L_Sidewinder_IR_AAM, AIM_9M_Sidewinder_IR_AAM, AIM_9M_Sidewinder_IR_AAM_, AIM_9X_Sidewinder_IR_AAM, LAU_105_1_AIM_9L_L
    # ... and 29 more
    "fc240df9": [
        {
            "id": "NFP_VIS_DrawArgNo_57",
            "label": "Body Color",
            "control": "comboList",
            "defValue": 0.1,
            "values": [
                {
                    "id": 0,
                    "dispName": "White"
                },
                {
                    "id": 0.1,
                    "dispName": "Grey"
                }
            ],
            "baseDim": "",
        }
    ],
    # Used by 4 weapon(s): MBD2_67U___4_x_OFAB_100_120___100_kg_GP_Bomb_LD, MBD2_67U___4_x_OFAB_100_120___100_kg_GP_Bomb_LD_, MBD3_U6_68___6_x_OFAB_100_120___100_kg_GP_Bomb_LD, OFAB_100_120___100_kg_GP_Bomb_LD
    "fef1fc0c": [
        {
            "id": "NFP_fuze_type_nose",
            "label": "Nose Fuze Well",
            "control": "comboList",
            "defValue": 1,
            "values": [
                {
                    "id": 1,
                    "dispName": "AVU-E"
                },
                {
                    "id": 2,
                    "dispName": "BNV-1E"
                },
                {
                    "id": 3,
                    "dispName": "BRV-1"
                },
                {
                    "id": 4,
                    "dispName": "AMV"
                },
                {
                    "id": 5,
                    "dispName": "AV-2E"
                },
                {
                    "id": 6,
                    "dispName": "AVShE"
                },
                {
                    "id": 7,
                    "dispName": "AVT-E"
                },
                {
                    "id": 8,
                    "dispName": "VDV"
                },
                {
                    "id": "EMPTY_NOSE",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "00_prfx_arm_delay_ctrl_BRV1",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 14,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 3}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_AVShE_NOSE",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 3.8,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 6}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_AMV",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 1.9,
            "values": [
                {
                    "id": 1.9,
                    "dispName": "1.9"
                },
                {
                    "id": 11.5,
                    "dispName": "11.5"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 4}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_BNV1E",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 14.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 2}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_AVTE_NOSE",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 4.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 7}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_AV2E_NOSE",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 1.8,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 5}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_AVUE_NOSE",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4.5,
            "values": [
                {
                    "id": 4.5,
                    "dispName": "4.5"
                },
                {
                    "id": 11.5,
                    "dispName": "11.5"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "00_prfx_arm_delay_ctrl_VDV_NOSE",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 6.8,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 8}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_AVShE_NOSE",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 12,
            "values": [
                {
                    "id": 12,
                    "dispName": "12 s"
                },
                {
                    "id": 25,
                    "dispName": "25 s"
                },
                {
                    "id": 70,
                    "dispName": "70 s"
                },
                {
                    "id": 200,
                    "dispName": "3' 20\""
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 6}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_VDV_NOSE",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.2,
                    "dispName": "0.2"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 8}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_AVTE_NOSE",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0.04,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.04,
                    "dispName": "40 ms"
                },
                {
                    "id": 0.35,
                    "dispName": "0.35 s"
                },
                {
                    "id": 0.8,
                    "dispName": "0.8 s"
                },
                {
                    "id": 26,
                    "dispName": "26 s"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 7}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_AMV",
            "label": "Function Delay",
            "control": "spinbox",
            "defValue": 0,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 4}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_AV2E_NOSE",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 25,
            "values": [
                {
                    "id": 12,
                    "dispName": "12"
                },
                {
                    "id": 25,
                    "dispName": "25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 5}],
        },
        {
            "id": "00_prfx_function_altitude_ctrl_BNV1E",
            "label": "Airburst Height",
            "control": "spinbox",
            "defValue": 10,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "m",
            "dimension": "m",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 2}],
        },
        {
            "id": "00_prfx_function_delay_ctrl_AVUE_NOSE",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.025,
                    "dispName": "25 ms"
                },
                {
                    "id": 0.075,
                    "dispName": "75 ms"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 1}],
        },
        {
            "id": "00_prfx_function_altitude_ctrl_BRV1",
            "label": "Airburst Height",
            "control": "spinbox",
            "defValue": 15,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "m",
            "dimension": "m",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_nose", "value": 3}],
        },
        {
            "id": "NFP_fuze_type_tail",
            "label": "Tail Fuze Well",
            "control": "comboList",
            "defValue": "EMPTY_TAIL",
            "values": [
                {
                    "id": 1,
                    "dispName": "AVU-E"
                },
                {
                    "id": 2,
                    "dispName": "AV-2E"
                },
                {
                    "id": 3,
                    "dispName": "AVShE"
                },
                {
                    "id": 4,
                    "dispName": "AVT-E"
                },
                {
                    "id": 5,
                    "dispName": "VDV"
                },
                {
                    "id": "EMPTY_TAIL",
                    "dispName": "Plugged"
                }
            ],
            "baseDim": "",
        },
        {
            "id": "01_prfx_arm_delay_ctrl_AVTE_TAIL",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 4.5,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 4}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_AVShE_TAIL",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 3.8,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 3}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_AV2E_TAIL",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 1.8,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 2}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_AVUE_TAIL",
            "label": "Arm Delay",
            "control": "comboList",
            "defValue": 4.5,
            "values": [
                {
                    "id": 4.5,
                    "dispName": "4.5"
                },
                {
                    "id": 11.5,
                    "dispName": "11.5"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        },
        {
            "id": "01_prfx_arm_delay_ctrl_VDV_TAIL",
            "label": "Arm Delay",
            "control": "spinbox",
            "defValue": 6.8,
            "min": 0,
            "max": 1000000000000,
            "baseDim": "s",
            "dimension": "s",
            "readOnly": True,
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 5}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_VDV_TAIL",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0"
                },
                {
                    "id": 0.1,
                    "dispName": "0.1"
                },
                {
                    "id": 0.2,
                    "dispName": "0.2"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 5}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_AV2E_TAIL",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 25,
            "values": [
                {
                    "id": 12,
                    "dispName": "12"
                },
                {
                    "id": 25,
                    "dispName": "25"
                }
            ],
            "baseDim": "s",
            "dimension": "s",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 2}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_AVTE_TAIL",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0.04,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.04,
                    "dispName": "40 ms"
                },
                {
                    "id": 0.35,
                    "dispName": "0.35 s"
                },
                {
                    "id": 0.8,
                    "dispName": "0.8 s"
                },
                {
                    "id": 26,
                    "dispName": "26 s"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 4}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_AVUE_TAIL",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 0,
            "values": [
                {
                    "id": 0,
                    "dispName": "0 s"
                },
                {
                    "id": 0.025,
                    "dispName": "25 ms"
                },
                {
                    "id": 0.075,
                    "dispName": "75 ms"
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 1}],
        },
        {
            "id": "01_prfx_function_delay_ctrl_AVShE_TAIL",
            "label": "Function Delay",
            "control": "comboList",
            "defValue": 12,
            "values": [
                {
                    "id": 12,
                    "dispName": "12 s"
                },
                {
                    "id": 25,
                    "dispName": "25 s"
                },
                {
                    "id": 70,
                    "dispName": "70 s"
                },
                {
                    "id": 200,
                    "dispName": "3' 20\""
                }
            ],
            "baseDim": "",
            "dimension": "",
            "VisibilityCondition": [{"id": "NFP_fuze_type_tail", "value": 3}],
        }
    ],
}
