import pygame_image_showing
import computing_coords
import requesting_map_image
import writing_map


def main():
    centerx, centery, sp1, sp2 = computing_coords.find_coords('США')
    map_content = requesting_map_image.map_request(centerx, centery, sp1, sp2)
    map_file = writing_map.map_image(map_content)
    pygame_image_showing.show_map(map_file)

main()
