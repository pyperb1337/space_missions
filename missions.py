def show_missions(missions):
    print("=== Каталог космических миссий ===")
    print()
    for index, mission in enumerate(missions, 1):
        print(f"{index}. {mission['name']}")
        print(f"Год запуска: {mission['year']}")
        print(f"Направление: {mission['direction']}")
        print()

def search_missions(missions, direction):
    found = []
    for mission in missions:
        if mission['direction'].lower() == direction.lower():
            found.append(mission)
    
    print("=== Результаты поиска ===")
    print()
    if found:
        for index, mission in enumerate(found, 1):
            print(f"{index}. {mission['name']}")
            print(f"Год запуска: {mission['year']}")
            print(f"Направление: {mission['direction']}")
            print()
    else:
        print("Миссии по данному направлению не найдены.")
        # Search logic