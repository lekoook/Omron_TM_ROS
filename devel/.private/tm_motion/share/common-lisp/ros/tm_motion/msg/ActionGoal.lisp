; Auto-generated. Do not edit!


(cl:in-package tm_motion-msg)


;//! \htmlinclude ActionGoal.msg.html

(cl:defclass <ActionGoal> (roslisp-msg-protocol:ros-message)
  ((goal_function
    :reader goal_function
    :initarg :goal_function
    :type cl:string
    :initform "")
   (goal_param
    :reader goal_param
    :initarg :goal_param
    :type cl:string
    :initform "")
   (goal_goal1
    :reader goal_goal1
    :initarg :goal_goal1
    :type cl:float
    :initform 0.0)
   (goal_goal2
    :reader goal_goal2
    :initarg :goal_goal2
    :type cl:float
    :initform 0.0)
   (goal_goal3
    :reader goal_goal3
    :initarg :goal_goal3
    :type cl:float
    :initform 0.0)
   (goal_goal4
    :reader goal_goal4
    :initarg :goal_goal4
    :type cl:float
    :initform 0.0)
   (goal_goal5
    :reader goal_goal5
    :initarg :goal_goal5
    :type cl:float
    :initform 0.0)
   (goal_goal6
    :reader goal_goal6
    :initarg :goal_goal6
    :type cl:float
    :initform 0.0))
)

(cl:defclass ActionGoal (<ActionGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ActionGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ActionGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tm_motion-msg:<ActionGoal> is deprecated: use tm_motion-msg:ActionGoal instead.")))

(cl:ensure-generic-function 'goal_function-val :lambda-list '(m))
(cl:defmethod goal_function-val ((m <ActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_motion-msg:goal_function-val is deprecated.  Use tm_motion-msg:goal_function instead.")
  (goal_function m))

(cl:ensure-generic-function 'goal_param-val :lambda-list '(m))
(cl:defmethod goal_param-val ((m <ActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_motion-msg:goal_param-val is deprecated.  Use tm_motion-msg:goal_param instead.")
  (goal_param m))

(cl:ensure-generic-function 'goal_goal1-val :lambda-list '(m))
(cl:defmethod goal_goal1-val ((m <ActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_motion-msg:goal_goal1-val is deprecated.  Use tm_motion-msg:goal_goal1 instead.")
  (goal_goal1 m))

(cl:ensure-generic-function 'goal_goal2-val :lambda-list '(m))
(cl:defmethod goal_goal2-val ((m <ActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_motion-msg:goal_goal2-val is deprecated.  Use tm_motion-msg:goal_goal2 instead.")
  (goal_goal2 m))

(cl:ensure-generic-function 'goal_goal3-val :lambda-list '(m))
(cl:defmethod goal_goal3-val ((m <ActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_motion-msg:goal_goal3-val is deprecated.  Use tm_motion-msg:goal_goal3 instead.")
  (goal_goal3 m))

(cl:ensure-generic-function 'goal_goal4-val :lambda-list '(m))
(cl:defmethod goal_goal4-val ((m <ActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_motion-msg:goal_goal4-val is deprecated.  Use tm_motion-msg:goal_goal4 instead.")
  (goal_goal4 m))

(cl:ensure-generic-function 'goal_goal5-val :lambda-list '(m))
(cl:defmethod goal_goal5-val ((m <ActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_motion-msg:goal_goal5-val is deprecated.  Use tm_motion-msg:goal_goal5 instead.")
  (goal_goal5 m))

(cl:ensure-generic-function 'goal_goal6-val :lambda-list '(m))
(cl:defmethod goal_goal6-val ((m <ActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_motion-msg:goal_goal6-val is deprecated.  Use tm_motion-msg:goal_goal6 instead.")
  (goal_goal6 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ActionGoal>) ostream)
  "Serializes a message object of type '<ActionGoal>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'goal_function))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'goal_function))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'goal_param))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'goal_param))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'goal_goal1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'goal_goal2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'goal_goal3))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'goal_goal4))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'goal_goal5))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'goal_goal6))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ActionGoal>) istream)
  "Deserializes a message object of type '<ActionGoal>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'goal_function) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'goal_function) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'goal_param) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'goal_param) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'goal_goal1) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'goal_goal2) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'goal_goal3) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'goal_goal4) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'goal_goal5) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'goal_goal6) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ActionGoal>)))
  "Returns string type for a message object of type '<ActionGoal>"
  "tm_motion/ActionGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ActionGoal)))
  "Returns string type for a message object of type 'ActionGoal"
  "tm_motion/ActionGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ActionGoal>)))
  "Returns md5sum for a message object of type '<ActionGoal>"
  "ad6a855c450be493ec664cf999a8fdac")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ActionGoal)))
  "Returns md5sum for a message object of type 'ActionGoal"
  "ad6a855c450be493ec664cf999a8fdac")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ActionGoal>)))
  "Returns full string definition for message of type '<ActionGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Goal~%string goal_function~%string goal_param~%float64 goal_goal1~%float64 goal_goal2~%float64 goal_goal3~%float64 goal_goal4~%float64 goal_goal5~%float64 goal_goal6~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ActionGoal)))
  "Returns full string definition for message of type 'ActionGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Goal~%string goal_function~%string goal_param~%float64 goal_goal1~%float64 goal_goal2~%float64 goal_goal3~%float64 goal_goal4~%float64 goal_goal5~%float64 goal_goal6~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ActionGoal>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'goal_function))
     4 (cl:length (cl:slot-value msg 'goal_param))
     8
     8
     8
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ActionGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'ActionGoal
    (cl:cons ':goal_function (goal_function msg))
    (cl:cons ':goal_param (goal_param msg))
    (cl:cons ':goal_goal1 (goal_goal1 msg))
    (cl:cons ':goal_goal2 (goal_goal2 msg))
    (cl:cons ':goal_goal3 (goal_goal3 msg))
    (cl:cons ':goal_goal4 (goal_goal4 msg))
    (cl:cons ':goal_goal5 (goal_goal5 msg))
    (cl:cons ':goal_goal6 (goal_goal6 msg))
))
