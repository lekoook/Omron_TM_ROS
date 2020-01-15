;; Auto-generated. Do not edit!


(when (boundp 'tm_motion::TmMotion)
  (if (not (find-package "TM_MOTION"))
    (make-package "TM_MOTION"))
  (shadow 'TmMotion (find-package "TM_MOTION")))
(unless (find-package "TM_MOTION::TMMOTION")
  (make-package "TM_MOTION::TMMOTION"))
(unless (find-package "TM_MOTION::TMMOTIONREQUEST")
  (make-package "TM_MOTION::TMMOTIONREQUEST"))
(unless (find-package "TM_MOTION::TMMOTIONRESPONSE")
  (make-package "TM_MOTION::TMMOTIONRESPONSE"))

(in-package "ROS")





(defclass tm_motion::TmMotionRequest
  :super ros::object
  :slots (_a ))

(defmethod tm_motion::TmMotionRequest
  (:init
   (&key
    ((:a __a) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _a __a)
   self)
  (:a
   (&optional __a)
   (if __a (setq _a __a)) _a)
  (:serialization-length
   ()
   (+
    ;; string[] _a
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _a)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string[] _a
     (write-long (length _a) s)
     (dolist (elem _a)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string[] _a
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _a (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _a i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(defclass tm_motion::TmMotionResponse
  :super ros::object
  :slots (_device ))

(defmethod tm_motion::TmMotionResponse
  (:init
   (&key
    ((:device __device) "")
    )
   (send-super :init)
   (setq _device (string __device))
   self)
  (:device
   (&optional __device)
   (if __device (setq _device __device)) _device)
  (:serialization-length
   ()
   (+
    ;; string _device
    4 (length _device)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _device
       (write-long (length _device) s) (princ _device s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _device
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _device (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass tm_motion::TmMotion
  :super ros::object
  :slots ())

(setf (get tm_motion::TmMotion :md5sum-) "b2778cec932742b2c8b6d125219e8d85")
(setf (get tm_motion::TmMotion :datatype-) "tm_motion/TmMotion")
(setf (get tm_motion::TmMotion :request) tm_motion::TmMotionRequest)
(setf (get tm_motion::TmMotion :response) tm_motion::TmMotionResponse)

(defmethod tm_motion::TmMotionRequest
  (:response () (instance tm_motion::TmMotionResponse :init)))

(setf (get tm_motion::TmMotionRequest :md5sum-) "b2778cec932742b2c8b6d125219e8d85")
(setf (get tm_motion::TmMotionRequest :datatype-) "tm_motion/TmMotionRequest")
(setf (get tm_motion::TmMotionRequest :definition-)
      "string[] a
---
string device

")

(setf (get tm_motion::TmMotionResponse :md5sum-) "b2778cec932742b2c8b6d125219e8d85")
(setf (get tm_motion::TmMotionResponse :datatype-) "tm_motion/TmMotionResponse")
(setf (get tm_motion::TmMotionResponse :definition-)
      "string[] a
---
string device

")



(provide :tm_motion/TmMotion "b2778cec932742b2c8b6d125219e8d85")


