# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .call_evaluation import CallEvaluation

__all__ = ["CallGetEvaluationsResponse"]

CallGetEvaluationsResponse: TypeAlias = List[CallEvaluation]
