FROM hashicorp/terraform:1.2.6 AS terraform

FROM python:3.8
COPY --from=terraform /bin/terraform /usr/bin/terraform
WORKDIR /infrastructure/
COPY ./ ./
RUN pip install --no-cache-dir --upgrade -r tflocal-requirements.txt
ENV LOCALSTACK_HOSTNAME=localstack
RUN chmod +x ./scripts/terraform-steps.sh
CMD ["./scripts/terraform-steps.sh"]
