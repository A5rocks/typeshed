import abc
from _typeshed import Incomplete, Unused
from abc import ABC, ABCMeta, abstractmethod
from builtins import bool as _bool
from collections.abc import Callable, Generator, Iterable, Iterator, Sequence
from contextlib import contextmanager
from enum import Enum
from types import TracebackType
from typing import Any, Generic, Literal, TypeVar, overload
from typing_extensions import ParamSpec, Self

from google.protobuf.message import Message
from tensorflow import (
    data as data,
    experimental as experimental,
    feature_column as feature_column,
    initializers as initializers,
    io as io,
    keras as keras,
    math as math,
    types as types,
)
from tensorflow._aliases import (
    AnyArray,
    DTypeLike,
    IntArray,
    ScalarTensorCompatible,
    ShapeLike,
    Slice,
    SparseTensorCompatible,
    TensorCompatible,
    UIntTensorCompatible,
)
from tensorflow.autodiff import GradientTape as GradientTape
from tensorflow.core.protobuf import struct_pb2
from tensorflow.dtypes import *
from tensorflow.experimental.dtensor import Layout
from tensorflow.keras import losses as losses
from tensorflow.linalg import eye as eye

# Most tf.math functions are exported as tf, but sadly not all are.
from tensorflow.math import (
    abs as abs,
    add as add,
    add_n as add_n,
    argmax as argmax,
    argmin as argmin,
    cos as cos,
    cosh as cosh,
    divide as divide,
    equal as equal,
    greater as greater,
    greater_equal as greater_equal,
    less as less,
    less_equal as less_equal,
    logical_and as logical_and,
    logical_not as logical_not,
    logical_or as logical_or,
    maximum as maximum,
    minimum as minimum,
    multiply as multiply,
    not_equal as not_equal,
    pow as pow,
    reduce_max as reduce_max,
    reduce_mean as reduce_mean,
    reduce_min as reduce_min,
    reduce_prod as reduce_prod,
    reduce_sum as reduce_sum,
    round as round,
    sigmoid as sigmoid,
    sign as sign,
    sin as sin,
    sinh as sinh,
    sqrt as sqrt,
    square as square,
    subtract as subtract,
    tanh as tanh,
)
from tensorflow.python.trackable.autotrackable import AutoTrackable
from tensorflow.sparse import SparseTensor as SparseTensor

# Tensors ideally should be a generic type, but properly typing data type/shape
# will be a lot of work. Until we have good non-generic tensorflow stubs,
# we will skip making Tensor generic. Also good type hints for shapes will
# run quickly into many places where type system is not strong enough today.
# So shape typing is probably not worth doing anytime soon.
class Tensor:
    def __init__(self, op: Operation, value_index: int, dtype: DType) -> None: ...
    def consumers(self) -> list[Incomplete]: ...
    @property
    def shape(self) -> TensorShape: ...
    def get_shape(self) -> TensorShape: ...
    @property
    def dtype(self) -> DType: ...
    @property
    def graph(self) -> Graph: ...
    @property
    def name(self) -> str: ...
    @property
    def op(self) -> Operation: ...
    def numpy(self) -> AnyArray: ...
    def __int__(self) -> int: ...
    def __abs__(self, name: str | None = None) -> Tensor: ...
    def __add__(self, other: TensorCompatible) -> Tensor: ...
    def __radd__(self, other: TensorCompatible) -> Tensor: ...
    def __sub__(self, other: TensorCompatible) -> Tensor: ...
    def __rsub__(self, other: TensorCompatible) -> Tensor: ...
    def __mul__(self, other: TensorCompatible) -> Tensor: ...
    def __rmul__(self, other: TensorCompatible) -> Tensor: ...
    def __pow__(self, other: TensorCompatible) -> Tensor: ...
    def __matmul__(self, other: TensorCompatible) -> Tensor: ...
    def __rmatmul__(self, other: TensorCompatible) -> Tensor: ...
    def __floordiv__(self, other: TensorCompatible) -> Tensor: ...
    def __rfloordiv__(self, other: TensorCompatible) -> Tensor: ...
    def __truediv__(self, other: TensorCompatible) -> Tensor: ...
    def __rtruediv__(self, other: TensorCompatible) -> Tensor: ...
    def __neg__(self, name: str | None = None) -> Tensor: ...
    def __and__(self, other: TensorCompatible) -> Tensor: ...
    def __rand__(self, other: TensorCompatible) -> Tensor: ...
    def __or__(self, other: TensorCompatible) -> Tensor: ...
    def __ror__(self, other: TensorCompatible) -> Tensor: ...
    def __eq__(self, other: TensorCompatible) -> Tensor: ...  # type: ignore[override]
    def __ne__(self, other: TensorCompatible) -> Tensor: ...  # type: ignore[override]
    def __ge__(self, other: TensorCompatible, name: str | None = None) -> Tensor: ...
    def __gt__(self, other: TensorCompatible, name: str | None = None) -> Tensor: ...
    def __le__(self, other: TensorCompatible, name: str | None = None) -> Tensor: ...
    def __lt__(self, other: TensorCompatible, name: str | None = None) -> Tensor: ...
    def __bool__(self) -> _bool: ...
    def __getitem__(self, slice_spec: Slice | tuple[Slice, ...]) -> Tensor: ...
    def __len__(self) -> int: ...
    # This only works for rank 0 tensors.
    def __index__(self) -> int: ...
    def __getattr__(self, name: str) -> Incomplete: ...

class VariableSynchronization(Enum):
    AUTO = 0
    NONE = 1
    ON_WRITE = 2
    ON_READ = 3

class VariableAggregation(Enum):
    NONE = 0
    SUM = 1
    MEAN = 2
    ONLY_FIRST_REPLICA = 3

class _VariableMetaclass(type): ...

# Variable class in intent/documentation is a Tensor. In implementation there's
# TODO: comment to make it Tensor. It is not actually Tensor type wise, but even
# dynamically patches on most methods of tf.Tensor
# https://github.com/tensorflow/tensorflow/blob/9524a636cae9ae3f0554203c1ba7ee29c85fcf12/tensorflow/python/ops/variables.py#L1086.
class Variable(Tensor, metaclass=_VariableMetaclass):
    def __init__(
        self,
        initial_value: Tensor | Callable[[], Tensor] | None = None,
        trainable: _bool | None = None,
        validate_shape: _bool = True,
        # Valid non-None values are deprecated.
        caching_device: None = None,
        name: str | None = None,
        # Real type is VariableDef protobuf type. Can be added after adding script
        # to generate tensorflow protobuf stubs with mypy-protobuf.
        variable_def=None,
        dtype: DTypeLike | None = None,
        import_scope: str | None = None,
        constraint: Callable[[Tensor], Tensor] | None = None,
        synchronization: VariableSynchronization = ...,
        aggregation: VariableAggregation = ...,
        shape: ShapeLike | None = None,
        experimental_enable_variable_lifting: _bool = True,
    ) -> None: ...
    def __getattr__(self, name: str) -> Incomplete: ...

class RaggedTensor(metaclass=ABCMeta):
    def bounding_shape(
        self, axis: TensorCompatible | None = None, name: str | None = None, out_type: DTypeLike | None = None
    ) -> Tensor: ...
    @classmethod
    def from_sparse(cls, st_input: SparseTensor, name: str | None = None, row_splits_dtype: DTypeLike = ...) -> RaggedTensor: ...
    def to_sparse(self, name: str | None = None) -> SparseTensor: ...
    def to_tensor(
        self, default_value: float | str | None = None, name: str | None = None, shape: ShapeLike | None = None
    ) -> Tensor: ...
    def __add__(self, other: RaggedTensor | float, name: str | None = None) -> RaggedTensor: ...
    def __radd__(self, other: RaggedTensor | float, name: str | None = None) -> RaggedTensor: ...
    def __sub__(self, other: RaggedTensor | float, name: str | None = None) -> RaggedTensor: ...
    def __mul__(self, other: RaggedTensor | float, name: str | None = None) -> RaggedTensor: ...
    def __rmul__(self, other: RaggedTensor | float, name: str | None = None) -> RaggedTensor: ...
    def __floordiv__(self, other: RaggedTensor | float, name: str | None = None) -> RaggedTensor: ...
    def __truediv__(self, other: RaggedTensor | float, name: str | None = None) -> RaggedTensor: ...
    def __getitem__(self, slice_spec: Slice | tuple[Slice, ...]) -> RaggedTensor: ...
    def __getattr__(self, name: str) -> Incomplete: ...

class Operation:
    def __init__(
        self,
        node_def,
        g: Graph,
        # isinstance is used so can not be Sequence/Iterable.
        inputs: list[Tensor] | None = None,
        output_types: Unused = None,
        control_inputs: Iterable[Tensor | Operation] | None = None,
        input_types: Iterable[DType] | None = None,
        original_op: Operation | None = None,
        op_def=None,
    ) -> None: ...
    @property
    def inputs(self) -> list[Tensor]: ...
    @property
    def outputs(self) -> list[Tensor]: ...
    @property
    def device(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def type(self) -> str: ...
    def __getattr__(self, name: str) -> Incomplete: ...

class TensorShape(metaclass=ABCMeta):
    def __init__(self, dims: ShapeLike) -> None: ...
    @property
    def rank(self) -> int: ...
    def as_list(self) -> list[int | None]: ...
    def assert_has_rank(self, rank: int) -> None: ...
    def assert_is_compatible_with(self, other: Iterable[int | None]) -> None: ...
    def __bool__(self) -> _bool: ...
    @overload
    def __getitem__(self, key: int) -> int | None: ...
    @overload
    def __getitem__(self, key: slice) -> TensorShape: ...
    def __iter__(self) -> Iterator[int | None]: ...
    def __len__(self) -> int: ...
    def __add__(self, other: Iterable[int | None]) -> TensorShape: ...
    def __radd__(self, other: Iterable[int | None]) -> TensorShape: ...
    def __getattr__(self, name: str) -> Incomplete: ...

class Graph:
    def add_to_collection(self, name: str, value: object) -> None: ...
    def add_to_collections(self, names: Iterable[str] | str, value: object) -> None: ...
    @contextmanager
    def as_default(self) -> Generator[Self]: ...
    def finalize(self) -> None: ...
    def get_tensor_by_name(self, name: str) -> Tensor: ...
    def get_operation_by_name(self, name: str) -> Operation: ...
    def get_operations(self) -> list[Operation]: ...
    def get_name_scope(self) -> str: ...
    def __getattr__(self, name: str) -> Incomplete: ...

class IndexedSlices(metaclass=ABCMeta):
    def __init__(self, values: Tensor, indices: Tensor, dense_shape: None | Tensor = None) -> None: ...
    @property
    def values(self) -> Tensor: ...
    @property
    def indices(self) -> Tensor: ...
    @property
    def dense_shape(self) -> None | Tensor: ...
    @property
    def shape(self) -> TensorShape: ...
    @property
    def dtype(self) -> DType: ...
    @property
    def name(self) -> str: ...
    @property
    def op(self) -> Operation: ...
    @property
    def graph(self) -> Graph: ...
    @property
    def device(self) -> str: ...
    def __neg__(self) -> IndexedSlices: ...
    def consumers(self) -> list[Operation]: ...

class name_scope(metaclass=abc.ABCMeta):
    def __init__(self, name: str) -> None: ...
    def __enter__(self) -> str: ...
    def __exit__(self, typ: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None) -> None: ...

_P = ParamSpec("_P")
_R = TypeVar("_R")

class Module(AutoTrackable):
    def __init__(self, name: str | None = None) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def name_scope(self) -> name_scope: ...
    # Documentation only specifies these as returning Sequence. Actual
    # implementation does tuple.
    @property
    def variables(self) -> Sequence[Variable]: ...
    @property
    def trainable_variables(self) -> Sequence[Variable]: ...
    @property
    def non_trainable_variables(self) -> Sequence[Variable]: ...
    @property
    def submodules(self) -> Sequence[Module]: ...
    @classmethod
    def with_name_scope(cls, method: Callable[_P, _R]) -> Callable[_P, _R]: ...

class UnconnectedGradients(Enum):
    NONE = "none"
    ZERO = "zero"

_SpecProto = TypeVar("_SpecProto", bound=Message)

class TypeSpec(ABC, Generic[_SpecProto]):
    @property
    @abstractmethod
    def value_type(self) -> Any: ...
    def experimental_as_proto(self) -> _SpecProto: ...
    @classmethod
    def experimental_from_proto(cls, proto: _SpecProto) -> Self: ...
    @classmethod
    def experimental_type_proto(cls) -> type[_SpecProto]: ...
    def is_compatible_with(self, spec_or_value: Self | TensorCompatible | SparseTensor | RaggedTensor) -> _bool: ...
    # Incomplete as tf.types is not yet covered.
    def is_subtype_of(self, other) -> _bool: ...
    def most_specific_common_supertype(self, others: Sequence[Incomplete]) -> Self | None: ...
    def most_specific_compatible_type(self, other: Self) -> Self: ...

class TensorSpec(TypeSpec[struct_pb2.TensorSpecProto]):
    def __init__(self, shape: ShapeLike, dtype: DTypeLike = ..., name: str | None = None) -> None: ...
    @property
    def value_type(self) -> Tensor: ...
    @property
    def shape(self) -> TensorShape: ...
    @property
    def dtype(self) -> DType: ...
    @property
    def name(self) -> str | None: ...
    @classmethod
    def from_spec(cls, spec: TypeSpec[Any], name: str | None = None) -> Self: ...
    @classmethod
    def from_tensor(cls, tensor: Tensor, name: str | None = None) -> Self: ...
    def is_compatible_with(self, spec_or_tensor: Self | TensorCompatible) -> _bool: ...  # type: ignore[override]

class SparseTensorSpec(TypeSpec[struct_pb2.TypeSpecProto]):
    def __init__(self, shape: ShapeLike | None = None, dtype: DTypeLike = ...) -> None: ...
    @property
    def value_type(self) -> SparseTensor: ...
    @property
    def shape(self) -> TensorShape: ...
    @property
    def dtype(self) -> DType: ...
    @classmethod
    def from_value(cls, value: SparseTensor) -> Self: ...

class RaggedTensorSpec(TypeSpec[struct_pb2.TypeSpecProto]):
    def __init__(
        self,
        shape: ShapeLike | None = None,
        dtype: DTypeLike = ...,
        ragged_rank: int | None = None,
        row_splits_dtype: DTypeLike = ...,
        flat_values_spec: TypeSpec[Any] | None = None,
    ) -> None: ...
    @property
    def value_type(self) -> RaggedTensor: ...
    @property
    def shape(self) -> TensorShape: ...
    @property
    def dtype(self) -> DType: ...
    @classmethod
    def from_value(cls, value: RaggedTensor) -> Self: ...

def convert_to_tensor(
    value: TensorCompatible | IndexedSlices,
    dtype: DTypeLike | None = None,
    dtype_hint: DTypeLike | None = None,
    name: str | None = None,
) -> Tensor: ...
@overload
def expand_dims(input: TensorCompatible, axis: int, name: str | None = None) -> Tensor: ...
@overload
def expand_dims(input: RaggedTensor, axis: int, name: str | None = None) -> RaggedTensor: ...
@overload
def concat(values: TensorCompatible, axis: int, name: str | None = "concat") -> Tensor: ...
@overload
def concat(values: Sequence[RaggedTensor], axis: int, name: str | None = "concat") -> RaggedTensor: ...
@overload
def squeeze(
    input: TensorCompatible, axis: int | tuple[int, ...] | list[int] | None = None, name: str | None = None
) -> Tensor: ...
@overload
def squeeze(input: RaggedTensor, axis: int | tuple[int, ...] | list[int], name: str | None = None) -> RaggedTensor: ...
def tensor_scatter_nd_update(
    tensor: TensorCompatible, indices: TensorCompatible, updates: TensorCompatible, name: str | None = None
) -> Tensor: ...
def constant(
    value: TensorCompatible, dtype: DTypeLike | None = None, shape: ShapeLike | None = None, name: str | None = "Const"
) -> Tensor: ...
@overload
def cast(x: TensorCompatible, dtype: DTypeLike, name: str | None = None) -> Tensor: ...
@overload
def cast(x: SparseTensor, dtype: DTypeLike, name: str | None = None) -> SparseTensor: ...
@overload
def cast(x: RaggedTensor, dtype: DTypeLike, name: str | None = None) -> RaggedTensor: ...
def zeros(shape: ShapeLike, dtype: DTypeLike = ..., name: str | None = None, layout: Layout | None = None) -> Tensor: ...
def ones(shape: ShapeLike, dtype: DTypeLike = ..., name: str | None = None, layout: Layout | None = None) -> Tensor: ...
@overload
def zeros_like(
    input: TensorCompatible | IndexedSlices, dtype: DTypeLike | None = None, name: str | None = None, layout: Layout | None = None
) -> Tensor: ...
@overload
def zeros_like(
    input: RaggedTensor, dtype: DTypeLike | None = None, name: str | None = None, layout: Layout | None = None
) -> RaggedTensor: ...
@overload
def ones_like(
    input: TensorCompatible, dtype: DTypeLike | None = None, name: str | None = None, layout: Layout | None = None
) -> Tensor: ...
@overload
def ones_like(
    input: RaggedTensor, dtype: DTypeLike | None = None, name: str | None = None, layout: Layout | None = None
) -> RaggedTensor: ...
def reshape(tensor: TensorCompatible, shape: ShapeLike | Tensor, name: str | None = None) -> Tensor: ...
def pad(
    tensor: TensorCompatible,
    paddings: Tensor | IntArray | Iterable[Iterable[int]],
    mode: Literal["CONSTANT", "constant", "REFLECT", "reflect", "SYMMETRIC", "symmetric"] = "CONSTANT",
    constant_values: ScalarTensorCompatible = 0,
    name: str | None = None,
) -> Tensor: ...
def shape(input: SparseTensorCompatible, out_type: DTypeLike | None = None, name: str | None = None) -> Tensor: ...
def where(
    condition: TensorCompatible, x: TensorCompatible | None = None, y: TensorCompatible | None = None, name: str | None = None
) -> Tensor: ...
def gather_nd(
    params: TensorCompatible,
    indices: UIntTensorCompatible,
    batch_dims: UIntTensorCompatible = 0,
    name: str | None = None,
    bad_indices_policy: Literal["", "DEFAULT", "ERROR", "IGNORE"] = "",
) -> Tensor: ...
def __getattr__(name: str): ...  # incomplete module
