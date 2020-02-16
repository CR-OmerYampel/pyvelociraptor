# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyvelociraptor/api.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyvelociraptor/api.proto',
  package='proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x18pyvelociraptor/api.proto\x12\x05proto\x1a\x1bgoogle/protobuf/empty.proto\"\'\n\nVQLRequest\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12\x0b\n\x03VQL\x18\x01 \x01(\t\"$\n\x06VQLEnv\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x8b\x01\n\x10VQLCollectorArgs\x12\x1a\n\x03\x65nv\x18\x03 \x03(\x0b\x32\r.proto.VQLEnv\x12 \n\x05Query\x18\x02 \x03(\x0b\x32\x11.proto.VQLRequest\x12\x0f\n\x07max_row\x18\x04 \x01(\x04\x12\x10\n\x08max_wait\x18\x06 \x01(\x04\x12\x16\n\x0eops_per_second\x18\x18 \x01(\x02\"*\n\nVQLTypeMap\x12\x0e\n\x06\x63olumn\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"\xbb\x01\n\x0bVQLResponse\x12\x10\n\x08Response\x18\x01 \x01(\t\x12\x0f\n\x07\x43olumns\x18\x02 \x03(\t\x12 \n\x05types\x18\x08 \x03(\x0b\x32\x11.proto.VQLTypeMap\x12\x10\n\x08query_id\x18\x05 \x01(\x04\x12\x0c\n\x04part\x18\x06 \x01(\x04\x12 \n\x05Query\x18\x03 \x01(\x0b\x32\x11.proto.VQLRequest\x12\x11\n\ttimestamp\x18\x04 \x01(\x04\x12\x12\n\ntotal_rows\x18\x07 \x01(\x04\x32{\n\x03\x41PI\x12\x38\n\x05Query\x12\x17.proto.VQLCollectorArgs\x1a\x12.proto.VQLResponse\"\x00\x30\x01\x12:\n\nWriteEvent\x12\x12.proto.VQLResponse\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_VQLREQUEST = _descriptor.Descriptor(
  name='VQLRequest',
  full_name='proto.VQLRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='proto.VQLRequest.Name', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='VQL', full_name='proto.VQLRequest.VQL', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=64,
  serialized_end=103,
)


_VQLENV = _descriptor.Descriptor(
  name='VQLEnv',
  full_name='proto.VQLEnv',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.VQLEnv.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.VQLEnv.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=105,
  serialized_end=141,
)


_VQLCOLLECTORARGS = _descriptor.Descriptor(
  name='VQLCollectorArgs',
  full_name='proto.VQLCollectorArgs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='env', full_name='proto.VQLCollectorArgs.env', index=0,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Query', full_name='proto.VQLCollectorArgs.Query', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_row', full_name='proto.VQLCollectorArgs.max_row', index=2,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_wait', full_name='proto.VQLCollectorArgs.max_wait', index=3,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ops_per_second', full_name='proto.VQLCollectorArgs.ops_per_second', index=4,
      number=24, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=144,
  serialized_end=283,
)


_VQLTYPEMAP = _descriptor.Descriptor(
  name='VQLTypeMap',
  full_name='proto.VQLTypeMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='column', full_name='proto.VQLTypeMap.column', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='proto.VQLTypeMap.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=285,
  serialized_end=327,
)


_VQLRESPONSE = _descriptor.Descriptor(
  name='VQLResponse',
  full_name='proto.VQLResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Response', full_name='proto.VQLResponse.Response', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Columns', full_name='proto.VQLResponse.Columns', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='types', full_name='proto.VQLResponse.types', index=2,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query_id', full_name='proto.VQLResponse.query_id', index=3,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='part', full_name='proto.VQLResponse.part', index=4,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Query', full_name='proto.VQLResponse.Query', index=5,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='proto.VQLResponse.timestamp', index=6,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_rows', full_name='proto.VQLResponse.total_rows', index=7,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=330,
  serialized_end=517,
)

_VQLCOLLECTORARGS.fields_by_name['env'].message_type = _VQLENV
_VQLCOLLECTORARGS.fields_by_name['Query'].message_type = _VQLREQUEST
_VQLRESPONSE.fields_by_name['types'].message_type = _VQLTYPEMAP
_VQLRESPONSE.fields_by_name['Query'].message_type = _VQLREQUEST
DESCRIPTOR.message_types_by_name['VQLRequest'] = _VQLREQUEST
DESCRIPTOR.message_types_by_name['VQLEnv'] = _VQLENV
DESCRIPTOR.message_types_by_name['VQLCollectorArgs'] = _VQLCOLLECTORARGS
DESCRIPTOR.message_types_by_name['VQLTypeMap'] = _VQLTYPEMAP
DESCRIPTOR.message_types_by_name['VQLResponse'] = _VQLRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VQLRequest = _reflection.GeneratedProtocolMessageType('VQLRequest', (_message.Message,), {
  'DESCRIPTOR' : _VQLREQUEST,
  '__module__' : 'pyvelociraptor.api_pb2'
  # @@protoc_insertion_point(class_scope:proto.VQLRequest)
  })
_sym_db.RegisterMessage(VQLRequest)

VQLEnv = _reflection.GeneratedProtocolMessageType('VQLEnv', (_message.Message,), {
  'DESCRIPTOR' : _VQLENV,
  '__module__' : 'pyvelociraptor.api_pb2'
  # @@protoc_insertion_point(class_scope:proto.VQLEnv)
  })
_sym_db.RegisterMessage(VQLEnv)

VQLCollectorArgs = _reflection.GeneratedProtocolMessageType('VQLCollectorArgs', (_message.Message,), {
  'DESCRIPTOR' : _VQLCOLLECTORARGS,
  '__module__' : 'pyvelociraptor.api_pb2'
  # @@protoc_insertion_point(class_scope:proto.VQLCollectorArgs)
  })
_sym_db.RegisterMessage(VQLCollectorArgs)

VQLTypeMap = _reflection.GeneratedProtocolMessageType('VQLTypeMap', (_message.Message,), {
  'DESCRIPTOR' : _VQLTYPEMAP,
  '__module__' : 'pyvelociraptor.api_pb2'
  # @@protoc_insertion_point(class_scope:proto.VQLTypeMap)
  })
_sym_db.RegisterMessage(VQLTypeMap)

VQLResponse = _reflection.GeneratedProtocolMessageType('VQLResponse', (_message.Message,), {
  'DESCRIPTOR' : _VQLRESPONSE,
  '__module__' : 'pyvelociraptor.api_pb2'
  # @@protoc_insertion_point(class_scope:proto.VQLResponse)
  })
_sym_db.RegisterMessage(VQLResponse)



_API = _descriptor.ServiceDescriptor(
  name='API',
  full_name='proto.API',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=519,
  serialized_end=642,
  methods=[
  _descriptor.MethodDescriptor(
    name='Query',
    full_name='proto.API.Query',
    index=0,
    containing_service=None,
    input_type=_VQLCOLLECTORARGS,
    output_type=_VQLRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='WriteEvent',
    full_name='proto.API.WriteEvent',
    index=1,
    containing_service=None,
    input_type=_VQLRESPONSE,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_API)

DESCRIPTOR.services_by_name['API'] = _API

# @@protoc_insertion_point(module_scope)
