
import pygame
import sys

class JoyStick:
    ''' Class of the joystick '''
    @staticmethod
    def GetPosition() -> int:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    return -1
                elif event.key == pygame.K_RIGHT:
                    return 1
                else:
                    return 0
            else:
                return 0


