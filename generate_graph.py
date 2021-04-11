import json

import matplotlib.pyplot as plt

RADON_CC_OUTPUT_PATH = './radon-cc-output.json'
CHURN_OUTPUT_PATH = './churn.list'


def calculate_code_complexity():
    code_complexity = {}

    with open(RADON_CC_OUTPUT_PATH) as file:
        radon_analysis = json.load(file)

        for file_name, blocks in list(radon_analysis.items())[:50]:
            total_complexity = sum([block['complexity'] for block in blocks])
            average_complexity = round((total_complexity / len(blocks)), 2)

            code_complexity[file_name] = average_complexity

        return code_complexity


def calculate_churn():
    churn = {}

    with open(CHURN_OUTPUT_PATH) as file:
        for line in file.readlines():
            churn_per_file = line.strip().replace('\n', '').split(' ')

            changed_times = churn_per_file[0]
            file_name = churn_per_file[1]

            churn[file_name] = changed_times

    return churn


if __name__ == '__main__':
    churn = calculate_churn()
    code_complexity = calculate_code_complexity()

    churn_values = list(churn.values())[::-1]
    code_complexity_values = list(code_complexity.values())[::-1]

    churn_length = len(churn_values)
    code_complexity_length = len(code_complexity_values)

    if code_complexity_length > churn_length:
        code_complexity_values = code_complexity_values[:churn_length]

    elif churn_length > code_complexity_length:
        churn_values = churn_values[:code_complexity_length]

    plt.xlabel('Churn')
    plt.ylabel('Code Complexity')

    plt.scatter(
        x=churn_values,
        y=code_complexity_values
    )

    # TODO: find a better way to store the generated chart with reasonable dimensions
    # plt.savefig('./code-complexity-vs-churn.jpeg')

    plt.show()
