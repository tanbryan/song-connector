import os
import re

SECTION_MAPPING = {
    "主歌": "verse",
    "副歌": "chorus",
    "前奏": "intro",
    "尾奏": "outro",
    "桥段": "bridge"
    
}

ELEMENT_MAPPING = {
    "前奏弱起": "intro_upbeat",

}

def parse_filenames(directory_path):
    files = os.listdir(directory_path)
    sections = {}
    transition = {}

    # 解析主要部分
    for file in files:
        filepath = os.path.join(directory_path, file)
        if os.path.isfile(filepath):
            # 主干映射文件对应
            for keyword, section in SECTION_MAPPING.items():
                if keyword in file and "主干" in file:
                    sections[section] = filepath
            # 特殊元素
            for keyword, section in ELEMENT_MAPPING.items():
                if keyword in file:
                    sections[section] = filepath

    # 解析过渡部分
    for folder in files:
        folder_path = os.path.join(directory_path, folder)
        if os.path.isdir(folder_path):
            # 文件夹名映射主干
            for keyword, section in SECTION_MAPPING.items():
                if keyword in folder:
                    transition[section] = {}
                    # 解析文件夹内部文件名， 例如：主歌尾巴/快乐1 主歌尾巴-接主歌.mp3
                    for bridge_file in os.listdir(folder_path):
                        target_section_keyword = re.search(r'接(.+?)\.mp3', bridge_file)
                        if target_section_keyword:
                            target_keyword = target_section_keyword.group(1)
                        
                            for key, target_section in SECTION_MAPPING.items():
                                if target_keyword in key:
                                    transition[section][target_section] = os.path.join(folder_path, bridge_file)

    return sections, transition