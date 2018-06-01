import tensorflow as tf

# node1 = tf.constant(3.0)
# node2 = tf.constant(4.0)
# node3 = tf.add(node1, node2)

# sess = tf.Session()  

# print(sess.run([node1, node2, node3]))


a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

adder_node = a + b

sess = tf.Session();

print(sess.run(adder_node, { a:3.1,b:5.5 }))

print(sess.run(adder_node, { a: [1,3], b: [4,5] }))

sess.close()


