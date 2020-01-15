; Auto-generated. Do not edit!


(cl:in-package tm_motion-srv)


;//! \htmlinclude TmMotion-request.msg.html

(cl:defclass <TmMotion-request> (roslisp-msg-protocol:ros-message)
  ((a
    :reader a
    :initarg :a
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element "")))
)

(cl:defclass TmMotion-request (<TmMotion-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TmMotion-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TmMotion-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tm_motion-srv:<TmMotion-request> is deprecated: use tm_motion-srv:TmMotion-request instead.")))

(cl:ensure-generic-function 'a-val :lambda-list '(m))
(cl:defmethod a-val ((m <TmMotion-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_motion-srv:a-val is deprecated.  Use tm_motion-srv:a instead.")
  (a m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TmMotion-request>) ostream)
  "Serializes a message object of type '<TmMotion-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'a))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'a))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TmMotion-request>) istream)
  "Deserializes a message object of type '<TmMotion-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'a) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'a)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TmMotion-request>)))
  "Returns string type for a service object of type '<TmMotion-request>"
  "tm_motion/TmMotionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TmMotion-request)))
  "Returns string type for a service object of type 'TmMotion-request"
  "tm_motion/TmMotionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TmMotion-request>)))
  "Returns md5sum for a message object of type '<TmMotion-request>"
  "b2778cec932742b2c8b6d125219e8d85")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TmMotion-request)))
  "Returns md5sum for a message object of type 'TmMotion-request"
  "b2778cec932742b2c8b6d125219e8d85")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TmMotion-request>)))
  "Returns full string definition for message of type '<TmMotion-request>"
  (cl:format cl:nil "string[] a~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TmMotion-request)))
  "Returns full string definition for message of type 'TmMotion-request"
  (cl:format cl:nil "string[] a~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TmMotion-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'a) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TmMotion-request>))
  "Converts a ROS message object to a list"
  (cl:list 'TmMotion-request
    (cl:cons ':a (a msg))
))
;//! \htmlinclude TmMotion-response.msg.html

(cl:defclass <TmMotion-response> (roslisp-msg-protocol:ros-message)
  ((device
    :reader device
    :initarg :device
    :type cl:string
    :initform ""))
)

(cl:defclass TmMotion-response (<TmMotion-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TmMotion-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TmMotion-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tm_motion-srv:<TmMotion-response> is deprecated: use tm_motion-srv:TmMotion-response instead.")))

(cl:ensure-generic-function 'device-val :lambda-list '(m))
(cl:defmethod device-val ((m <TmMotion-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_motion-srv:device-val is deprecated.  Use tm_motion-srv:device instead.")
  (device m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TmMotion-response>) ostream)
  "Serializes a message object of type '<TmMotion-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'device))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'device))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TmMotion-response>) istream)
  "Deserializes a message object of type '<TmMotion-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'device) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'device) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TmMotion-response>)))
  "Returns string type for a service object of type '<TmMotion-response>"
  "tm_motion/TmMotionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TmMotion-response)))
  "Returns string type for a service object of type 'TmMotion-response"
  "tm_motion/TmMotionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TmMotion-response>)))
  "Returns md5sum for a message object of type '<TmMotion-response>"
  "b2778cec932742b2c8b6d125219e8d85")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TmMotion-response)))
  "Returns md5sum for a message object of type 'TmMotion-response"
  "b2778cec932742b2c8b6d125219e8d85")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TmMotion-response>)))
  "Returns full string definition for message of type '<TmMotion-response>"
  (cl:format cl:nil "string device~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TmMotion-response)))
  "Returns full string definition for message of type 'TmMotion-response"
  (cl:format cl:nil "string device~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TmMotion-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'device))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TmMotion-response>))
  "Converts a ROS message object to a list"
  (cl:list 'TmMotion-response
    (cl:cons ':device (device msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'TmMotion)))
  'TmMotion-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'TmMotion)))
  'TmMotion-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TmMotion)))
  "Returns string type for a service object of type '<TmMotion>"
  "tm_motion/TmMotion")