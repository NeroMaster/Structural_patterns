from mine_facade import MineFacade

def main():
    facade = MineFacade()
    facade.start_new_day()
    facade.dig_out()
    facade.end_day()

if __name__ == "__main__":
    main()