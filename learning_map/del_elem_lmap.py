import json

def del_elem_lmap(data,del_elem):
    with open(data,encoding='utf-8') as f:
        f_data = json.load(f)
        for dic,levels in f_data.items():
            for level,program in levels.items():
                if del_elem in program:
                    program.remove(del_elem)
                    with open(data,'w',encoding='utf-8') as f:
                        json.dump(f_data,f)
                    return del_elem