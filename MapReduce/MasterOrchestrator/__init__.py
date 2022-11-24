# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df

from functools import reduce

def orchestrator_function(context: df.DurableOrchestrationContext):
    get_input_data = yield context.call_activity('GetInputDataFn', "ass2-mapreduce-container")
    activities = []
    res3 = []
    for file in get_input_data:
        activities.append(context.call_activity("MapperFunction", file))
    res = yield context.task_all(activities)
    res1 = reduce(lambda k1, k2 :k1 + k2, res)
    res2 = yield context.call_activity('ShufflerFunction', res1)
    for word in res2:
        mid_res = yield context.call_activity('ReducerFunction', (word, res2[word]))
        res3.append(mid_res)
    return res3
main = df.Orchestrator.create(orchestrator_function)