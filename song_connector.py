
from file_processor import parse_filenames
from audio_merger import merge_audio
from directory_handler import get_valid_directory
import os

def main():
    # 获取有目录路径
    directory_path = get_valid_directory()  
    sections, transition = parse_filenames(directory_path)
    user_input_str = input("Please enter the song structure (e.g., [verse][chorus][verse]): ")
    
    # # 测试
    # user_input_str= "[verse][verse][chorus][verse][chorus][chorus]"
    user_sections = [section.strip("[]") for section in user_input_str.split("]") if section]
    
    # 添加开场和结尾部分
    user_sections = ["intro_upbeat"] + ["intro"] + user_sections + ["outro"]
    files_to_merge = []

    # 找对应的音频文件
    for i in range(len(user_sections) - 1):
        section, next_section = user_sections[i], user_sections[i + 1]
        section_path = sections.get(section, "")

        if not section_path.strip():  
            print(f"Error: Path for section '{section}' not found.")
        else:
            files_to_merge.append(section_path)  

        transition_path = transition.get(section, {}).get(next_section, "")

        if not transition_path.strip():  
            print(f"Warning: Transition path from '{section}' to '{next_section}' not found.")
        else:
            files_to_merge.append(transition_path)

    outro = user_sections[-1]
    outro_path = sections.get(outro, "")
    if not outro_path.strip():  
        print(f"Error: Path for outro '{outro}' not found.")
    else:
        files_to_merge.append(outro_path)
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    final_filename = os.path.basename(os.path.normpath(directory_path)) + ".mp3"
    
    # 合并音频文件
    merged_audio = merge_audio(files_to_merge)

    # 导出合并后的音频文件
    merged_audio.export(os.path.join(output_dir, final_filename), format="mp3")
    print(f"Finished integrating'{final_filename}'!")
