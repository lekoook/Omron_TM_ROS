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
    :type cl:string
    :initform "")
   (goal_goal2
    :reader goal_goal2
    :initarg :goal_goal2
    :type cl:string
    :initform "")
   (goal_goal3
    :reader goal_goal3
    :initarg :goal_goal3
    :type cl:string
    :initform "")
   (goal_goal4
    :reader goal_goal4
    :initarg :goal_goal4
    :type cl:string
    :initform "")
   (goal_goal5
    :reader goal_goal5
    :initarg :goal_goal5
    :type cl:string
    :initform "")
   (goal_goal6
    :reader goal_goal6
    :initarg :goal_goal6
    :type cl:string
    :initform "")
   (goal_goal7
    :reader goal_goal7
    :initarg :goal_goal7
    :type cl:string
    :initform "")
   (goal_goal8
    :reader goal_goal8
    :initarg :goal_goal8
    :type cl:string
    :initform "")
   (goal_goal9
    :reader goal_goal9
    :initarg :goal_goal9
    :type cl:string
    :initform "")
   (goal_goal10
    :reader goal_goal10
    :initarg :goal_goal10
    :type cl:string
    :initform "")
   (goal_goal11
    :reader goal_goal11
    :initarg :goal_goal11
    :type cl:string
    :initform "")
   (goal_goal12
    :reader goal_goal12
    :initarg :goal_goal12
    :type cl:string
    :initform ""))
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

(cl:ensure-generic-function 'goal_goal7-val :lambda-list '(m))
(cl:defmethod goal_goal7-val ((m <ActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_motion-msg:goal_goal7-val is deprecated.  Use tm_motion-msg:goal_goal7 instead.")
  (goal_goal7 m))

(cl:ensure-generic-function 'goal_goal8-val :lambda-list '(m))
(cl:defmethod goal_goal8-val ((m <ActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_motion-msg:goal_goal8-val is deprecated.  Use tm_motion-msg:goal_goal8 instead.")
  (goal_goal8 m))

(cl:ensure-generic-function 'goal_goal9-val :lambda-list '(m))
(cl:defmethod goal_goal9-val ((m <ActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_motion-msg:goal_goal9-val is deprecated.  Use tm_motion-msg:goal_goal9 instead.")
  (goal_goal9 m))

(cl:ensure-generic-function 'goal_goal10-val :lambda-list '(m))
(cl:defmethod goal_goal10-val ((m <ActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_motion-msg:goal_goal10-val is deprecated.  Use tm_motion-msg:goal_goal10 instead.")
  (goal_goal10 m))

(cl:ensure-generic-function 'goal_goal11-val :lambda-list '(m))
(cl:defmethod goal_goal11-val ((m <ActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_motion-msg:goal_goal11-val is deprecated.  Use tm_motion-msg:goal_goal11 instead.")
  (goal_goal11 m))

(cl:ensure-generic-function 'goal_goal12-val :lambda-list '(m))
(cl:defmethod goal_goal12-val ((m <ActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_motion-msg:goal_goal12-val is deprecated.  Use tm_motion-msg:goal_goal12 instead.")
  (goal_goal12 m))
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
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'goal_goal1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'goal_goal1))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'goal_goal2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'goal_goal2))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'goal_goal3))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'goal_goal3))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'goal_goal4))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'goal_goal4))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'goal_goal5))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'goal_goal5))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'goal_goal6))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'goal_goal6))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'goal_goal7))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'goal_goal7))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'goal_goal8))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'goal_goal8))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'goal_goal9))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'goal_goal9))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'goal_goal10))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'goal_goal10))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'goal_goal11))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'goal_goal11))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'goal_goal12))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'goal_goal12))
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
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'goal_goal1) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'goal_goal1) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'goal_goal2) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'goal_goal2) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'goal_goal3) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'goal_goal3) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'goal_goal4) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'goal_goal4) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'goal_goal5) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'goal_goal5) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'goal_goal6) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'goal_goal6) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'goal_goal7) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'goal_goal7) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'goal_goal8) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'goal_goal8) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'goal_goal9) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'goal_goal9) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'goal_goal10) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'goal_goal10) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'goal_goal11) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'goal_goal11) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'goal_goal12) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'goal_goal12) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
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
  "f77355aacb91e97eb06df0dbd18cbf5e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ActionGoal)))
  "Returns md5sum for a message object of type 'ActionGoal"
  "f77355aacb91e97eb06df0dbd18cbf5e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ActionGoal>)))
  "Returns full string definition for message of type '<ActionGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Goal~%string goal_function~%string goal_param~%string goal_goal1~%string goal_goal2~%string goal_goal3~%string goal_goal4~%string goal_goal5~%string goal_goal6~%string goal_goal7~%string goal_goal8~%string goal_goal9~%string goal_goal10~%string goal_goal11~%string goal_goal12~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ActionGoal)))
  "Returns full string definition for message of type 'ActionGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Goal~%string goal_function~%string goal_param~%string goal_goal1~%string goal_goal2~%string goal_goal3~%string goal_goal4~%string goal_goal5~%string goal_goal6~%string goal_goal7~%string goal_goal8~%string goal_goal9~%string goal_goal10~%string goal_goal11~%string goal_goal12~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ActionGoal>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'goal_function))
     4 (cl:length (cl:slot-value msg 'goal_param))
     4 (cl:length (cl:slot-value msg 'goal_goal1))
     4 (cl:length (cl:slot-value msg 'goal_goal2))
     4 (cl:length (cl:slot-value msg 'goal_goal3))
     4 (cl:length (cl:slot-value msg 'goal_goal4))
     4 (cl:length (cl:slot-value msg 'goal_goal5))
     4 (cl:length (cl:slot-value msg 'goal_goal6))
     4 (cl:length (cl:slot-value msg 'goal_goal7))
     4 (cl:length (cl:slot-value msg 'goal_goal8))
     4 (cl:length (cl:slot-value msg 'goal_goal9))
     4 (cl:length (cl:slot-value msg 'goal_goal10))
     4 (cl:length (cl:slot-value msg 'goal_goal11))
     4 (cl:length (cl:slot-value msg 'goal_goal12))
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
    (cl:cons ':goal_goal7 (goal_goal7 msg))
    (cl:cons ':goal_goal8 (goal_goal8 msg))
    (cl:cons ':goal_goal9 (goal_goal9 msg))
    (cl:cons ':goal_goal10 (goal_goal10 msg))
    (cl:cons ':goal_goal11 (goal_goal11 msg))
    (cl:cons ':goal_goal12 (goal_goal12 msg))
))
