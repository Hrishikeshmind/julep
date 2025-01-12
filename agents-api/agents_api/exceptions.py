class AgentsBaseException(Exception):
    pass


class ModelNotSupportedError(AgentsBaseException):
    def __init__(self, model_name) -> None:
        super().__init__(f"model {model_name} is not supported")


class PromptTooBigError(AgentsBaseException):
    def __init__(self, token_count, max_tokens) -> None:
        super().__init__(
            f"prompt is too big, {token_count} tokens provided, exceeds maximum of {max_tokens}"
        )


class UnknownTokenizerError(AgentsBaseException):
    def __init__(self) -> None:
        super().__init__("unknown tokenizer")
