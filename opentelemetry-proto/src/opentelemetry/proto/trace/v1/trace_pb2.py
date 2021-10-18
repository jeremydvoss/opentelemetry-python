# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: opentelemetry/proto/trace/v1/trace.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from opentelemetry.proto.common.v1 import common_pb2 as opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2
from opentelemetry.proto.resource.v1 import resource_pb2 as opentelemetry_dot_proto_dot_resource_dot_v1_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='opentelemetry/proto/trace/v1/trace.proto',
  package='opentelemetry.proto.trace.v1',
  syntax='proto3',
  serialized_options=b'\n\037io.opentelemetry.proto.trace.v1B\nTraceProtoP\001Z=github.com/open-telemetry/opentelemetry-proto/gen/go/trace/v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(opentelemetry/proto/trace/v1/trace.proto\x12\x1copentelemetry.proto.trace.v1\x1a*opentelemetry/proto/common/v1/common.proto\x1a.opentelemetry/proto/resource/v1/resource.proto\"\xc2\x01\n\rResourceSpans\x12;\n\x08resource\x18\x01 \x01(\x0b\x32).opentelemetry.proto.resource.v1.Resource\x12`\n\x1dinstrumentation_library_spans\x18\x02 \x03(\x0b\x32\x39.opentelemetry.proto.trace.v1.InstrumentationLibrarySpans\x12\x12\n\nschema_url\x18\x03 \x01(\t\"\xbc\x01\n\x1bInstrumentationLibrarySpans\x12V\n\x17instrumentation_library\x18\x01 \x01(\x0b\x32\x35.opentelemetry.proto.common.v1.InstrumentationLibrary\x12\x31\n\x05spans\x18\x02 \x03(\x0b\x32\".opentelemetry.proto.trace.v1.Span\x12\x12\n\nschema_url\x18\x03 \x01(\t\"\xe6\x07\n\x04Span\x12\x10\n\x08trace_id\x18\x01 \x01(\x0c\x12\x0f\n\x07span_id\x18\x02 \x01(\x0c\x12\x13\n\x0btrace_state\x18\x03 \x01(\t\x12\x16\n\x0eparent_span_id\x18\x04 \x01(\x0c\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x39\n\x04kind\x18\x06 \x01(\x0e\x32+.opentelemetry.proto.trace.v1.Span.SpanKind\x12\x1c\n\x14start_time_unix_nano\x18\x07 \x01(\x06\x12\x1a\n\x12\x65nd_time_unix_nano\x18\x08 \x01(\x06\x12;\n\nattributes\x18\t \x03(\x0b\x32\'.opentelemetry.proto.common.v1.KeyValue\x12 \n\x18\x64ropped_attributes_count\x18\n \x01(\r\x12\x38\n\x06\x65vents\x18\x0b \x03(\x0b\x32(.opentelemetry.proto.trace.v1.Span.Event\x12\x1c\n\x14\x64ropped_events_count\x18\x0c \x01(\r\x12\x36\n\x05links\x18\r \x03(\x0b\x32\'.opentelemetry.proto.trace.v1.Span.Link\x12\x1b\n\x13\x64ropped_links_count\x18\x0e \x01(\r\x12\x34\n\x06status\x18\x0f \x01(\x0b\x32$.opentelemetry.proto.trace.v1.Status\x1a\x8c\x01\n\x05\x45vent\x12\x16\n\x0etime_unix_nano\x18\x01 \x01(\x06\x12\x0c\n\x04name\x18\x02 \x01(\t\x12;\n\nattributes\x18\x03 \x03(\x0b\x32\'.opentelemetry.proto.common.v1.KeyValue\x12 \n\x18\x64ropped_attributes_count\x18\x04 \x01(\r\x1a\x9d\x01\n\x04Link\x12\x10\n\x08trace_id\x18\x01 \x01(\x0c\x12\x0f\n\x07span_id\x18\x02 \x01(\x0c\x12\x13\n\x0btrace_state\x18\x03 \x01(\t\x12;\n\nattributes\x18\x04 \x03(\x0b\x32\'.opentelemetry.proto.common.v1.KeyValue\x12 \n\x18\x64ropped_attributes_count\x18\x05 \x01(\r\"\x99\x01\n\x08SpanKind\x12\x19\n\x15SPAN_KIND_UNSPECIFIED\x10\x00\x12\x16\n\x12SPAN_KIND_INTERNAL\x10\x01\x12\x14\n\x10SPAN_KIND_SERVER\x10\x02\x12\x14\n\x10SPAN_KIND_CLIENT\x10\x03\x12\x16\n\x12SPAN_KIND_PRODUCER\x10\x04\x12\x16\n\x12SPAN_KIND_CONSUMER\x10\x05\"\xdd\x07\n\x06Status\x12V\n\x0f\x64\x65precated_code\x18\x01 \x01(\x0e\x32\x39.opentelemetry.proto.trace.v1.Status.DeprecatedStatusCodeB\x02\x18\x01\x12\x0f\n\x07message\x18\x02 \x01(\t\x12=\n\x04\x63ode\x18\x03 \x01(\x0e\x32/.opentelemetry.proto.trace.v1.Status.StatusCode\"\xda\x05\n\x14\x44\x65precatedStatusCode\x12\x1d\n\x19\x44\x45PRECATED_STATUS_CODE_OK\x10\x00\x12$\n DEPRECATED_STATUS_CODE_CANCELLED\x10\x01\x12(\n$DEPRECATED_STATUS_CODE_UNKNOWN_ERROR\x10\x02\x12+\n\'DEPRECATED_STATUS_CODE_INVALID_ARGUMENT\x10\x03\x12,\n(DEPRECATED_STATUS_CODE_DEADLINE_EXCEEDED\x10\x04\x12$\n DEPRECATED_STATUS_CODE_NOT_FOUND\x10\x05\x12)\n%DEPRECATED_STATUS_CODE_ALREADY_EXISTS\x10\x06\x12,\n(DEPRECATED_STATUS_CODE_PERMISSION_DENIED\x10\x07\x12-\n)DEPRECATED_STATUS_CODE_RESOURCE_EXHAUSTED\x10\x08\x12.\n*DEPRECATED_STATUS_CODE_FAILED_PRECONDITION\x10\t\x12\"\n\x1e\x44\x45PRECATED_STATUS_CODE_ABORTED\x10\n\x12\'\n#DEPRECATED_STATUS_CODE_OUT_OF_RANGE\x10\x0b\x12(\n$DEPRECATED_STATUS_CODE_UNIMPLEMENTED\x10\x0c\x12)\n%DEPRECATED_STATUS_CODE_INTERNAL_ERROR\x10\r\x12&\n\"DEPRECATED_STATUS_CODE_UNAVAILABLE\x10\x0e\x12$\n DEPRECATED_STATUS_CODE_DATA_LOSS\x10\x0f\x12*\n&DEPRECATED_STATUS_CODE_UNAUTHENTICATED\x10\x10\"N\n\nStatusCode\x12\x15\n\x11STATUS_CODE_UNSET\x10\x00\x12\x12\n\x0eSTATUS_CODE_OK\x10\x01\x12\x15\n\x11STATUS_CODE_ERROR\x10\x02\x42n\n\x1fio.opentelemetry.proto.trace.v1B\nTraceProtoP\x01Z=github.com/open-telemetry/opentelemetry-proto/gen/go/trace/v1b\x06proto3'
  ,
  dependencies=[opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2.DESCRIPTOR,opentelemetry_dot_proto_dot_resource_dot_v1_dot_resource__pb2.DESCRIPTOR,])



_SPAN_SPANKIND = _descriptor.EnumDescriptor(
  name='SpanKind',
  full_name='opentelemetry.proto.trace.v1.Span.SpanKind',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SPAN_KIND_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPAN_KIND_INTERNAL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPAN_KIND_SERVER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPAN_KIND_CLIENT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPAN_KIND_PRODUCER', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPAN_KIND_CONSUMER', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1400,
  serialized_end=1553,
)
_sym_db.RegisterEnumDescriptor(_SPAN_SPANKIND)

_STATUS_DEPRECATEDSTATUSCODE = _descriptor.EnumDescriptor(
  name='DeprecatedStatusCode',
  full_name='opentelemetry.proto.trace.v1.Status.DeprecatedStatusCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEPRECATED_STATUS_CODE_OK', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPRECATED_STATUS_CODE_CANCELLED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPRECATED_STATUS_CODE_UNKNOWN_ERROR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPRECATED_STATUS_CODE_INVALID_ARGUMENT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPRECATED_STATUS_CODE_DEADLINE_EXCEEDED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPRECATED_STATUS_CODE_NOT_FOUND', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPRECATED_STATUS_CODE_ALREADY_EXISTS', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPRECATED_STATUS_CODE_PERMISSION_DENIED', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPRECATED_STATUS_CODE_RESOURCE_EXHAUSTED', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPRECATED_STATUS_CODE_FAILED_PRECONDITION', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPRECATED_STATUS_CODE_ABORTED', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPRECATED_STATUS_CODE_OUT_OF_RANGE', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPRECATED_STATUS_CODE_UNIMPLEMENTED', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPRECATED_STATUS_CODE_INTERNAL_ERROR', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPRECATED_STATUS_CODE_UNAVAILABLE', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPRECATED_STATUS_CODE_DATA_LOSS', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPRECATED_STATUS_CODE_UNAUTHENTICATED', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1735,
  serialized_end=2465,
)
_sym_db.RegisterEnumDescriptor(_STATUS_DEPRECATEDSTATUSCODE)

_STATUS_STATUSCODE = _descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='opentelemetry.proto.trace.v1.Status.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_CODE_UNSET', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_CODE_OK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_CODE_ERROR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2467,
  serialized_end=2545,
)
_sym_db.RegisterEnumDescriptor(_STATUS_STATUSCODE)


_RESOURCESPANS = _descriptor.Descriptor(
  name='ResourceSpans',
  full_name='opentelemetry.proto.trace.v1.ResourceSpans',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource', full_name='opentelemetry.proto.trace.v1.ResourceSpans.resource', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instrumentation_library_spans', full_name='opentelemetry.proto.trace.v1.ResourceSpans.instrumentation_library_spans', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schema_url', full_name='opentelemetry.proto.trace.v1.ResourceSpans.schema_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=361,
)


_INSTRUMENTATIONLIBRARYSPANS = _descriptor.Descriptor(
  name='InstrumentationLibrarySpans',
  full_name='opentelemetry.proto.trace.v1.InstrumentationLibrarySpans',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instrumentation_library', full_name='opentelemetry.proto.trace.v1.InstrumentationLibrarySpans.instrumentation_library', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='spans', full_name='opentelemetry.proto.trace.v1.InstrumentationLibrarySpans.spans', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schema_url', full_name='opentelemetry.proto.trace.v1.InstrumentationLibrarySpans.schema_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=364,
  serialized_end=552,
)


_SPAN_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='opentelemetry.proto.trace.v1.Span.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_unix_nano', full_name='opentelemetry.proto.trace.v1.Span.Event.time_unix_nano', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='opentelemetry.proto.trace.v1.Span.Event.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='opentelemetry.proto.trace.v1.Span.Event.attributes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dropped_attributes_count', full_name='opentelemetry.proto.trace.v1.Span.Event.dropped_attributes_count', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1097,
  serialized_end=1237,
)

_SPAN_LINK = _descriptor.Descriptor(
  name='Link',
  full_name='opentelemetry.proto.trace.v1.Span.Link',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='opentelemetry.proto.trace.v1.Span.Link.trace_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='span_id', full_name='opentelemetry.proto.trace.v1.Span.Link.span_id', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trace_state', full_name='opentelemetry.proto.trace.v1.Span.Link.trace_state', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='opentelemetry.proto.trace.v1.Span.Link.attributes', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dropped_attributes_count', full_name='opentelemetry.proto.trace.v1.Span.Link.dropped_attributes_count', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1240,
  serialized_end=1397,
)

_SPAN = _descriptor.Descriptor(
  name='Span',
  full_name='opentelemetry.proto.trace.v1.Span',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='opentelemetry.proto.trace.v1.Span.trace_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='span_id', full_name='opentelemetry.proto.trace.v1.Span.span_id', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trace_state', full_name='opentelemetry.proto.trace.v1.Span.trace_state', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent_span_id', full_name='opentelemetry.proto.trace.v1.Span.parent_span_id', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='opentelemetry.proto.trace.v1.Span.name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kind', full_name='opentelemetry.proto.trace.v1.Span.kind', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_time_unix_nano', full_name='opentelemetry.proto.trace.v1.Span.start_time_unix_nano', index=6,
      number=7, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_time_unix_nano', full_name='opentelemetry.proto.trace.v1.Span.end_time_unix_nano', index=7,
      number=8, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='opentelemetry.proto.trace.v1.Span.attributes', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dropped_attributes_count', full_name='opentelemetry.proto.trace.v1.Span.dropped_attributes_count', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='events', full_name='opentelemetry.proto.trace.v1.Span.events', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dropped_events_count', full_name='opentelemetry.proto.trace.v1.Span.dropped_events_count', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='links', full_name='opentelemetry.proto.trace.v1.Span.links', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dropped_links_count', full_name='opentelemetry.proto.trace.v1.Span.dropped_links_count', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='opentelemetry.proto.trace.v1.Span.status', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SPAN_EVENT, _SPAN_LINK, ],
  enum_types=[
    _SPAN_SPANKIND,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=555,
  serialized_end=1553,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='opentelemetry.proto.trace.v1.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deprecated_code', full_name='opentelemetry.proto.trace.v1.Status.deprecated_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='opentelemetry.proto.trace.v1.Status.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='opentelemetry.proto.trace.v1.Status.code', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATUS_DEPRECATEDSTATUSCODE,
    _STATUS_STATUSCODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1556,
  serialized_end=2545,
)

_RESOURCESPANS.fields_by_name['resource'].message_type = opentelemetry_dot_proto_dot_resource_dot_v1_dot_resource__pb2._RESOURCE
_RESOURCESPANS.fields_by_name['instrumentation_library_spans'].message_type = _INSTRUMENTATIONLIBRARYSPANS
_INSTRUMENTATIONLIBRARYSPANS.fields_by_name['instrumentation_library'].message_type = opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2._INSTRUMENTATIONLIBRARY
_INSTRUMENTATIONLIBRARYSPANS.fields_by_name['spans'].message_type = _SPAN
_SPAN_EVENT.fields_by_name['attributes'].message_type = opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2._KEYVALUE
_SPAN_EVENT.containing_type = _SPAN
_SPAN_LINK.fields_by_name['attributes'].message_type = opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2._KEYVALUE
_SPAN_LINK.containing_type = _SPAN
_SPAN.fields_by_name['kind'].enum_type = _SPAN_SPANKIND
_SPAN.fields_by_name['attributes'].message_type = opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2._KEYVALUE
_SPAN.fields_by_name['events'].message_type = _SPAN_EVENT
_SPAN.fields_by_name['links'].message_type = _SPAN_LINK
_SPAN.fields_by_name['status'].message_type = _STATUS
_SPAN_SPANKIND.containing_type = _SPAN
_STATUS.fields_by_name['deprecated_code'].enum_type = _STATUS_DEPRECATEDSTATUSCODE
_STATUS.fields_by_name['code'].enum_type = _STATUS_STATUSCODE
_STATUS_DEPRECATEDSTATUSCODE.containing_type = _STATUS
_STATUS_STATUSCODE.containing_type = _STATUS
DESCRIPTOR.message_types_by_name['ResourceSpans'] = _RESOURCESPANS
DESCRIPTOR.message_types_by_name['InstrumentationLibrarySpans'] = _INSTRUMENTATIONLIBRARYSPANS
DESCRIPTOR.message_types_by_name['Span'] = _SPAN
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResourceSpans = _reflection.GeneratedProtocolMessageType('ResourceSpans', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCESPANS,
  '__module__' : 'opentelemetry.proto.trace.v1.trace_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.trace.v1.ResourceSpans)
  })
_sym_db.RegisterMessage(ResourceSpans)

InstrumentationLibrarySpans = _reflection.GeneratedProtocolMessageType('InstrumentationLibrarySpans', (_message.Message,), {
  'DESCRIPTOR' : _INSTRUMENTATIONLIBRARYSPANS,
  '__module__' : 'opentelemetry.proto.trace.v1.trace_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.trace.v1.InstrumentationLibrarySpans)
  })
_sym_db.RegisterMessage(InstrumentationLibrarySpans)

Span = _reflection.GeneratedProtocolMessageType('Span', (_message.Message,), {

  'Event' : _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
    'DESCRIPTOR' : _SPAN_EVENT,
    '__module__' : 'opentelemetry.proto.trace.v1.trace_pb2'
    # @@protoc_insertion_point(class_scope:opentelemetry.proto.trace.v1.Span.Event)
    })
  ,

  'Link' : _reflection.GeneratedProtocolMessageType('Link', (_message.Message,), {
    'DESCRIPTOR' : _SPAN_LINK,
    '__module__' : 'opentelemetry.proto.trace.v1.trace_pb2'
    # @@protoc_insertion_point(class_scope:opentelemetry.proto.trace.v1.Span.Link)
    })
  ,
  'DESCRIPTOR' : _SPAN,
  '__module__' : 'opentelemetry.proto.trace.v1.trace_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.trace.v1.Span)
  })
_sym_db.RegisterMessage(Span)
_sym_db.RegisterMessage(Span.Event)
_sym_db.RegisterMessage(Span.Link)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'opentelemetry.proto.trace.v1.trace_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.trace.v1.Status)
  })
_sym_db.RegisterMessage(Status)


DESCRIPTOR._options = None
_STATUS.fields_by_name['deprecated_code']._options = None
# @@protoc_insertion_point(module_scope)
