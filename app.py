def hex_to_rgb(hex_color):
    # Converts a hex color string to an RGB tuple.
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(r, g, b):
    # Converts RGB values to hex.
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def get_brightness(hex_color):
    # Returns the perceived luminance of a hex color as a value between 0 and 1
    r, g, b = hex_to_rgb(hex_color)
    luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255.0
    return luminance


def set_brightness(hex_color, target_brightness):
   # Adjusts the brightness of the given hex color to the target brightness.
    r, g, b = hex_to_rgb(hex_color)
    current_brightness = get_brightness(hex_color)

    # Avoid division by zero
    if current_brightness == 0:
        factor = 0
    else:
        factor = target_brightness / current_brightness

    r = min(255, int(r * factor))
    g = min(255, int(g * factor))
    b = min(255, int(b * factor))

    return rgb_to_hex(r, g, b)


# Test
print(get_brightness("#fbbc05"))
print(set_brightness("#fbbc05", 0.6888235294117647))
