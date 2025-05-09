# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example/example_proto/demo/single_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example/example_proto/demo/single_config.proto',
  package='single_config',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n.example/example_proto/demo/single_config.proto\x12\rsingle_config\"\\\n\x0bUserMessage\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x02\x12\x10\n\x08is_adult\x18\x07 \x01(\x08\x12\x11\n\tuser_name\x18\x08 \x01(\tb\x06proto3'
)




_USERMESSAGE = _descriptor.Descriptor(
  name='UserMessage',
  full_name='single_config.UserMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='single_config.UserMessage.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='age', full_name='single_config.UserMessage.age', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='single_config.UserMessage.height', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_adult', full_name='single_config.UserMessage.is_adult', index=3,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='single_config.UserMessage.user_name', index=4,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=65,
  serialized_end=157,
)

DESCRIPTOR.message_types_by_name['UserMessage'] = _USERMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserMessage = _reflection.GeneratedProtocolMessageType('UserMessage', (_message.Message,), {
  'DESCRIPTOR' : _USERMESSAGE,
  '__module__' : 'example.example_proto.demo.single_config_pb2'
  # @@protoc_insertion_point(class_scope:single_config.UserMessage)
  })
_sym_db.RegisterMessage(UserMessage)


# @@protoc_insertion_point(module_scope)
