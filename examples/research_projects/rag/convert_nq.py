import argparse
from random import choice

import jsonlines


def convert_dataset(source_file, target_question_file, target_answer_file):
    with jsonlines.open(source_file, "r") as source, open(target_question_file, "w") as target_question, open(
        target_answer_file, "w"
    ) as target_answer:
        for line in source:
            answer = choice(line["answer"])
            question = line["question"]
            target_question.write(question + "\n")
            target_answer.write(answer + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source_file",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--target_path",
        type=str,
        required=True,
    )
    parser.add_argument("--split", required=True, type=str, choices=["train", "val"])
    args = parser.parse_args()

    convert_dataset(
        args.source_file,
        args.target_path + "/" + args.split + ".source",
        args.target_path + "/" + args.split + ".target",
    )
