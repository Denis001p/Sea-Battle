import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * height for _ in range(width)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen, color, thick):
        top = self.top
        left = self.left
        size = self.cell_size
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, color, ((top, left), (size, size)), thick)
                left += size
            top += size
            left = self.left

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        x = (x - self.top) // self.cell_size
        y = (y - self.left) // self.cell_size
        return (x, y) if 0 <= x < self.width and 0 <= y < self.height else None

    def on_click(self, cell_coords):
        pass