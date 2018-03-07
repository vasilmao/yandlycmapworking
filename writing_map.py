def map_image(content):
    import sys
    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)
    return 'map.png'