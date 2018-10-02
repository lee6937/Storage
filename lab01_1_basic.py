import tensorflow as tf
import numpy as np

node1 = tf.constant(3.0)
node2 = tf.constant(4.0)   
node3 = tf.add(node1, node2)

sess = tf.Session()
print("node1: ", sess.run(node1), "node2: ", sess.run(node2))
print("node3: ", sess.run(node3))

