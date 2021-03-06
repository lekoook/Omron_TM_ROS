// Generated by gencpp from file tm_motion/TmMotion.msg
// DO NOT EDIT!


#ifndef TM_MOTION_MESSAGE_TMMOTION_H
#define TM_MOTION_MESSAGE_TMMOTION_H

#include <ros/service_traits.h>


#include <tm_motion/TmMotionRequest.h>
#include <tm_motion/TmMotionResponse.h>


namespace tm_motion
{

struct TmMotion
{

typedef TmMotionRequest Request;
typedef TmMotionResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct TmMotion
} // namespace tm_motion


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::tm_motion::TmMotion > {
  static const char* value()
  {
    return "b2778cec932742b2c8b6d125219e8d85";
  }

  static const char* value(const ::tm_motion::TmMotion&) { return value(); }
};

template<>
struct DataType< ::tm_motion::TmMotion > {
  static const char* value()
  {
    return "tm_motion/TmMotion";
  }

  static const char* value(const ::tm_motion::TmMotion&) { return value(); }
};


// service_traits::MD5Sum< ::tm_motion::TmMotionRequest> should match 
// service_traits::MD5Sum< ::tm_motion::TmMotion > 
template<>
struct MD5Sum< ::tm_motion::TmMotionRequest>
{
  static const char* value()
  {
    return MD5Sum< ::tm_motion::TmMotion >::value();
  }
  static const char* value(const ::tm_motion::TmMotionRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::tm_motion::TmMotionRequest> should match 
// service_traits::DataType< ::tm_motion::TmMotion > 
template<>
struct DataType< ::tm_motion::TmMotionRequest>
{
  static const char* value()
  {
    return DataType< ::tm_motion::TmMotion >::value();
  }
  static const char* value(const ::tm_motion::TmMotionRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::tm_motion::TmMotionResponse> should match 
// service_traits::MD5Sum< ::tm_motion::TmMotion > 
template<>
struct MD5Sum< ::tm_motion::TmMotionResponse>
{
  static const char* value()
  {
    return MD5Sum< ::tm_motion::TmMotion >::value();
  }
  static const char* value(const ::tm_motion::TmMotionResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::tm_motion::TmMotionResponse> should match 
// service_traits::DataType< ::tm_motion::TmMotion > 
template<>
struct DataType< ::tm_motion::TmMotionResponse>
{
  static const char* value()
  {
    return DataType< ::tm_motion::TmMotion >::value();
  }
  static const char* value(const ::tm_motion::TmMotionResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // TM_MOTION_MESSAGE_TMMOTION_H
