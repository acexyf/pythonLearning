import tensorflow as tf

a = tf.constant([2, 2], name='a1')
b = tf.constant([[0, 1], [2, 3]], name='b1')
x = tf.multiply(a, b, name='dot_production')

print(a)
print(b)

with tf.Session() as sess:
    writer = tf.summary.FileWriter('./graphs', sess.graph)
    print(sess.run(x))
writer.close()