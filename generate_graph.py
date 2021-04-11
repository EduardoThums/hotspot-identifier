import matplotlib.pyplot as plt

if __name__ == '__main__':
    with open('./code-complexity.list') as cc_file, open('./churn.list') as churn_file:
        cc_files = [line.replace('\n', '') for line in cc_file.readlines()]
        churn_files = [line.replace('\n', '') for line in churn_file.readlines()]

        cc_length = len(cc_files)
        churn_length = len(churn_files)

        if cc_length > churn_length:
            cc_files = cc_files[:churn_length]

        elif churn_length > cc_length:
            churn_files = churn_files[:cc_length]

        plt.xlabel('Churn')
        plt.ylabel('Code Complexity')

        plt.scatter(
            x=cc_files,
            y=churn_files
        )

        plt.show()

        plt.savefig('./code-complexity-vs-churn.jpeg')
