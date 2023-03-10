import jsonpickle

from Backend.Help.synagogue import SynagogueList
from Backend.Help.gabai import GabaiList, Gabai

if __name__ == '__main__':
    x = SynagogueList()
    y = GabaiList()
    y.gabai_list.append(Gabai("admin", 1, "1243", "054548111", []))
    jsonpickle.set_encoder_options('json', sort_keys=False, indent=4)
    frozen = jsonpickle.encode(x.synagogues)
    with open("data_syng.json", "w") as text_file:
        print(frozen, file=text_file)
    with open("index_syng.txt", "w") as text_file:
        print(str(x.nextid), file=text_file)

    jsonpickle.set_encoder_options('json', sort_keys=False, indent=4)
    frozen = jsonpickle.encode(y.gabai_list)
    with open('data_gabai.json', "w") as text_file:
        print(frozen, file=text_file)
    with open("index_gabai.txt", "w") as text_file:
        print(str(y.nextid), file=text_file)


'''



'''