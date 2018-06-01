import tensorflow as tf

# import input_data
# mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)


a = tf.Variable(2, name='scalar')
b = tf.Variable([2, 3], name='vector')
c = tf.Variable([[0, 1], [2, 3]], name='matrix')
w = tf.Variable(tf.zeros([784, 10]), name='weight')

assign_op = a.assign(100)


with tf.Session() as sess:
    sess.run(a.initializer)
    sess.run(assign_op)
    print(a.eval())


matrix1 = tf.constant([[3., 3.]])

matrix2 = tf.constant([[2.],[2.]])

product = tf.matmul(matrix1, matrix2)


sess = tf.Session()


result = sess.run(product)


print(result)

sess.close()