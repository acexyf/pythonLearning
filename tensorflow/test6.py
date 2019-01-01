import tensorflow as tf

two_node = tf.constant(2)


print(two_node)



three_node = tf.constant(3)

sum_node = two_node + three_node

input_placeholder = tf.placeholder(tf.int32)


sess = tf.Session()
print(sess.run(input_placeholder, feed_dict={input_placeholder:2 }))


