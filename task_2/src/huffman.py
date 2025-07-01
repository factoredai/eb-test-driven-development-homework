import dataclasses
import heapq
from collections.abc import Mapping
from typing import cast


@dataclasses.dataclass(kw_only=True)
class HuffmanTree:
    weight: int
    key: str | None = None
    children: tuple["HuffmanTree", "HuffmanTree"] | None = None

    ## homework:start
    @classmethod
    def from_frequenceies(cls, frequencies: Mapping[str, int]) -> "HuffmanTree":
      raise NotImplementedError
    ## homework:end


def create_prefix_code_table(tree: HuffmanTree) -> dict[str, str]:
    if tree.children is None:
        key = cast(str, tree.key)
        return {key: "0"}

    result: dict[str, str] = {}
    stack = [(tree, "")]
    while stack:
        root, code = stack.pop()
        if root.children is not None:
            left, right = root.children
            stack.append((left, code + "0"))
            stack.append((right, code + "1"))
            continue
        assert root.key is not None
        result[root.key] = code
    return result
