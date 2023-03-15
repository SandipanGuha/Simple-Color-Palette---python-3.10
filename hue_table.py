import pygame


class hue():
    channel: pygame.Color
    rgb_notation: tuple[int,int,int]
    hex_notation: str
    html_notation: str

    def __init__(self, channel:tuple[int,int,int] | list[int,int,int]) -> None:
        self.channel = pygame.Color(channel)
        self.rgb_notation = tuple([self.channel.r,self.channel.g,self.channel.b])
        self.hex_notation = rgb_to_hex(self.rgb_notation)
        self.html_notation = rgb_to_html(self.rgb_notation)

    def get_color(self)->pygame.Color:
        return self.channel
    def get_rgb_notation(self) -> tuple:
        return self.rgb_notation

    #def set_rgb_notation(self, rgb =tuple[int,int,int] | list[int,int,int]):
        #self.rgb_notation = tuple(rgb)

    def get_hex_notation(self) -> str:
        return self.hex_notation

    def get_html_notation(self) -> str:
        return self.html_notation

    #def set_hex_notation(self, rgb =tuple[int,int,int] | list[int,int,int]):
        #self.hex_notation = rgb_to_hex(rgb)

    def update_channel(self, channel:tuple[int,int,int] | list[int,int,int]) -> None:
        self.__init__(channel)
    #COMMENT:  HTML notation is same as hexadecimal notation therefore no extra function is not required !!

    def rgb_to_hex(self, rgb =tuple[int,int,int] | list[int,int,int], uppercase:bool = False) -> str:
        if uppercase:
            return '0x' + (('').join([hex(value)[2:] for value in rgb])).upper()  # Example: 0xA48D4D or 0xFF00FF
        return '0x' + ('').join([hex(value)[2:] for value in rgb])   #Example: 0xa48d4d or 0xff00ff

    def rgb_to_html(self, rgb =tuple[int,int,int] | list[int,int,int], uppercase:bool = False) -> str:
        if uppercase:
            return '#' + ('').join([hex(value)[2:] for value in rgb])   #Example: #A48D4D or #FF00FF
        return '#' + ('').join([hex(value)[2:] for value in rgb]) #Example: #a48d4d or #ff00ff