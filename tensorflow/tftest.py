import tensorflow as tf
hello = tf.constant('Hello Glen Pi Geekers, this is TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
