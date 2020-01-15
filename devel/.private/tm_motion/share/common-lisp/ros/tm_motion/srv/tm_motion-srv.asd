
(cl:in-package :asdf)

(defsystem "tm_motion-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "TmMotion" :depends-on ("_package_TmMotion"))
    (:file "_package_TmMotion" :depends-on ("_package"))
  ))