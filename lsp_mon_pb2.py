# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lsp_mon.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='lsp_mon.proto',
  package='',
  serialized_pb='\n\rlsp_mon.proto\"E\n\x03key\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x1b\n\x13instance_identifier\x18\x02 \x02(\x05\x12\x13\n\x0btime_stampg\x18\x03 \x02(\x04\"_\n\x16lsp_monitor_data_event\x12$\n\x10\x65vent_identifier\x18\x01 \x02(\x0e\x32\n.lsp_event\x12\x1f\n\x07subcode\x18\x02 \x01(\x0e\x32\x0e.event_subcode\"+\n\x0e\x65ro_type_entry\x12\n\n\x02ip\x18\x01 \x02(\r\x12\r\n\x05\x66lags\x18\x02 \x01(\t\"/\n\rero_ipv4_type\x12\x1e\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x0f.ero_type_entry\"Q\n\x0erro_type_entry\x12\x0e\n\x06nodeid\x18\x01 \x01(\r\x12\r\n\x05\x66lags\x18\x02 \x01(\r\x12\x11\n\tintf_addr\x18\x03 \x01(\r\x12\r\n\x05label\x18\x04 \x01(\r\"3\n\rrro_ipv4_type\x12\"\n\trro_entry\x18\x01 \x03(\x0b\x32\x0f.rro_type_entry\"\x9f\x01\n\x19lsp_monitor_data_property\x12\x11\n\tbandwidth\x18\x01 \x01(\x04\x12\x11\n\tpath_name\x18\x02 \x01(\t\x12\x0e\n\x06metric\x18\x03 \x01(\x05\x12\x12\n\nmax_avg_bw\x18\x04 \x01(\x02\x12\x1b\n\x03\x65ro\x18\x05 \x01(\x0b\x32\x0e.ero_ipv4_type\x12\x1b\n\x03rro\x18\x06 \x01(\x0b\x32\x0e.rro_ipv4_type\"\x84\x01\n\x07lsp_mon\x12\x17\n\tkey_field\x18\x01 \x02(\x0b\x32\x04.key\x12,\n\x0b\x65vent_field\x18\x02 \x01(\x0b\x32\x17.lsp_monitor_data_event\x12\x32\n\x0eproperty_field\x18\x03 \x01(\x0b\x32\x1a.lsp_monitor_data_property*\xbb\x03\n\tlsp_event\x12\r\n\tINITIATED\x10\x00\x12\x10\n\x0c\x43ONCLUDED_UP\x10\x01\x12\x17\n\x13\x43ONCLUDED_TORN_DOWN\x10\x02\x12\x18\n\x14PROTECTION_AVAILABLE\x10\x03\x12\x1a\n\x16PROTECTION_UNAVAILABLE\x10\x04\x12\x12\n\x0e\x41UTOBW_SUCCESS\x10\x05\x12\x0f\n\x0b\x41UTOBW_FAIL\x10\x06\x12\x16\n\x12RESV_TEAR_RECEIVED\x10\x07\x12\x18\n\x14\x44\x45SELECT_ACTIVE_PATH\x10\x08\x12\x16\n\x12\x43HANGE_ACTIVE_PATH\x10\t\x12\r\n\tDETOUR_UP\x10\n\x12\x0f\n\x0b\x44\x45TOUR_DOWN\x10\x0b\x12\x11\n\rORIGINATE_MBB\x10\x0c\x12\x16\n\x12SELECT_ACTIVE_PATH\x10\r\x12\x11\n\rCSPF_NO_ROUTE\x10\x0e\x12\x10\n\x0c\x43SPF_SUCCESS\x10\x0f\x12\x19\n\x15RESTART_RECOVERY_FAIL\x10\x10\x12\x14\n\x10PATHERR_RECEIVED\x10\x11\x12\x13\n\x0fPATH_MTU_CHANGE\x10\x12\x12\x19\n\x15TUNNEL_LOCAL_REPAIRED\x10\x13*\xfc\x01\n\revent_subcode\x12\x1d\n\x19\x41\x44MISSION_CONTROL_FAILURE\x10\x01\x12\x15\n\x11SESSION_PREEMPTED\x10\x02\x12\x13\n\x0f\x42\x41\x44_LOOSE_ROUTE\x10\x03\x12\x14\n\x10\x42\x41\x44_STRICT_ROUTE\x10\x04\x12\x1c\n\x18LABEL_ALLOCATION_FAILURE\x10\x05\x12\x1b\n\x17NON_RSVP_CAPABLE_ROUTER\x10\x06\x12\x0f\n\x0bTTL_EXPIRED\x10\x07\x12\x19\n\x15ROUTING_LOOP_DETECTED\x10\x08\x12#\n\x1fREQUESTED_BANDWIDTH_UNAVAILABLE\x10\tB\x02H\x03')

_LSP_EVENT = _descriptor.EnumDescriptor(
  name='lsp_event',
  full_name='lsp_event',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INITIATED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONCLUDED_UP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONCLUDED_TORN_DOWN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTECTION_AVAILABLE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTECTION_UNAVAILABLE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTOBW_SUCCESS', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTOBW_FAIL', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESV_TEAR_RECEIVED', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESELECT_ACTIVE_PATH', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANGE_ACTIVE_PATH', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DETOUR_UP', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DETOUR_DOWN', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORIGINATE_MBB', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SELECT_ACTIVE_PATH', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CSPF_NO_ROUTE', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CSPF_SUCCESS', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESTART_RECOVERY_FAIL', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PATHERR_RECEIVED', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PATH_MTU_CHANGE', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TUNNEL_LOCAL_REPAIRED', index=19, number=19,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=713,
  serialized_end=1156,
)

lsp_event = enum_type_wrapper.EnumTypeWrapper(_LSP_EVENT)
_EVENT_SUBCODE = _descriptor.EnumDescriptor(
  name='event_subcode',
  full_name='event_subcode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADMISSION_CONTROL_FAILURE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESSION_PREEMPTED', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_LOOSE_ROUTE', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_STRICT_ROUTE', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LABEL_ALLOCATION_FAILURE', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NON_RSVP_CAPABLE_ROUTER', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TTL_EXPIRED', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUTING_LOOP_DETECTED', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUESTED_BANDWIDTH_UNAVAILABLE', index=8, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1159,
  serialized_end=1411,
)

event_subcode = enum_type_wrapper.EnumTypeWrapper(_EVENT_SUBCODE)
INITIATED = 0
CONCLUDED_UP = 1
CONCLUDED_TORN_DOWN = 2
PROTECTION_AVAILABLE = 3
PROTECTION_UNAVAILABLE = 4
AUTOBW_SUCCESS = 5
AUTOBW_FAIL = 6
RESV_TEAR_RECEIVED = 7
DESELECT_ACTIVE_PATH = 8
CHANGE_ACTIVE_PATH = 9
DETOUR_UP = 10
DETOUR_DOWN = 11
ORIGINATE_MBB = 12
SELECT_ACTIVE_PATH = 13
CSPF_NO_ROUTE = 14
CSPF_SUCCESS = 15
RESTART_RECOVERY_FAIL = 16
PATHERR_RECEIVED = 17
PATH_MTU_CHANGE = 18
TUNNEL_LOCAL_REPAIRED = 19
ADMISSION_CONTROL_FAILURE = 1
SESSION_PREEMPTED = 2
BAD_LOOSE_ROUTE = 3
BAD_STRICT_ROUTE = 4
LABEL_ALLOCATION_FAILURE = 5
NON_RSVP_CAPABLE_ROUTER = 6
TTL_EXPIRED = 7
ROUTING_LOOP_DETECTED = 8
REQUESTED_BANDWIDTH_UNAVAILABLE = 9



_KEY = _descriptor.Descriptor(
  name='key',
  full_name='key',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='key.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instance_identifier', full_name='key.instance_identifier', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_stampg', full_name='key.time_stampg', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=17,
  serialized_end=86,
)


_LSP_MONITOR_DATA_EVENT = _descriptor.Descriptor(
  name='lsp_monitor_data_event',
  full_name='lsp_monitor_data_event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_identifier', full_name='lsp_monitor_data_event.event_identifier', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subcode', full_name='lsp_monitor_data_event.subcode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=88,
  serialized_end=183,
)


_ERO_TYPE_ENTRY = _descriptor.Descriptor(
  name='ero_type_entry',
  full_name='ero_type_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='ero_type_entry.ip', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flags', full_name='ero_type_entry.flags', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=185,
  serialized_end=228,
)


_ERO_IPV4_TYPE = _descriptor.Descriptor(
  name='ero_ipv4_type',
  full_name='ero_ipv4_type',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry', full_name='ero_ipv4_type.entry', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=230,
  serialized_end=277,
)


_RRO_TYPE_ENTRY = _descriptor.Descriptor(
  name='rro_type_entry',
  full_name='rro_type_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodeid', full_name='rro_type_entry.nodeid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flags', full_name='rro_type_entry.flags', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='intf_addr', full_name='rro_type_entry.intf_addr', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='rro_type_entry.label', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=279,
  serialized_end=360,
)


_RRO_IPV4_TYPE = _descriptor.Descriptor(
  name='rro_ipv4_type',
  full_name='rro_ipv4_type',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rro_entry', full_name='rro_ipv4_type.rro_entry', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=362,
  serialized_end=413,
)


_LSP_MONITOR_DATA_PROPERTY = _descriptor.Descriptor(
  name='lsp_monitor_data_property',
  full_name='lsp_monitor_data_property',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bandwidth', full_name='lsp_monitor_data_property.bandwidth', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path_name', full_name='lsp_monitor_data_property.path_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metric', full_name='lsp_monitor_data_property.metric', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_avg_bw', full_name='lsp_monitor_data_property.max_avg_bw', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ero', full_name='lsp_monitor_data_property.ero', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rro', full_name='lsp_monitor_data_property.rro', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=416,
  serialized_end=575,
)


_LSP_MON = _descriptor.Descriptor(
  name='lsp_mon',
  full_name='lsp_mon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_field', full_name='lsp_mon.key_field', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_field', full_name='lsp_mon.event_field', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='property_field', full_name='lsp_mon.property_field', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=578,
  serialized_end=710,
)

_LSP_MONITOR_DATA_EVENT.fields_by_name['event_identifier'].enum_type = _LSP_EVENT
_LSP_MONITOR_DATA_EVENT.fields_by_name['subcode'].enum_type = _EVENT_SUBCODE
_ERO_IPV4_TYPE.fields_by_name['entry'].message_type = _ERO_TYPE_ENTRY
_RRO_IPV4_TYPE.fields_by_name['rro_entry'].message_type = _RRO_TYPE_ENTRY
_LSP_MONITOR_DATA_PROPERTY.fields_by_name['ero'].message_type = _ERO_IPV4_TYPE
_LSP_MONITOR_DATA_PROPERTY.fields_by_name['rro'].message_type = _RRO_IPV4_TYPE
_LSP_MON.fields_by_name['key_field'].message_type = _KEY
_LSP_MON.fields_by_name['event_field'].message_type = _LSP_MONITOR_DATA_EVENT
_LSP_MON.fields_by_name['property_field'].message_type = _LSP_MONITOR_DATA_PROPERTY
DESCRIPTOR.message_types_by_name['key'] = _KEY
DESCRIPTOR.message_types_by_name['lsp_monitor_data_event'] = _LSP_MONITOR_DATA_EVENT
DESCRIPTOR.message_types_by_name['ero_type_entry'] = _ERO_TYPE_ENTRY
DESCRIPTOR.message_types_by_name['ero_ipv4_type'] = _ERO_IPV4_TYPE
DESCRIPTOR.message_types_by_name['rro_type_entry'] = _RRO_TYPE_ENTRY
DESCRIPTOR.message_types_by_name['rro_ipv4_type'] = _RRO_IPV4_TYPE
DESCRIPTOR.message_types_by_name['lsp_monitor_data_property'] = _LSP_MONITOR_DATA_PROPERTY
DESCRIPTOR.message_types_by_name['lsp_mon'] = _LSP_MON

class key(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _KEY

  # @@protoc_insertion_point(class_scope:key)

class lsp_monitor_data_event(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LSP_MONITOR_DATA_EVENT

  # @@protoc_insertion_point(class_scope:lsp_monitor_data_event)

class ero_type_entry(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ERO_TYPE_ENTRY

  # @@protoc_insertion_point(class_scope:ero_type_entry)

class ero_ipv4_type(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ERO_IPV4_TYPE

  # @@protoc_insertion_point(class_scope:ero_ipv4_type)

class rro_type_entry(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RRO_TYPE_ENTRY

  # @@protoc_insertion_point(class_scope:rro_type_entry)

class rro_ipv4_type(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RRO_IPV4_TYPE

  # @@protoc_insertion_point(class_scope:rro_ipv4_type)

class lsp_monitor_data_property(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LSP_MONITOR_DATA_PROPERTY

  # @@protoc_insertion_point(class_scope:lsp_monitor_data_property)

class lsp_mon(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LSP_MON

  # @@protoc_insertion_point(class_scope:lsp_mon)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'H\003')
# @@protoc_insertion_point(module_scope)
