#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

nodeName, topicName = 'Publicador_de_Messagem', 'Informacao'

rospy.init_node(nodeName, anonymous = True)

publisher1 = rospy.Publisher(topicName, Int32, queue_size = 5)

# Taxa de publicação da menssagem, no caso é 1 Hz. Ou seja, 1 mensagem a cada segundo.
ratePublisher = rospy.Rate(1)
intMessage = 0

while not rospy.is_shutdown():
   
    rospy.loginfo(intMessage)    
    publisher1.publish(intMessage) # A mensagem publicada
    intMessage = intMessage + 1    # Modificando a mensagem publicada, adiocionamos +1
    ratePublisher.sleep()          # Esperamos, isso garante que a taxa de publicacao é atingingida.

