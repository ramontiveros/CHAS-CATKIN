; Auto-generated. Do not edit!


(cl:in-package dji_sdk-msg)


;//! \htmlinclude LocalPositionNavigationResult.msg.html

(cl:defclass <LocalPositionNavigationResult> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass LocalPositionNavigationResult (<LocalPositionNavigationResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LocalPositionNavigationResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LocalPositionNavigationResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dji_sdk-msg:<LocalPositionNavigationResult> is deprecated: use dji_sdk-msg:LocalPositionNavigationResult instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <LocalPositionNavigationResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dji_sdk-msg:result-val is deprecated.  Use dji_sdk-msg:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LocalPositionNavigationResult>) ostream)
  "Serializes a message object of type '<LocalPositionNavigationResult>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LocalPositionNavigationResult>) istream)
  "Deserializes a message object of type '<LocalPositionNavigationResult>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LocalPositionNavigationResult>)))
  "Returns string type for a message object of type '<LocalPositionNavigationResult>"
  "dji_sdk/LocalPositionNavigationResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LocalPositionNavigationResult)))
  "Returns string type for a message object of type 'LocalPositionNavigationResult"
  "dji_sdk/LocalPositionNavigationResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LocalPositionNavigationResult>)))
  "Returns md5sum for a message object of type '<LocalPositionNavigationResult>"
  "eb13ac1f1354ccecb7941ee8fa2192e8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LocalPositionNavigationResult)))
  "Returns md5sum for a message object of type 'LocalPositionNavigationResult"
  "eb13ac1f1354ccecb7941ee8fa2192e8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LocalPositionNavigationResult>)))
  "Returns full string definition for message of type '<LocalPositionNavigationResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LocalPositionNavigationResult)))
  "Returns full string definition for message of type 'LocalPositionNavigationResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LocalPositionNavigationResult>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LocalPositionNavigationResult>))
  "Converts a ROS message object to a list"
  (cl:list 'LocalPositionNavigationResult
    (cl:cons ':result (result msg))
))
