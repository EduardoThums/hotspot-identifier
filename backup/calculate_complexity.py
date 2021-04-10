import json


if __name__ == '__main__':
    with open('radon-cc-output.json') as file:
        radon_analysis = json.load(file)
        code_complexity = {}
        
        for file_name, blocks in list(radon_analysis.items())[:50]:
            total_complexity = sum([block['complexity'] for block in blocks])
            average_complexity = round((total_complexity / len(blocks)), 2) 

            code_complexity[file_name] = average_complexity

        most_complexy_files = sorted(radon_analysis.keys(), key=lambda file_name: code_complexity[file_name])

    with open('code-complexity.list', 'w') as file:
        for file_name in most_complexy_files:
            file.write(f'{file_name}\n')
