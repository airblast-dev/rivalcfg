from .. import usbhid


profile = {
    "name": "SteelSeries Aerox 3 Wireless",
    "models": [
        {
            "name": "SteelSeries Aerox 3 Wireless (wired mode)",
            "vendor_id": 0x1038,
            "product_id": 0x183A,
            "endpoint": 3,
        },
    ],
    "settings": {
        "sensitivity": {
            "label": "Sensibility presets",
            "description": "Set sensitivity preset (DPI)",
            "cli": ["-s", "--sensitivity"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x2D],
            "value_type": "multidpi_range",
            "input_range": [200, 8500, 100],
            "output_range": [0x04, 0xC5, 2.33],
            "dpi_length_byte": 1,
            "count_mode": "number",
            "max_preset_count": 5,
            "default": "800, 1600",
        },
        "polling_rate": {
            "label": "Polling rate",
            "description": "Set polling rate (Hz)",
            "cli": ["-p", "--polling-rate"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x2B],
            "value_type": "choice",
            "choices": {
                125: 0x03,
                250: 0x02,
                500: 0x01,
                1000: 0x00,
            },
            "default": 1000,
        },
        "z1_color": {
            "label": "Strip top LED color",
            "description": "Set the color of the top LED",
            "cli": ["--top-color", "--z1"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x21, 0x01, 0x00],
            "value_type": "rgbcolor",
            "default": "red",
        },
        "z2_color": {
            "label": "Strip middle LED color",
            "description": "Set the color of the middle LED",
            "cli": ["--middle-color", "--z2"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x21, 0x01, 0x01],
            "value_type": "rgbcolor",
            "default": "lime",
        },
        "z3_color": {
            "label": "Strip bottom LED color",
            "description": "Set the color of the bottom LED",
            "cli": ["--bottom-color", "--z3"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x21, 0x01, 0x02],
            "value_type": "rgbcolor",
            "default": "blue",
        },
        "led_brightness": {
            "label": "LED Brightness",
            "description": "Set the brightness of the LEDs",
            "cli": ["-l", "--led-brightness"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x23],
            "command_suffix": [0x01, 0x01, 0x00, 0x30, 0x75, 0x00],
            "value_type": "range",
            "input_range": [0, 15, 1],
            "output_range": [0x00, 0x0F, 1],
            "default": 15,
        },
        "buttons_mapping": {
            "label": "Buttons mapping",
            "description": "Set the mapping of the buttons",
            "cli": ["-b", "--buttons"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x2A],
            "value_type": "buttons",
            # fmt: off
            "buttons": {
                "Button1":    {"id": 0x01, "offset": 0x00, "default": "button1"},
                "Button2":    {"id": 0x02, "offset": 0x05, "default": "button2"},
                "Button3":    {"id": 0x03, "offset": 0x0A, "default": "button3"},
                "Button4":    {"id": 0x04, "offset": 0x0F, "default": "button4"},
                "Button5":    {"id": 0x05, "offset": 0x14, "default": "button5"},
                "Button6":    {"id": 0x06, "offset": 0x19, "default": "dpi"},
                "ScrollUp"  : {"id": 0x31, "offset": 0x1E, "default": "scrollup"},
                "ScrollDown": {"id": 0x32, "offset": 0x23, "default": "scrolldown"},
            },
            "button_field_length": 5,
            "button_disable":     0x00,
            "button_keyboard":    0x51,
            "button_multimedia":  0x61,
            "button_dpi_switch":  0x30,
            "button_scroll_up":   None,
            "button_scroll_down": None,
            # fmt: on
            "default": "buttons(button1=button1; button2=button2; button3=button3; button4=button4; button5=button5; button6=dpi; scrollup=scrollup; scrolldown=scrolldown; layout=qwerty)",
        },
        "rainbow_effect": {
            "label": "rainbow effect",
            "description": "Enable the rainbow effect (can be disabled by setting a color)",
            "cli": ["-e", "--rainbow-effect"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x22, 0xFF],
            "value_type": "none",
        },
    },
    "save_command": {
        "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
        "command": [0x11, 0x00],
    },
}
