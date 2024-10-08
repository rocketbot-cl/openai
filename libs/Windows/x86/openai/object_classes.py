from __future__ import absolute_import, division, print_function

from r_openai import api_resources
from r_openai.api_resources.experimental.completion_config import CompletionConfig

OBJECT_CLASSES = {
    "engine": api_resources.Engine,
    "experimental.completion_config": CompletionConfig,
    "file": api_resources.File,
    "fine-tune": api_resources.FineTune,
    "snapshot": api_resources.Snapshot,
}
