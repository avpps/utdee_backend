from typing import Dict


def env_file_parser(env_file_path) -> Dict[str, str]:
    with open(env_file_path, encoding="utf-8") as file:
        lines = file.readlines()

    result = {}
    for line in lines:
        if not line.strip():
            continue
        key, value = line.split("=")
        result[key.strip()] = value.strip()
    return result


def env_files_keys_equal(env_file_1: Dict[str, str], env_file_2: Dict[str, str]) -> bool:
    keys_1 = sorted(list(env_file_1.keys()))
    keys_2 = sorted(list(env_file_2.keys()))
    all_keys = keys_1 == keys_2
    if not all_keys:
        print(".env_template file keys are not aligned with local .env file")
        return False
    return True
