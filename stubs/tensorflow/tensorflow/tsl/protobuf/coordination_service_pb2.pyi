"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import sys
import typing

import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _CoordinatedTaskState:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _CoordinatedTaskStateEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_CoordinatedTaskState.ValueType], builtins.type
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    TASKSTATE_UNSPECIFIED: _CoordinatedTaskState.ValueType  # 0
    """TASKSTATE_UNSPECIFIED is an invalid state such that indicates a bug."""
    TASKSTATE_UNINITIALIZED: _CoordinatedTaskState.ValueType  # 1
    """TASKSTATE_UNINITIALIZED is an agent-only state. While the agent is
    disconnected, the service has no way of knowing if the task is
    initialized/uninitialized.
    """
    TASKSTATE_DISCONNECTED: _CoordinatedTaskState.ValueType  # 2
    TASKSTATE_CONNECTED: _CoordinatedTaskState.ValueType  # 3
    TASKSTATE_ERROR: _CoordinatedTaskState.ValueType  # 4

class CoordinatedTaskState(_CoordinatedTaskState, metaclass=_CoordinatedTaskStateEnumTypeWrapper):
    """Represents the state of a remote worker"""

TASKSTATE_UNSPECIFIED: CoordinatedTaskState.ValueType  # 0
"""TASKSTATE_UNSPECIFIED is an invalid state such that indicates a bug."""
TASKSTATE_UNINITIALIZED: CoordinatedTaskState.ValueType  # 1
"""TASKSTATE_UNINITIALIZED is an agent-only state. While the agent is
disconnected, the service has no way of knowing if the task is
initialized/uninitialized.
"""
TASKSTATE_DISCONNECTED: CoordinatedTaskState.ValueType  # 2
TASKSTATE_CONNECTED: CoordinatedTaskState.ValueType  # 3
TASKSTATE_ERROR: CoordinatedTaskState.ValueType  # 4
global___CoordinatedTaskState = CoordinatedTaskState

@typing.final
class CoordinatedTask(google.protobuf.message.Message):
    """Represents a remote worker task, specified by job name and task id."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_NAME_FIELD_NUMBER: builtins.int
    TASK_ID_FIELD_NUMBER: builtins.int
    job_name: builtins.str
    task_id: builtins.int
    def __init__(self, *, job_name: builtins.str | None = ..., task_id: builtins.int | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["job_name", b"job_name", "task_id", b"task_id"]) -> None: ...

global___CoordinatedTask = CoordinatedTask

@typing.final
class CoordinationServiceError(google.protobuf.message.Message):
    """Status payload for all coordination service errors.
    Note: an empty proto may be set if the error is triggered by the task's own
    agent calls (i.e. not propagated by the service from another remote task).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IS_REPORTED_ERROR_FIELD_NUMBER: builtins.int
    SOURCE_TASK_FIELD_NUMBER: builtins.int
    is_reported_error: builtins.bool
    """If true, error is reported via the agent API by the user (and not an
    internal service error).
    """
    @property
    def source_task(self) -> global___CoordinatedTask:
        """Denotes which task hit the error. If unset, the error originated from the
        same task that is processing this error.
        """

    def __init__(
        self, *, is_reported_error: builtins.bool | None = ..., source_task: global___CoordinatedTask | None = ...
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["source_task", b"source_task"]) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing.Literal["is_reported_error", b"is_reported_error", "source_task", b"source_task"]
    ) -> None: ...

global___CoordinationServiceError = CoordinationServiceError

@typing.final
class CoordinatedTaskStateInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TASK_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    ERROR_CODE_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    ERROR_PAYLOAD_FIELD_NUMBER: builtins.int
    state: global___CoordinatedTaskState.ValueType
    error_code: builtins.int
    error_message: builtins.str
    @property
    def task(self) -> global___CoordinatedTask: ...
    @property
    def error_payload(self) -> global___CoordinationServiceError: ...
    def __init__(
        self,
        *,
        task: global___CoordinatedTask | None = ...,
        state: global___CoordinatedTaskState.ValueType | None = ...,
        error_code: builtins.int | None = ...,
        error_message: builtins.str | None = ...,
        error_payload: global___CoordinationServiceError | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["error_payload", b"error_payload", "task", b"task"]) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "error_code",
            b"error_code",
            "error_message",
            b"error_message",
            "error_payload",
            b"error_payload",
            "state",
            b"state",
            "task",
            b"task",
        ],
    ) -> None: ...

global___CoordinatedTaskStateInfo = CoordinatedTaskStateInfo

@typing.final
class DeviceInfo(google.protobuf.message.Message):
    """Placeholder message to be extended by other runtimes' device representations."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_FIELD_NUMBER: builtins.int
    @property
    def device(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]: ...
    def __init__(self, *, device: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["device", b"device"]) -> None: ...

global___DeviceInfo = DeviceInfo

@typing.final
class RegisterTaskRequest(google.protobuf.message.Message):
    """Request and response messages for registering a task to the cluster leader.
    A task is uniquely represented by its `job_name`, `task_id` and
    `incarnation`. Leader responds with its `incarnation` to identify a leader
    process.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INCARNATION_FIELD_NUMBER: builtins.int
    SOURCE_TASK_FIELD_NUMBER: builtins.int
    incarnation: builtins.int
    @property
    def source_task(self) -> global___CoordinatedTask: ...
    def __init__(self, *, incarnation: builtins.int | None = ..., source_task: global___CoordinatedTask | None = ...) -> None: ...
    def HasField(self, field_name: typing.Literal["source_task", b"source_task"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["incarnation", b"incarnation", "source_task", b"source_task"]) -> None: ...

global___RegisterTaskRequest = RegisterTaskRequest

@typing.final
class RegisterTaskResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LEADER_INCARNATION_FIELD_NUMBER: builtins.int
    leader_incarnation: builtins.int
    def __init__(self, *, leader_incarnation: builtins.int | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["leader_incarnation", b"leader_incarnation"]) -> None: ...

global___RegisterTaskResponse = RegisterTaskResponse

@typing.final
class HeartbeatRequest(google.protobuf.message.Message):
    """Request and response messages for sending heartbeats."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INCARNATION_FIELD_NUMBER: builtins.int
    SOURCE_TASK_FIELD_NUMBER: builtins.int
    incarnation: builtins.int
    @property
    def source_task(self) -> global___CoordinatedTask: ...
    def __init__(self, *, incarnation: builtins.int | None = ..., source_task: global___CoordinatedTask | None = ...) -> None: ...
    def HasField(self, field_name: typing.Literal["source_task", b"source_task"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["incarnation", b"incarnation", "source_task", b"source_task"]) -> None: ...

global___HeartbeatRequest = HeartbeatRequest

@typing.final
class HeartbeatResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LEADER_INCARNATION_FIELD_NUMBER: builtins.int
    leader_incarnation: builtins.int
    """If there are failures in cluster, use additional metadata in response to
    broadcast error code and message to other tasks.
    """
    def __init__(self, *, leader_incarnation: builtins.int | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["leader_incarnation", b"leader_incarnation"]) -> None: ...

global___HeartbeatResponse = HeartbeatResponse

@typing.final
class PollForErrorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOURCE_TASK_FIELD_NUMBER: builtins.int
    @property
    def source_task(self) -> global___CoordinatedTask: ...
    def __init__(self, *, source_task: global___CoordinatedTask | None = ...) -> None: ...
    def HasField(self, field_name: typing.Literal["source_task", b"source_task"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["source_task", b"source_task"]) -> None: ...

global___PollForErrorRequest = PollForErrorRequest

@typing.final
class PollForErrorResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None: ...

global___PollForErrorResponse = PollForErrorResponse

@typing.final
class WaitForAllTasksRequest(google.protobuf.message.Message):
    """Request and response messages for waiting for all tasks."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOURCE_TASK_FIELD_NUMBER: builtins.int
    DEVICE_INFO_FIELD_NUMBER: builtins.int
    @property
    def source_task(self) -> global___CoordinatedTask: ...
    @property
    def device_info(self) -> global___DeviceInfo:
        """All local device attributes on the request sender;"""

    def __init__(
        self, *, source_task: global___CoordinatedTask | None = ..., device_info: global___DeviceInfo | None = ...
    ) -> None: ...
    def HasField(
        self, field_name: typing.Literal["device_info", b"device_info", "source_task", b"source_task"]
    ) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["device_info", b"device_info", "source_task", b"source_task"]) -> None: ...

global___WaitForAllTasksRequest = WaitForAllTasksRequest

@typing.final
class WaitForAllTasksResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LEADER_INCARNATION_FIELD_NUMBER: builtins.int
    DEVICE_INFO_FIELD_NUMBER: builtins.int
    leader_incarnation: builtins.int
    @property
    def device_info(self) -> global___DeviceInfo:
        """All devices in the cluster."""

    def __init__(
        self, *, leader_incarnation: builtins.int | None = ..., device_info: global___DeviceInfo | None = ...
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["device_info", b"device_info"]) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing.Literal["device_info", b"device_info", "leader_incarnation", b"leader_incarnation"]
    ) -> None: ...

global___WaitForAllTasksResponse = WaitForAllTasksResponse

@typing.final
class ShutdownTaskRequest(google.protobuf.message.Message):
    """Request and response messages for disconnecting a task from the service."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOURCE_TASK_FIELD_NUMBER: builtins.int
    @property
    def source_task(self) -> global___CoordinatedTask: ...
    def __init__(self, *, source_task: global___CoordinatedTask | None = ...) -> None: ...
    def HasField(self, field_name: typing.Literal["source_task", b"source_task"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["source_task", b"source_task"]) -> None: ...

global___ShutdownTaskRequest = ShutdownTaskRequest

@typing.final
class ShutdownTaskResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None: ...

global___ShutdownTaskResponse = ShutdownTaskResponse

@typing.final
class ResetTaskRequest(google.protobuf.message.Message):
    """Request and response messages for resetting a task state in the service."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOURCE_TASK_FIELD_NUMBER: builtins.int
    @property
    def source_task(self) -> global___CoordinatedTask: ...
    def __init__(self, *, source_task: global___CoordinatedTask | None = ...) -> None: ...
    def HasField(self, field_name: typing.Literal["source_task", b"source_task"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["source_task", b"source_task"]) -> None: ...

global___ResetTaskRequest = ResetTaskRequest

@typing.final
class ResetTaskResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None: ...

global___ResetTaskResponse = ResetTaskResponse

@typing.final
class ReportErrorToTaskRequest(google.protobuf.message.Message):
    """Request and response messages for reporting errors to task."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ERROR_CODE_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    ERROR_PAYLOAD_FIELD_NUMBER: builtins.int
    error_code: builtins.int
    error_message: builtins.str
    @property
    def error_payload(self) -> global___CoordinationServiceError: ...
    def __init__(
        self,
        *,
        error_code: builtins.int | None = ...,
        error_message: builtins.str | None = ...,
        error_payload: global___CoordinationServiceError | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["error_payload", b"error_payload"]) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "error_code", b"error_code", "error_message", b"error_message", "error_payload", b"error_payload"
        ],
    ) -> None: ...

global___ReportErrorToTaskRequest = ReportErrorToTaskRequest

@typing.final
class ReportErrorToTaskResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None: ...

global___ReportErrorToTaskResponse = ReportErrorToTaskResponse

@typing.final
class ReportErrorToServiceRequest(google.protobuf.message.Message):
    """Request and response messages for reporting errors to service instance."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ERROR_CODE_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    ERROR_ORIGIN_FIELD_NUMBER: builtins.int
    error_code: builtins.int
    error_message: builtins.str
    @property
    def error_origin(self) -> global___CoordinatedTask: ...
    def __init__(
        self,
        *,
        error_code: builtins.int | None = ...,
        error_message: builtins.str | None = ...,
        error_origin: global___CoordinatedTask | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["error_origin", b"error_origin"]) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "error_code", b"error_code", "error_message", b"error_message", "error_origin", b"error_origin"
        ],
    ) -> None: ...

global___ReportErrorToServiceRequest = ReportErrorToServiceRequest

@typing.final
class ReportErrorToServiceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None: ...

global___ReportErrorToServiceResponse = ReportErrorToServiceResponse

@typing.final
class GetTaskStateRequest(google.protobuf.message.Message):
    """Request and response messages for getting state of a remote task."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOURCE_TASK_FIELD_NUMBER: builtins.int
    @property
    def source_task(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CoordinatedTask]: ...
    def __init__(self, *, source_task: collections.abc.Iterable[global___CoordinatedTask] | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["source_task", b"source_task"]) -> None: ...

global___GetTaskStateRequest = GetTaskStateRequest

@typing.final
class GetTaskStateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TASK_STATE_FIELD_NUMBER: builtins.int
    @property
    def task_state(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CoordinatedTaskStateInfo]: ...
    def __init__(self, *, task_state: collections.abc.Iterable[global___CoordinatedTaskStateInfo] | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["task_state", b"task_state"]) -> None: ...

global___GetTaskStateResponse = GetTaskStateResponse

@typing.final
class KeyValueEntry(google.protobuf.message.Message):
    """Message for configuration key value.
    Key is structured like Unix file system, with multiple levels of directory
    names separated by the slash ('/') characters.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    key: builtins.str
    value: builtins.bytes
    def __init__(self, *, key: builtins.str | None = ..., value: builtins.bytes | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

global___KeyValueEntry = KeyValueEntry

@typing.final
class InsertKeyValueRequest(google.protobuf.message.Message):
    """Request and response messages for inserting configuration key-value data."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KV_FIELD_NUMBER: builtins.int
    ALLOW_OVERWRITE_FIELD_NUMBER: builtins.int
    allow_overwrite: builtins.bool
    @property
    def kv(self) -> global___KeyValueEntry: ...
    def __init__(self, *, kv: global___KeyValueEntry | None = ..., allow_overwrite: builtins.bool | None = ...) -> None: ...
    def HasField(self, field_name: typing.Literal["kv", b"kv"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["allow_overwrite", b"allow_overwrite", "kv", b"kv"]) -> None: ...

global___InsertKeyValueRequest = InsertKeyValueRequest

@typing.final
class InsertKeyValueResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None: ...

global___InsertKeyValueResponse = InsertKeyValueResponse

@typing.final
class GetKeyValueRequest(google.protobuf.message.Message):
    """Request and response messages for getting configuration key-value data."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    key: builtins.str
    def __init__(self, *, key: builtins.str | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["key", b"key"]) -> None: ...

global___GetKeyValueRequest = GetKeyValueRequest

@typing.final
class GetKeyValueResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KV_FIELD_NUMBER: builtins.int
    @property
    def kv(self) -> global___KeyValueEntry: ...
    def __init__(self, *, kv: global___KeyValueEntry | None = ...) -> None: ...
    def HasField(self, field_name: typing.Literal["kv", b"kv"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["kv", b"kv"]) -> None: ...

global___GetKeyValueResponse = GetKeyValueResponse

@typing.final
class TryGetKeyValueRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    key: builtins.str
    def __init__(self, *, key: builtins.str | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["key", b"key"]) -> None: ...

global___TryGetKeyValueRequest = TryGetKeyValueRequest

@typing.final
class TryGetKeyValueResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KV_FIELD_NUMBER: builtins.int
    @property
    def kv(self) -> global___KeyValueEntry: ...
    def __init__(self, *, kv: global___KeyValueEntry | None = ...) -> None: ...
    def HasField(self, field_name: typing.Literal["kv", b"kv"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["kv", b"kv"]) -> None: ...

global___TryGetKeyValueResponse = TryGetKeyValueResponse

@typing.final
class GetKeyValueDirRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DIRECTORY_KEY_FIELD_NUMBER: builtins.int
    directory_key: builtins.str
    def __init__(self, *, directory_key: builtins.str | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["directory_key", b"directory_key"]) -> None: ...

global___GetKeyValueDirRequest = GetKeyValueDirRequest

@typing.final
class GetKeyValueDirResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DIRECTORY_KEY_FIELD_NUMBER: builtins.int
    KV_FIELD_NUMBER: builtins.int
    directory_key: builtins.str
    @property
    def kv(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___KeyValueEntry]: ...
    def __init__(
        self, *, directory_key: builtins.str | None = ..., kv: collections.abc.Iterable[global___KeyValueEntry] | None = ...
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["directory_key", b"directory_key", "kv", b"kv"]) -> None: ...

global___GetKeyValueDirResponse = GetKeyValueDirResponse

@typing.final
class DeleteKeyValueRequest(google.protobuf.message.Message):
    """Request and response messages for deleting configuration key-value data.
    When is_directory is true, delete key-values recursively under `key`.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    IS_DIRECTORY_FIELD_NUMBER: builtins.int
    key: builtins.str
    is_directory: builtins.bool
    def __init__(self, *, key: builtins.str | None = ..., is_directory: builtins.bool | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["is_directory", b"is_directory", "key", b"key"]) -> None: ...

global___DeleteKeyValueRequest = DeleteKeyValueRequest

@typing.final
class DeleteKeyValueResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None: ...

global___DeleteKeyValueResponse = DeleteKeyValueResponse

@typing.final
class BarrierRequest(google.protobuf.message.Message):
    """Request and response messages for generic sync barriers."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BARRIER_ID_FIELD_NUMBER: builtins.int
    BARRIER_TIMEOUT_IN_MS_FIELD_NUMBER: builtins.int
    TASKS_FIELD_NUMBER: builtins.int
    SOURCE_TASK_FIELD_NUMBER: builtins.int
    barrier_id: builtins.str
    barrier_timeout_in_ms: builtins.int
    @property
    def tasks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CoordinatedTask]:
        """Denotes list of tasks that will wait for the barrier. If unspecified, it
        implies that the entire cluster is participating in the barrier.
        """

    @property
    def source_task(self) -> global___CoordinatedTask:
        """Task that is making the request."""

    def __init__(
        self,
        *,
        barrier_id: builtins.str | None = ...,
        barrier_timeout_in_ms: builtins.int | None = ...,
        tasks: collections.abc.Iterable[global___CoordinatedTask] | None = ...,
        source_task: global___CoordinatedTask | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["source_task", b"source_task"]) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "barrier_id",
            b"barrier_id",
            "barrier_timeout_in_ms",
            b"barrier_timeout_in_ms",
            "source_task",
            b"source_task",
            "tasks",
            b"tasks",
        ],
    ) -> None: ...

global___BarrierRequest = BarrierRequest

@typing.final
class BarrierResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None: ...

global___BarrierResponse = BarrierResponse

@typing.final
class CancelBarrierRequest(google.protobuf.message.Message):
    """Request and response messages for  cancelling generic sync barriers."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BARRIER_ID_FIELD_NUMBER: builtins.int
    SOURCE_TASK_FIELD_NUMBER: builtins.int
    barrier_id: builtins.str
    @property
    def source_task(self) -> global___CoordinatedTask:
        """Task that is making the request."""

    def __init__(self, *, barrier_id: builtins.str | None = ..., source_task: global___CoordinatedTask | None = ...) -> None: ...
    def HasField(self, field_name: typing.Literal["source_task", b"source_task"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["barrier_id", b"barrier_id", "source_task", b"source_task"]) -> None: ...

global___CancelBarrierRequest = CancelBarrierRequest

@typing.final
class CancelBarrierResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None: ...

global___CancelBarrierResponse = CancelBarrierResponse
