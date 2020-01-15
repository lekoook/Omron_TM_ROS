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
    ((:device __device) 0.0)
    )
   (send-super :init)
   (setq _device (float __device))
   self)
  (:device
   (&optional __device)
   (if __device (setq _device __device)) _device)
  (:serialization-length
   ()
   (+
    ;; float64 _device
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _device
       (sys::poke _device (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _device
     (setq _device (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass tm_motion::TmMotion
  :super ros::object
  :slots ())

(setf (get tm_motion::TmMotion :md5sum-) "484bd188cd41111d4e02ce9b6e0a0b66")
(setf (get tm_motion::TmMotion :datatype-) "tm_motion/TmMotion")
(setf (get tm_motion::TmMotion :request) tm_motion::TmMotionRequest)
(setf (get tm_motion::TmMotion :response) tm_motion::TmMotionResponse)

(defmethod tm_motion::TmMotionRequest
  (:response () (instance tm_motion::TmMotionResponse :init)))

(setf (get tm_motion::TmMotionRequest :md5sum-) "484bd188cd41111d4e02ce9b6e0a0b66")
(setf (get tm_motion::TmMotionRequest :datatype-) "tm_motion/TmMotionRequest")
(setf (get tm_motion::TmMotionRequest :definition-)
      "string[] a
---
float64 device

")

(setf (get tm_motion::TmMotionResponse :md5sum-) "484bd188cd41111d4e02ce9b6e0a0b66")
(setf (get tm_motion::TmMotionResponse :datatype-) "tm_motion/TmMotionResponse")
(setf (get tm_motion::TmMotionResponse :definition-)
      "string[] a
---
float64 device

")



(provide :tm_motion/TmMotion "484bd188cd41111d4e02ce9b6e0a0b66")


