#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "sensor_msgs/msg/joy.hpp"

using namespace std::chrono_literals;

class RobotController : public rclcpp::Node
{
  public:
    RobotController(): Node("robot_controller_node"), count_(0)
    {
      publisher_ = this->create_publisher<std_msgs::msg::String>("robot_mode", 10);
      subscription_ = this->create_subscription<sensor_msgs::msg::Joy>("joy", 10, std::bind(&RobotController::joystick_callback), this);
    }

  private:
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    rclcpp::Subscription<sensor_msgs::msg::Joy>::SharedPtr subscription_;
    size_t count_;
    // Publish
    void timer_callback()
    {
      auto message = std_msgs::msg::String();
      message.data = "Hello, world! ";
      RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
      publisher_->publish(message);
    }
    // Subscription 
    void joystick_callback(const sensor_msgs::msg::Joy::SharedPtr joystick_msg) const
    {
      auto manual_control_btn = joystick_msg->buttons[2];
      if(manual_control_btn == 1){
        RCLCPP_INFO(this->get_logger(), "Got it!");
      }
    }
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<RobotController>());
  rclcpp::shutdown();
  return 0;
}