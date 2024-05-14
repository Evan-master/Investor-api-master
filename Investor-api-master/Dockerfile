FROM python:slim-bullseye
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.7.1 /lambda-adapter /opt/extensions/lambda-adapter
WORKDIR /app
COPY ./* .
RUN pip install -r requirements.txt
CMD bash

ENTRYPOINT ["/usr/local/bin/python", "./app.py"]

