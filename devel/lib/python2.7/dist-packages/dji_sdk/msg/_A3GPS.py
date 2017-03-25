# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from dji_sdk/A3GPS.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class A3GPS(genpy.Message):
  _md5sum = "11eb94934f90318efef991e43caf4ed1"
  _type = "dji_sdk/A3GPS"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint32 date #GPS date
uint32 time #GPS time
int32 longitude #unit in degree*10^7
int32 latitude  #unit in degree*10^7
int32 height_above_sea #unit in mm 
float32 velocity_north #unit in cm/s
float32 velocity_east #unit in cm/s
float32 velocity_ground #unit in cm/s
"""
  __slots__ = ['date','time','longitude','latitude','height_above_sea','velocity_north','velocity_east','velocity_ground']
  _slot_types = ['uint32','uint32','int32','int32','int32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       date,time,longitude,latitude,height_above_sea,velocity_north,velocity_east,velocity_ground

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(A3GPS, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.date is None:
        self.date = 0
      if self.time is None:
        self.time = 0
      if self.longitude is None:
        self.longitude = 0
      if self.latitude is None:
        self.latitude = 0
      if self.height_above_sea is None:
        self.height_above_sea = 0
      if self.velocity_north is None:
        self.velocity_north = 0.
      if self.velocity_east is None:
        self.velocity_east = 0.
      if self.velocity_ground is None:
        self.velocity_ground = 0.
    else:
      self.date = 0
      self.time = 0
      self.longitude = 0
      self.latitude = 0
      self.height_above_sea = 0
      self.velocity_north = 0.
      self.velocity_east = 0.
      self.velocity_ground = 0.

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
      buff.write(_struct_2I3i3f.pack(_x.date, _x.time, _x.longitude, _x.latitude, _x.height_above_sea, _x.velocity_north, _x.velocity_east, _x.velocity_ground))
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
      end += 32
      (_x.date, _x.time, _x.longitude, _x.latitude, _x.height_above_sea, _x.velocity_north, _x.velocity_east, _x.velocity_ground,) = _struct_2I3i3f.unpack(str[start:end])
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
      buff.write(_struct_2I3i3f.pack(_x.date, _x.time, _x.longitude, _x.latitude, _x.height_above_sea, _x.velocity_north, _x.velocity_east, _x.velocity_ground))
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
      end += 32
      (_x.date, _x.time, _x.longitude, _x.latitude, _x.height_above_sea, _x.velocity_north, _x.velocity_east, _x.velocity_ground,) = _struct_2I3i3f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2I3i3f = struct.Struct("<2I3i3f")