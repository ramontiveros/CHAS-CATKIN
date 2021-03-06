# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from dji_sdk/GimbalAngleControlRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GimbalAngleControlRequest(genpy.Message):
  _md5sum = "3ada515ce6b45dc1f09c576bfab01d4a"
  _type = "dji_sdk/GimbalAngleControlRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """


int16 yaw
int16 roll
int16 pitch
int16 duration

bool absolute_or_incremental
bool yaw_cmd_ignore
bool roll_cmd_ignore
bool pitch_cmd_ignore
"""
  __slots__ = ['yaw','roll','pitch','duration','absolute_or_incremental','yaw_cmd_ignore','roll_cmd_ignore','pitch_cmd_ignore']
  _slot_types = ['int16','int16','int16','int16','bool','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       yaw,roll,pitch,duration,absolute_or_incremental,yaw_cmd_ignore,roll_cmd_ignore,pitch_cmd_ignore

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GimbalAngleControlRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.yaw is None:
        self.yaw = 0
      if self.roll is None:
        self.roll = 0
      if self.pitch is None:
        self.pitch = 0
      if self.duration is None:
        self.duration = 0
      if self.absolute_or_incremental is None:
        self.absolute_or_incremental = False
      if self.yaw_cmd_ignore is None:
        self.yaw_cmd_ignore = False
      if self.roll_cmd_ignore is None:
        self.roll_cmd_ignore = False
      if self.pitch_cmd_ignore is None:
        self.pitch_cmd_ignore = False
    else:
      self.yaw = 0
      self.roll = 0
      self.pitch = 0
      self.duration = 0
      self.absolute_or_incremental = False
      self.yaw_cmd_ignore = False
      self.roll_cmd_ignore = False
      self.pitch_cmd_ignore = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_4h4B.pack(_x.yaw, _x.roll, _x.pitch, _x.duration, _x.absolute_or_incremental, _x.yaw_cmd_ignore, _x.roll_cmd_ignore, _x.pitch_cmd_ignore))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.yaw, _x.roll, _x.pitch, _x.duration, _x.absolute_or_incremental, _x.yaw_cmd_ignore, _x.roll_cmd_ignore, _x.pitch_cmd_ignore,) = _struct_4h4B.unpack(str[start:end])
      self.absolute_or_incremental = bool(self.absolute_or_incremental)
      self.yaw_cmd_ignore = bool(self.yaw_cmd_ignore)
      self.roll_cmd_ignore = bool(self.roll_cmd_ignore)
      self.pitch_cmd_ignore = bool(self.pitch_cmd_ignore)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_4h4B.pack(_x.yaw, _x.roll, _x.pitch, _x.duration, _x.absolute_or_incremental, _x.yaw_cmd_ignore, _x.roll_cmd_ignore, _x.pitch_cmd_ignore))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.yaw, _x.roll, _x.pitch, _x.duration, _x.absolute_or_incremental, _x.yaw_cmd_ignore, _x.roll_cmd_ignore, _x.pitch_cmd_ignore,) = _struct_4h4B.unpack(str[start:end])
      self.absolute_or_incremental = bool(self.absolute_or_incremental)
      self.yaw_cmd_ignore = bool(self.yaw_cmd_ignore)
      self.roll_cmd_ignore = bool(self.roll_cmd_ignore)
      self.pitch_cmd_ignore = bool(self.pitch_cmd_ignore)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4h4B = struct.Struct("<4h4B")
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from dji_sdk/GimbalAngleControlResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GimbalAngleControlResponse(genpy.Message):
  _md5sum = "eb13ac1f1354ccecb7941ee8fa2192e8"
  _type = "dji_sdk/GimbalAngleControlResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool result

"""
  __slots__ = ['result']
  _slot_types = ['bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       result

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GimbalAngleControlResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.result is None:
        self.result = False
    else:
      self.result = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_struct_B.pack(self.result))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 1
      (self.result,) = _struct_B.unpack(str[start:end])
      self.result = bool(self.result)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_struct_B.pack(self.result))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 1
      (self.result,) = _struct_B.unpack(str[start:end])
      self.result = bool(self.result)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B = struct.Struct("<B")
class GimbalAngleControl(object):
  _type          = 'dji_sdk/GimbalAngleControl'
  _md5sum = '355893b815576f75c0061dddd133c146'
  _request_class  = GimbalAngleControlRequest
  _response_class = GimbalAngleControlResponse
