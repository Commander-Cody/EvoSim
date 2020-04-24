import pygame
import numpy
from Scenario.PrimordialSoupScenario import PrimordialSoup
from Scenario.SimpleScenario import SimpleScenario


def main():
    cycles = 1000
    scenario = create_primordial_soup_scenario()
    for i in range(cycles):
        scenario.advance()

    scenario.finish()


def create_simple_scenario():
    return SimpleScenario(0.1)


def create_primordial_soup_scenario():
    return PrimordialSoup()


if __name__ == '__main__':
    main()
