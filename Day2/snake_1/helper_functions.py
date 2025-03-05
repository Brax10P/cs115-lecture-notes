#------
# Function Definitions
#-----
"""
This Function Draws Text to the Screen
Text: Holds our Text
Coordinate: Holds Coord Values
text_color: Color of Text
"""
def draw_text(text, coordinate, text_color, my_font, screen):
  text_image = my_font.render(text, True, text_color)
  text_rect = text_image.get_rect()
  text_rect.topleft = coordinate
  screen.blit(text_image, text_rect)