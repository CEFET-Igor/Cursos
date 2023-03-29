"""
Faça um programa em Python que abra e
reproduzam o áudio de um arquivo MP3.
"""
import pygame
pygame.init()
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play()
pygame.event.wait()
