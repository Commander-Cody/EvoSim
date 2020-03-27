from Scenario.SimpleScenario import SimpleScenario


def main():
    cycles = 1000
    scenario = SimpleScenario(0.1)
    for i in range(cycles):
        scenario.advance()


if __name__ == '__main__':
    main()
