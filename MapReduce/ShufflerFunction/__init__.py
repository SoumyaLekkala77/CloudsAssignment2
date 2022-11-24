# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


def main(input: list) -> dict:
    res = {}
    for wpos in input:
        (word, position) = wpos
        pos = res.get(word)
        if pos is None:
            pos = [position]
        else:
            pos.append(position)
        res[word] = pos
    return res
