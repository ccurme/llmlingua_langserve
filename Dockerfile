FROM python:3.10

WORKDIR /llmlingua_langserve

COPY . /llmlingua_langserve

RUN pip install poetry
RUN poetry install

EXPOSE 8000

ENV HOST=0.0.0.0
ENV PORT=8000
CMD ["poetry", "run", "python", "llmlingua_langserve/langserver.py"]
