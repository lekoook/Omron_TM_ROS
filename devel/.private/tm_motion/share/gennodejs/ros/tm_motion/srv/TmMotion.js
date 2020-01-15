// Auto-generated. Do not edit!

// (in-package tm_motion.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class TmMotionRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.a = null;
    }
    else {
      if (initObj.hasOwnProperty('a')) {
        this.a = initObj.a
      }
      else {
        this.a = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TmMotionRequest
    // Serialize message field [a]
    bufferOffset = _arraySerializer.string(obj.a, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TmMotionRequest
    let len;
    let data = new TmMotionRequest(null);
    // Deserialize message field [a]
    data.a = _arrayDeserializer.string(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.a.forEach((val) => {
      length += 4 + val.length;
    });
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'tm_motion/TmMotionRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4f6bc51cbf7510cc87897366558eca7b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string[] a
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TmMotionRequest(null);
    if (msg.a !== undefined) {
      resolved.a = msg.a;
    }
    else {
      resolved.a = []
    }

    return resolved;
    }
};

class TmMotionResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.device = null;
    }
    else {
      if (initObj.hasOwnProperty('device')) {
        this.device = initObj.device
      }
      else {
        this.device = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TmMotionResponse
    // Serialize message field [device]
    bufferOffset = _serializer.float64(obj.device, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TmMotionResponse
    let len;
    let data = new TmMotionResponse(null);
    // Deserialize message field [device]
    data.device = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'tm_motion/TmMotionResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c7c8e2bbfbe24a7d431a1b7094d844bc';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 device
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TmMotionResponse(null);
    if (msg.device !== undefined) {
      resolved.device = msg.device;
    }
    else {
      resolved.device = 0.0
    }

    return resolved;
    }
};

module.exports = {
  Request: TmMotionRequest,
  Response: TmMotionResponse,
  md5sum() { return '484bd188cd41111d4e02ce9b6e0a0b66'; },
  datatype() { return 'tm_motion/TmMotion'; }
};
