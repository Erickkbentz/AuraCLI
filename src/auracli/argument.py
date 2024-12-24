from typing import Optional, List, Any


class Argument:
    def __init__(
        self,
        name: str,
        message: Optional[str] = None,
        required: Optional[bool] = False,
        default: Optional[str] = None,
        choices: Optional[List[Any]] = None,
        type: Optional[type] = str,
    ):
        """
        Initialize an Argument object.

        Args:
            name (str):
                The name of the argument.
            message (Optional[str]):
                The help message to display for the argument.
            required (Optional[bool]):
                Whether the argument is required.
            default (Optional[str]):
                The default value for the argument.
            choices (Optional[List[Any]]):
                The choices available for the argument.
            type (Optional[type]):
                The type of the argument.
        """
        self.name = name
        self.message = message
        self.required = required
        self.default = default
        self.choices = choices
        self.type = type