import goslate


def india_states_to_json():
    gs = goslate.Goslate(service_urls=['http://translate.google.de'])
    with open("india_states", 'r') as reader:
        with open("india_states.json", 'a') as writer:
            writer.write("[")
            for line in reader:
                writer.write("\"" + gs.translate(line, 'te') + "\",")
            writer.write("]")


def world_countries_to_json():
    gs = goslate.Goslate(service_urls=['http://translate.google.de'])
    with open("world_countries", 'r') as reader:
        with open("world_countries.json", 'a') as writer:
            writer.write("[")
            for line in reader:
                writer.write("\"" + line.strip() + "\",")
            writer.write("]")


if __name__ == "__main__":
    world_countries_to_json()