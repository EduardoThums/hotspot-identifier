import json

RADON_CC_OUTPUT_PATH = './radon-cc-output.json'
CODE_COMPLEXITY_LIST_PATH = './code-complexity.list'

if __name__ == '__main__':
    with open(RADON_CC_OUTPUT_PATH) as file:
        radon_analysis = json.load(file)
        code_complexity = {}

        for file_name, blocks in list(radon_analysis.items())[:50]:
            total_complexity = sum([block['complexity'] for block in blocks])
            average_complexity = round((total_complexity / len(blocks)), 2)

            code_complexity[file_name] = average_complexity

        most_complex_files = sorted(radon_analysis.keys(), key=lambda file_name: code_complexity[file_name])

    with open(CODE_COMPLEXITY_LIST_PATH, 'w') as file:
        for file_name in most_complex_files:
            file.write(f'{file_name}\n')
