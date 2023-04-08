import colorgram

def extract_colors():
    # TODO: teacher's solution
    rgb_colors = []
    colors = colorgram.extract("image_hirst.jpg", 40)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    # print(rgb_colors)
    return rgb_colors

# colors_set is a list object
# TODO: MY SOLUTION
# extract_colors = colorgram.extract("image_hirst.jpg", 5 * 8)
# print(extract_colors)
# # print(len(colors_set))
# color_list = []
# for number_of_color in range(len(extract_colors)):
#     select_color = extract_colors[number_of_color]
#     rgb = select_color.rgb
#     r = rgb[0]
#     g = rgb[1]
#     b = rgb[2]
#     color = (r, g, b)
#     color_list.append(color)
# print(color_list)
