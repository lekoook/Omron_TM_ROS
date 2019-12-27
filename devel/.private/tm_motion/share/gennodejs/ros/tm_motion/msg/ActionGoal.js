// Auto-generated. Do not edit!

// (in-package tm_motion.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class ActionGoal {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.goal_function = null;
      this.goal_param = null;
      this.goal_goal1 = null;
      this.goal_goal2 = null;
      this.goal_goal3 = null;
      this.goal_goal4 = null;
      this.goal_goal5 = null;
      this.goal_goal6 = null;
    }
    else {
      if (initObj.hasOwnProperty('goal_function')) {
        this.goal_function = initObj.goal_function
      }
      else {
        this.goal_function = '';
      }
      if (initObj.hasOwnProperty('goal_param')) {
        this.goal_param = initObj.goal_param
      }
      else {
        this.goal_param = '';
      }
      if (initObj.hasOwnProperty('goal_goal1')) {
        this.goal_goal1 = initObj.goal_goal1
      }
      else {
        this.goal_goal1 = '';
      }
      if (initObj.hasOwnProperty('goal_goal2')) {
        this.goal_goal2 = initObj.goal_goal2
      }
      else {
        this.goal_goal2 = '';
      }
      if (initObj.hasOwnProperty('goal_goal3')) {
        this.goal_goal3 = initObj.goal_goal3
      }
      else {
        this.goal_goal3 = '';
      }
      if (initObj.hasOwnProperty('goal_goal4')) {
        this.goal_goal4 = initObj.goal_goal4
      }
      else {
        this.goal_goal4 = '';
      }
      if (initObj.hasOwnProperty('goal_goal5')) {
        this.goal_goal5 = initObj.goal_goal5
      }
      else {
        this.goal_goal5 = '';
      }
      if (initObj.hasOwnProperty('goal_goal6')) {
        this.goal_goal6 = initObj.goal_goal6
      }
      else {
        this.goal_goal6 = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ActionGoal
    // Serialize message field [goal_function]
    bufferOffset = _serializer.string(obj.goal_function, buffer, bufferOffset);
    // Serialize message field [goal_param]
    bufferOffset = _serializer.string(obj.goal_param, buffer, bufferOffset);
    // Serialize message field [goal_goal1]
    bufferOffset = _serializer.string(obj.goal_goal1, buffer, bufferOffset);
    // Serialize message field [goal_goal2]
    bufferOffset = _serializer.string(obj.goal_goal2, buffer, bufferOffset);
    // Serialize message field [goal_goal3]
    bufferOffset = _serializer.string(obj.goal_goal3, buffer, bufferOffset);
    // Serialize message field [goal_goal4]
    bufferOffset = _serializer.string(obj.goal_goal4, buffer, bufferOffset);
    // Serialize message field [goal_goal5]
    bufferOffset = _serializer.string(obj.goal_goal5, buffer, bufferOffset);
    // Serialize message field [goal_goal6]
    bufferOffset = _serializer.string(obj.goal_goal6, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ActionGoal
    let len;
    let data = new ActionGoal(null);
    // Deserialize message field [goal_function]
    data.goal_function = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [goal_param]
    data.goal_param = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [goal_goal1]
    data.goal_goal1 = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [goal_goal2]
    data.goal_goal2 = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [goal_goal3]
    data.goal_goal3 = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [goal_goal4]
    data.goal_goal4 = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [goal_goal5]
    data.goal_goal5 = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [goal_goal6]
    data.goal_goal6 = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.goal_function.length;
    length += object.goal_param.length;
    length += object.goal_goal1.length;
    length += object.goal_goal2.length;
    length += object.goal_goal3.length;
    length += object.goal_goal4.length;
    length += object.goal_goal5.length;
    length += object.goal_goal6.length;
    return length + 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'tm_motion/ActionGoal';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'bdea93a608d7ca728e6127b539a20557';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    # Goal
    string goal_function
    string goal_param
    string goal_goal1
    string goal_goal2
    string goal_goal3
    string goal_goal4
    string goal_goal5
    string goal_goal6
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ActionGoal(null);
    if (msg.goal_function !== undefined) {
      resolved.goal_function = msg.goal_function;
    }
    else {
      resolved.goal_function = ''
    }

    if (msg.goal_param !== undefined) {
      resolved.goal_param = msg.goal_param;
    }
    else {
      resolved.goal_param = ''
    }

    if (msg.goal_goal1 !== undefined) {
      resolved.goal_goal1 = msg.goal_goal1;
    }
    else {
      resolved.goal_goal1 = ''
    }

    if (msg.goal_goal2 !== undefined) {
      resolved.goal_goal2 = msg.goal_goal2;
    }
    else {
      resolved.goal_goal2 = ''
    }

    if (msg.goal_goal3 !== undefined) {
      resolved.goal_goal3 = msg.goal_goal3;
    }
    else {
      resolved.goal_goal3 = ''
    }

    if (msg.goal_goal4 !== undefined) {
      resolved.goal_goal4 = msg.goal_goal4;
    }
    else {
      resolved.goal_goal4 = ''
    }

    if (msg.goal_goal5 !== undefined) {
      resolved.goal_goal5 = msg.goal_goal5;
    }
    else {
      resolved.goal_goal5 = ''
    }

    if (msg.goal_goal6 !== undefined) {
      resolved.goal_goal6 = msg.goal_goal6;
    }
    else {
      resolved.goal_goal6 = ''
    }

    return resolved;
    }
};

module.exports = ActionGoal;
