FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt --target "${LAMBDA_RUNTIME_DIR}"
RUN pip install --no-cache-dir --upgrade  mangum --target "${LAMBDA_RUNTIME_DIR}"

COPY . ${LAMBDA_TASK_ROOT}

CMD [ "runner_lambda.handler" ]
