def interpolate_colors_hex(color1, color2, num_colors):
    def hex_to_rgb(hex_color):
    # Remove the '#' and convert to integer
        return tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

    def rgb_to_hex(rgb_color):
    # Convert each element to hex and format
        return '#' + ''.join(f'{int(c):02x}' for c in rgb_color)
    
    # Convert colors to numpy arrays for vectorized operations
    color1 = np.array(hex_to_rgb(color1))
    color2 = np.array(hex_to_rgb(color2))
    
    # Generate a list of 't' values to determine the ratio of interpolation
    t_values = np.linspace(0, 1, num_colors)
    
    # Calculate interpolated colors and convert them to hexadecimal format
    colors = []
    for t in t_values:
        interpolated_color = tuple(map(int, color1 + t * (color2 - color1)))
        hex_color = rgb_to_hex(interpolated_color)
        colors.append(hex_color)
    
    return colors