# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: example.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'example.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rexample.proto\x12\x07student\"W\n\x07Student\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\x12\x0e\n\x06scores\x18\x03 \x01(\x0c\x12\r\n\x05shape\x18\x04 \x03(\x05\x12\x12\n\nattributes\x18\x05 \x01(\t\"9\n\x12\x41\x64\x64StudentResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x12\n\nstudent_id\x18\x02 \x01(\x05\"\x1f\n\x11GetStudentRequest\x12\n\n\x02id\x18\x02 \x01(\x05\x32\x89\x01\n\x0eStudentService\x12;\n\nAddStudent\x12\x10.student.Student\x1a\x1b.student.AddStudentResponse\x12:\n\nGetStudent\x12\x1a.student.GetStudentRequest\x1a\x10.student.Studentb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'example_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_STUDENT']._serialized_start=26
  _globals['_STUDENT']._serialized_end=113
  _globals['_ADDSTUDENTRESPONSE']._serialized_start=115
  _globals['_ADDSTUDENTRESPONSE']._serialized_end=172
  _globals['_GETSTUDENTREQUEST']._serialized_start=174
  _globals['_GETSTUDENTREQUEST']._serialized_end=205
  _globals['_STUDENTSERVICE']._serialized_start=208
  _globals['_STUDENTSERVICE']._serialized_end=345
# @@protoc_insertion_point(module_scope)
