import rospy
import sys
from std_msgs.msg import String


# Display received message
def show_msg(msg):
    print(f'[Received]: {msg.data}')


# Send messages
def talk():
    pub = rospy.Publisher(publish_to, String, queue_size=10)
    while not rospy.is_shutdown():
        msg = input()
        if not pub.get_num_connections():
            print('No listeners connected!')
        else:
            pub.publish(msg)


# Listen for messages
def listen():
    rospy.Subscriber(sub_to, String, show_msg)


# Start chatter
if __name__ == '__main__':
    try:
        publish_to = sys.argv[1]
        sub_to = sys.argv[2]
        rospy.init_node('chatter', anonymous=True)
        listen()
        talk()
    except IndexError:
        print('Missing arguments!')
    except rospy.ROSInterruptException:
        print('Exiting ROS chatter...')
