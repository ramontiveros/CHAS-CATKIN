; Auto-generated. Do not edit!


(cl:in-package dji_sdk-msg)


;//! \htmlinclude WaypointNavigationGoal.msg.html

(cl:defclass <WaypointNavigationGoal> (roslisp-msg-protocol:ros-message)
  ((waypoint_list
    :reader waypoint_list
    :initarg :waypoint_list
    :type dji_sdk-msg:WaypointList
    :initform (cl:make-instance 'dji_sdk-msg:WaypointList)))
)

(cl:defclass WaypointNavigationGoal (<WaypointNavigationGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <WaypointNavigationGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'WaypointNavigationGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dji_sdk-msg:<WaypointNavigationGoal> is deprecated: use dji_sdk-msg:WaypointNavigationGoal instead.")))

(cl:ensure-generic-function 'waypoint_list-val :lambda-list '(m))
(cl:defmethod waypoint_list-val ((m <WaypointNavigationGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dji_sdk-msg:waypoint_list-val is deprecated.  Use dji_sdk-msg:waypoint_list instead.")
  (waypoint_list m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <WaypointNavigationGoal>) ostream)
  "Serializes a message object of type '<WaypointNavigationGoal>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'waypoint_list) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <WaypointNavigationGoal>) istream)
  "Deserializes a message object of type '<WaypointNavigationGoal>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'waypoint_list) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<WaypointNavigationGoal>)))
  "Returns string type for a message object of type '<WaypointNavigationGoal>"
  "dji_sdk/WaypointNavigationGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WaypointNavigationGoal)))
  "Returns string type for a message object of type 'WaypointNavigationGoal"
  "dji_sdk/WaypointNavigationGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<WaypointNavigationGoal>)))
  "Returns md5sum for a message object of type '<WaypointNavigationGoal>"
  "f8c17a2713443e9792d80cdae0b731c2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'WaypointNavigationGoal)))
  "Returns md5sum for a message object of type 'WaypointNavigationGoal"
  "f8c17a2713443e9792d80cdae0b731c2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<WaypointNavigationGoal>)))
  "Returns full string definition for message of type '<WaypointNavigationGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%WaypointList waypoint_list~%~%================================================================================~%MSG: dji_sdk/WaypointList~%Waypoint[] waypoint_list~%~%================================================================================~%MSG: dji_sdk/Waypoint~%#latitude is in degree~%float64 latitude~%#longitude is in degree~%float64 longitude~%float32 altitude~%#heading is in [-180,180]~%int16 heading ~%#stay time is in second~%uint16 staytime~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'WaypointNavigationGoal)))
  "Returns full string definition for message of type 'WaypointNavigationGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%WaypointList waypoint_list~%~%================================================================================~%MSG: dji_sdk/WaypointList~%Waypoint[] waypoint_list~%~%================================================================================~%MSG: dji_sdk/Waypoint~%#latitude is in degree~%float64 latitude~%#longitude is in degree~%float64 longitude~%float32 altitude~%#heading is in [-180,180]~%int16 heading ~%#stay time is in second~%uint16 staytime~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <WaypointNavigationGoal>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'waypoint_list))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <WaypointNavigationGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'WaypointNavigationGoal
    (cl:cons ':waypoint_list (waypoint_list msg))
))
